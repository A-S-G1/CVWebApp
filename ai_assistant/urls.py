from django.urls import path
from . import views

app_name = 'ai_assistant'

urlpatterns = [
    path('chat/', views.chat_with_assistant, name='chat'),
]