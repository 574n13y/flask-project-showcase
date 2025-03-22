import os
import pytest
from app import app, items

@pytest.fixture
def client():
    # Configure app for testing
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'localhost'
    
    # Set template folder to test templates
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    app.template_folder = template_dir
    
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_home_page(client):
    """Test that home page loads successfully"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Project Showcase' in rv.data

def test_about_page(client):
    """Test that about page loads successfully"""
    rv = client.get('/about')
    assert rv.status_code == 200
    assert b'About Project Showcase' in rv.data

def test_api_projects(client):
    """Test the projects API endpoint"""
    rv = client.get('/api/projects')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert 'projects' in json_data
    assert len(json_data['projects']) > 0

def test_404_handling(client):
    """Test 404 error handling"""
    rv = client.get('/nonexistent-page')
    assert rv.status_code == 404
    assert b'Page Not Found' in rv.data

def test_category_filter(client):
    """Test category filtering"""
    # Get a category that exists in our sample data
    first_item_category = items[0]['category']
    rv = client.get(f'/api/projects?category={first_item_category}')
    assert rv.status_code == 200
    json_data = rv.get_json()
    projects = json_data['projects']
    assert len(projects) > 0
    assert all(p['category'] == first_item_category for p in projects)

def test_search_functionality(client):
    """Test search functionality"""
    # Get a word from the first item's title
    search_term = items[0]['title'].split()[0]
    rv = client.get(f'/api/projects?search={search_term}')
    assert rv.status_code == 200
    json_data = rv.get_json()
    projects = json_data['projects']
    assert len(projects) > 0
    assert any(search_term.lower() in p['title'].lower() for p in projects)

def test_categories_endpoint(client):
    """Test the categories API endpoint"""
    rv = client.get('/api/categories')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert 'categories' in json_data
    assert len(json_data['categories']) > 0
    # Verify categories are unique
    categories = json_data['categories']
    assert len(categories) == len(set(categories))

def test_empty_search_results(client):
    """Test search with no results"""
    rv = client.get('/api/projects?search=nonexistentproject123456')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert len(json_data['projects']) == 0

def test_invalid_category(client):
    """Test filtering with invalid category"""
    rv = client.get('/api/projects?category=nonexistentcategory123456')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert len(json_data['projects']) == 0
