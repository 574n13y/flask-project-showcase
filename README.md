# Flask Project Showcase

A modern web application built with Flask that showcases various projects in a clean, responsive interface. The application displays a collection of projects in a card-based layout, making it easy to browse and view project details.

## Features

- Responsive card-based grid layout for project display
- Bootstrap-powered modern UI design
- Dynamic project data integration
- About page with additional information
- Clean and organized template structure using Jinja2
- Mobile-friendly interface

## Tech Stack

- Python 3.10+
- Flask 3.0.0
- Werkzeug 3.0.1
- Bootstrap (for responsive design)
- HTML5/CSS3
- Jinja2 templating

## Project Structure

```
pywebapplication/
├── .github/
│   └── workflows/        # GitHub Actions workflows
├── templates/
│   ├── base.html        # Base template with common layout
│   ├── index.html       # Home page with project cards
│   └── about.html       # About page template
├── app.py              # Main Flask application file
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd pywebapplication
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

The application will display a grid of project cards on the home page and provide navigation to an about page.

## Development

The application uses GitHub Actions for CI/CD pipeline, which includes:
- Code quality checks with flake8
- Python syntax verification
- Automated testing of application startup
- Dependency installation verification

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
