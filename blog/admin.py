from django.contrib import admin
from .models import Post

# Register the Post model with the Django admin site
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Customize the list view in the admin
    list_display = ('title', 'author', 'created_at', 'updated_at')
    # Automatically generate the slug from the title as you type
    prepopulated_fields = {'slug': ('title',)}
    # Add search capability by title and content
    search_fields = ('title', 'content')
    # Add filters for author and creation date
    list_filter = ('author', 'created_at')
    # fields = ('title', 'slug', 'content', 'author', 'image') # Example if you add an image field
