from django.urls import path
from . import views

# Define app_name for namespacing URLs (e.g., {% url 'contact:feedback_form' %})
app_name = 'contact'

urlpatterns = [
    path('', views.feedback_form_view, name='feedback_form'), # URL for the feedback form
]
