"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Import settings
from django.conf.urls.static import static # Import static function to serve media files

urlpatterns = [
    path('admin/', admin.site.urls), # Django Admin interface
    path('', include('portfolio.urls')),       # Portfolio app (your CV pages)
    path('ai-assistant/', include('ai_assistant.urls')), # AI assistant API endpoint
    path('blog/', include('blog.urls')),       # Blog app for posts
    path('contact/', include('contact.urls')), # Contact/Feedback form
    path('specs/', include('about_site.urls')),# Web App Specifications page
]

# ONLY serve media files during development (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
