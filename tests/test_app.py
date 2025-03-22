import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads successfully"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Project' in rv.data

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

def test_category_filter(client):
    """Test category filtering"""
    rv = client.get('/api/projects?category=Technology')
    assert rv.status_code == 200
    json_data = rv.get_json()
    projects = json_data['projects']
    assert all(p['category'] == 'Technology' for p in projects)
