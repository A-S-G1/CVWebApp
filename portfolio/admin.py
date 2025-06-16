from django.contrib import admin
from .models import Project # Import the Project model

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'app_link', 'github_link', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    # If you want to use the slug for a unique URL for each project (optional)
    # prepopulated_fields = {'slug': ('title',)}
