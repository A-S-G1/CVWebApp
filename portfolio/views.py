from django.shortcuts import render
# Import models from about_site app
from about_site.models import AboutMeContent, Skill, Experience, Education, Achievement
# Import the Project model from the current portfolio app
from .models import Project
# Also keep Post if you plan to display latest blog posts or other blog content on portfolio pages
from blog.models import Post

# --- View Functions (updated to use models) ---

def about_me(request):
    """
    Renders the 'About Me' page with personal information and education
    fetched from the database.
    """
    # Fetch the About Me content (assuming you'll have only one main entry)
    about_me_content = AboutMeContent.objects.first()

    # Fetch all education entries
    education_data = Education.objects.all().order_by('-start_date')

    # Fetch all achievements
    achievements_data = Achievement.objects.all().order_by('order')

    context = {
        'my_info': about_me_content, # This object now contains bio, contact, image etc.
        'education': education_data,
        'achievements': achievements_data,
    }
    return render(request, 'portfolio/about.html', context)

def work_experience(request):
    """
    Renders the 'Work Experience' page, fetching data from the database.
    """
    experience_data = Experience.objects.all().order_by('-start_date')
    return render(request, 'portfolio/experience.html', {'experience': experience_data})

def skills(request):
    """
    Renders the 'Skills' page, fetching data from the database.
    Categorizes skills by their defined 'category'.
    """
    skills_data = Skill.objects.all().order_by('category', 'order', 'name') # Order by category, then order, then name
    categorized_skills = {}
    for skill in skills_data:
        # Use the skill's category for grouping
        category_display_name = dict(Skill.CATEGORY_CHOICES).get(skill.category, skill.category.capitalize())
        if category_display_name not in categorized_skills:
            categorized_skills[category_display_name] = []
        categorized_skills[category_display_name].append(skill)

    return render(request, 'portfolio/skills.html', {'skills': categorized_skills})

def projects(request): # Renamed function from test_apps to projects for clarity
    """
    Renders the 'Projects' page, fetching project data from the database.
    """
    projects_data = Project.objects.all().order_by('-created_at') # Fetch all projects, newest first
    return render(request, 'portfolio/projects.html', {'projects': projects_data})

