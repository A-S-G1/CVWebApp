from django.urls import path
from . import views # Import views from the current app

app_name = 'portfolio' # Define app_name for namespacing URLs

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('experience/', views.work_experience, name='experience'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'), # CHANGED: views.test_apps to views.projects
]
