from django.urls import path
from . import views

# Define app_name for namespacing URLs (e.g., {% url 'about_site:specs' %})
app_name = 'about_site'

urlpatterns = [
    path('', views.specs_view, name='specs'), # URL for the specifications page
]
