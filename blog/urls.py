from django.urls import path
from . import views

# Define app_name for namespacing URLs (e.g., {% url 'blog:post_list' %})
app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'), # URL for the list of all posts
    path('<slug:slug>/', views.post_detail, name='post_detail'), # URL for individual post detail (e.g., /blog/my-first-post/)
]
