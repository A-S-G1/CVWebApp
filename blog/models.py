from django.db import models
from django.utils import timezone # Import timezone for automatic timestamps

class Post(models.Model):
    title = models.CharField(max_length=200)
    # Slug for clean URLs (e.g., /blog/my-first-post/)
    slug = models.SlugField(max_length=200, unique=True, help_text="A short label for the URL, contains only letters, numbers, underscores or hyphens.")
    content = models.TextField()
    author = models.CharField(max_length=100, default='Anton Georgiiev') # Default author for new posts
    created_at = models.DateTimeField(auto_now_add=True) # Automatically sets the creation timestamp
    updated_at = models.DateTimeField(auto_now=True) # Automatically updates the timestamp on every save
    # Optional: Image field for post thumbnails
    # image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at'] # Order posts by creation date, newest first

    def __str__(self):
        return self.title # Human-readable representation in the admin
