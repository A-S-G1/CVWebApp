from django.contrib import admin
from .models import AboutMeContent, Skill, Experience, Education, Achievement

# Register your models here.

@admin.register(AboutMeContent)
class AboutMeContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'phone', 'updated_at')
    # Fields to display in the form for editing
    fieldsets = (
        (None, {
            'fields': ('title', 'bio_content', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'address', 'linkedin', 'github', 'languages')
        }),
    )
    # To ensure only one AboutMeContent instance, you can use a custom form or method
    # For now, we'll rely on users only creating one entry.

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'duration', 'start_date', 'end_date')
    list_filter = ('institution',)
    search_fields = ('degree', 'institution')
    date_hierarchy = 'start_date'

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('description', 'order')
    list_editable = ('order',)
    search_fields = ('description',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'order')
    list_editable = ('category', 'level', 'order') # Allows editing directly from list view
    list_filter = ('category', 'level')
    search_fields = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'company')
    search_fields = ('title', 'company', 'description')
    date_hierarchy = 'start_date' # Adds a date filter at the top
