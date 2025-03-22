from flask import Flask, render_template, request, jsonify, abort
import datetime
import os
from config import config

app = Flask(__name__)

# Configure app based on environment
env = os.environ.get('FLASK_ENV', 'default')
app.config.from_object(config[env])

# Sample data - in a real app, this would typically come from a database
items = [
    {
        'id': 1,
        'title': 'Project Alpha',
        'description': 'Revolutionizing AI-driven automation.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 2,
        'title': 'Project Beta',
        'description': 'Advancing next-gen medical research.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 3,
        'title': 'Project Gamma',
        'description': 'Exploring quantum computing applications.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 4,
        'title': 'Project Delta',
        'description': 'Developing sustainable energy solutions.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 5,
        'title': 'Project Epsilon',
        'description': 'Enhancing cybersecurity with AI.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 6,
        'title': 'Project Zeta',
        'description': 'Pioneering advancements in biotechnology.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 7,
        'title': 'Project Eta',
        'description': 'Creating immersive AR experiences.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 8,
        'title': 'Project Theta',
        'description': 'Analyzing climate change patterns.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 9,
        'title': 'Project Iota',
        'description': 'Building next-gen IoT devices.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 10,
        'title': 'Project Kappa',
        'description': 'Investigating human genome sequencing.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 11,
        'title': 'Project Lambda',
        'description': 'Developing blockchain-based solutions.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 12,
        'title': 'Project Mu',
        'description': 'Studying deep-sea ecosystems.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 13,
        'title': 'Project Nu',
        'description': 'Enhancing cloud computing infrastructure.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 14,
        'title': 'Project Xi',
        'description': 'Exploring the effects of space travel.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 15,
        'title': 'Project Omicron',
        'description': 'Integrating AI into smart homes.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 16,
        'title': 'Project Pi',
        'description': 'Advancing neuroscience studies.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 17,
        'title': 'Project Rho',
        'description': 'Improving autonomous vehicle technology.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 18,
        'title': 'Project Sigma',
        'description': 'Developing next-gen cancer treatments.',
        'date': '2025-03-13',
        'category': 'Research'
    },
    {
        'id': 19,
        'title': 'Project Tau',
        'description': 'Innovating AI-driven healthcare.',
        'date': '2025-03-13',
        'category': 'Technology'
    },
    {
        'id': 20,
        'title': 'Project Upsilon',
        'description': 'Investigating renewable energy sources.',
        'date': '2025-03-13',
        'category': 'Research'
    }
]

def filter_items(items_list, search_query=None, category=None):
    """Filter items based on search query and category"""
    filtered = items_list
    if search_query:
        search_query = search_query.lower()
        filtered = [
            item for item in filtered
            if search_query in item['title'].lower() 
            or search_query in item['description'].lower()
        ]
    if category:
        filtered = [
            item for item in filtered
            if item['category'].lower() == category.lower()
        ]
    return filtered

@app.route('/')
def home():
    """Home page route"""
    search_query = request.args.get('search', '')
    current_category = request.args.get('category', '')
    
    filtered_items = filter_items(items, search_query, current_category)
    categories = sorted(set(item['category'] for item in items))
    
    return render_template('index.html', 
                         items=filtered_items,
                         categories=categories,
                         search_query=search_query,
                         current_category=current_category)

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/api/projects')
def get_projects():
    """API endpoint to get filtered projects"""
    search_query = request.args.get('search', '')
    category = request.args.get('category', '')
    
    filtered_items = filter_items(items, search_query, category)
    return jsonify({'projects': filtered_items})

@app.route('/api/categories')
def get_categories():
    """API endpoint to get unique categories"""
    categories = sorted(set(item['category'] for item in items))
    return jsonify({'categories': categories})

@app.route('/api/projects/<int:project_id>')
def get_project(project_id):
    """API endpoint to get a specific project"""
    project = next((item for item in items if item['id'] == project_id), None)
    if project is None:
        abort(404)
    return jsonify({'project': project})

@app.errorhandler(404)
def not_found_error(error):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Use environment variables for configuration
    port = int(os.environ.get('PORT', 5000))
    # Default to localhost for security, allow override via environment
    host = os.environ.get('HOST', '127.0.0.1')  # Default to localhost
    app.run(host=host, port=port)  # Debug mode is set via config