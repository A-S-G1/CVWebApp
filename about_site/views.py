from django.shortcuts import render

def specs_view(request):
    """
    Renders the web app specifications page.
    Contains hardcoded data about the technologies used.
    """
    tech_specs = {
        'Backend Development': {
            'Language': 'Python',
            'Framework': 'Django (Version 5.2.1)',
            'Database': 'SQLite (used for development and small projects)',
            'API Integration': 'OpenAI API (for AI Assistant functionality)',
            'Environment Management': 'Virtual Environments (venv)',
            'Dependency Management': 'pip',
            'Environment Variables': 'python-dotenv'
        },
        'Frontend Development': {
            'Languages': 'HTML5, CSS3, JavaScript',
            'CSS Framework': 'Tailwind CSS (via CDN for simplicity)',
            'Icons': 'Font Awesome',
            'Animations/Transitions': 'Custom CSS (keyframe animations) and JavaScript (for page transitions)',
            'Templating Engine': 'Django Templates (Jinja-like syntax)'
        },
        'AI Assistant Model': {
            'Provider': 'OpenAI',
            'Model': 'GPT-3.5 Turbo (configurable to other models like GPT-4)'
        },
        'Deployment Considerations (Future)': 'For production, typically Gunicorn (WSGI server), Nginx (web server), and a PostgreSQL database. Could be deployed on cloud platforms like Heroku, Vercel, or Google Cloud.',
        'Version Control': 'Git / GitHub (for collaborative development and tracking changes)'
    }
    return render(request, 'about_site/specs.html', {'tech_specs': tech_specs})
