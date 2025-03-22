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
    response = client.get('/')
    assert response.status_code == 200
    assert b'Project Showcase' in response.data

def test_about_page(client):
    """Test that about page loads successfully"""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About Project Showcase' in response.data

def test_404_page(client):
    """Test 404 error handling"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
    assert b'Page Not Found' in response.data

def test_api_projects_endpoint(client):
    """Test the projects API endpoint"""
    response = client.get('/api/projects')
    assert response.status_code == 200
    data = response.get_json()
    assert 'projects' in data
    assert isinstance(data['projects'], list)
    assert len(data['projects']) > 0

def test_api_categories_endpoint(client):
    """Test the categories API endpoint"""
    response = client.get('/api/categories')
    assert response.status_code == 200
    data = response.get_json()
    assert 'categories' in data
    assert isinstance(data['categories'], list)
    assert len(data['categories']) > 0
    # Check if categories are unique
    assert len(data['categories']) == len(set(data['categories']))

def test_search_functionality(client):
    """Test search functionality"""
    # Test with existing title
    search_term = items[0]['title']
    response = client.get(f'/api/projects?search={search_term}')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['projects']) > 0
    assert any(search_term.lower() in p['title'].lower() for p in data['projects'])

    # Test with non-existent term
    response = client.get('/api/projects?search=nonexistentproject123456')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['projects']) == 0

def test_category_filter(client):
    """Test category filtering"""
    # Test with existing category
    category = items[0]['category']
    response = client.get(f'/api/projects?category={category}')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['projects']) > 0
    assert all(p['category'] == category for p in data['projects'])

    # Test with non-existent category
    response = client.get('/api/projects?category=nonexistentcategory123456')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data['projects']) == 0

def test_specific_project_endpoint(client):
    """Test getting a specific project"""
    # Test with existing project
    project_id = items[0]['id']
    response = client.get(f'/api/projects/{project_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert 'project' in data
    assert data['project']['id'] == project_id

    # Test with non-existent project
    response = client.get('/api/projects/999')
    assert response.status_code == 404
