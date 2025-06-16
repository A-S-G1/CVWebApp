from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Using URLField for links to external applications or GitHub repos
    app_link = models.URLField(max_length=500, blank=True, null=True, help_text="Link to the live application (if deployed)")
    github_link = models.URLField(max_length=500, blank=True, null=True, help_text="Link to the GitHub repository")
    # Image field for project thumbnails. Requires Pillow library: pip install Pillow
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, help_text="Thumbnail image for the project")
    # Date project was created or last updated (optional but useful)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', 'title'] # Order by newest first, then by title
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

