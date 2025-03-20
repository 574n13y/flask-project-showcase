from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Sample data - in a real app, this would typically come from a database
items = [
    {
        'id': 1,
        'title': 'Project Alpha',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 2,
        'title': 'Project Beta',
        'description': 'Innovation at its finest',
        'date': '2025-03-13'
    },
    {
        'id': 3,
        'title': 'Project Gamma',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 4,
        'title': 'Project Delta',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 5,
        'title': 'Project Epsilon',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 6,
        'title': 'Project Zeta',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 7,
        'title': 'Project Eta',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 8,
        'title': 'Project Theta',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 9,
        'title': 'Project Iota',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 10,
        'title': 'Project Kappa',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 11,
        'title': 'Project Lambda',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 12,
        'title': 'Project Mu',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 13,
        'title': 'Project Nu',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 14    ,
        'title': 'Project Xi',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 15,
        'title': 'Project Omicron',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 16,
        'title': 'Project Pi',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 17,
        'title': 'Project Rho',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 18,
        'title': 'Project Sigma',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 19,
        'title': 'Project Tau',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 20,
        'title': 'Project Upsilon',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    }
]

@app.route('/')
def home():
    return render_template('index.html', items=items)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
