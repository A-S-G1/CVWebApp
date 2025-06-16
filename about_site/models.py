from django.db import models

# Model for 'About Me' content (assuming a single, editable block of text)
class AboutMeContent(models.Model):
    # This will hold your main bio and related fixed text
    title = models.CharField(max_length=200, default="About Me Section")
    # Your main biography text
    bio_content = models.TextField(help_text="Your main biography and profile text.")
    # You might consider adding fields for contact info here if you want them editable
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=500, blank=True, null=True)
    github = models.URLField(max_length=500, blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True, help_text="Comma-separated list of languages (e.g., English, Ukrainian, Russian)")
    profile_image = models.ImageField(upload_to='about_me_images/', blank=True, null=True, help_text="Your profile picture")
    
    updated_at = models.DateTimeField(auto_now=True) # Automatically updates on each save

    class Meta:
        verbose_name = "About Me Content"
        verbose_name_plural = "About Me Content"
        # Ordering can be used if you anticipate multiple entries for a specific reason
        # and want to control which one shows up first. For a single 'About Me' block, it's less critical.
        ordering = ['-updated_at'] # Ensures the latest updated entry appears first

    def __str__(self):
        return self.title

# Model for 'Education' entries (moved from portfolio/views.py hardcoded)
class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    duration = models.CharField(max_length=100, help_text="e.g., 2024 - Present")
    start_date = models.DateField(blank=True, null=True) # For chronological ordering in admin
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-start_date'] # Order by most recent education first
        verbose_name = "Education Entry"
        verbose_name_plural = "Education Entries"

    def __str__(self):
        return f"{self.degree} from {self.institution}"

# Model for 'Achievements' entries (moved from portfolio/views.py hardcoded)
class Achievement(models.Model):
    description = models.TextField()
    order = models.IntegerField(default=0, help_text="Order in which achievements are displayed.")

    class Meta:
        ordering = ['order']
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

    def __str__(self):
        return self.description[:50] + "..." if len(self.description) > 50 else self.description

# Model for 'Skills'
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('core', 'Core Skills'),
            ('technical', 'Technical Skills'),
            ('professional', 'Professional Skills'),
            ('other', 'Other Skills'), # Added 'other' for flexibility
        ],
        default='technical', # Default category
        help_text="Category for this skill (e.g., Technical, Core, Professional)"
    )
    # You can add more fields like 'level' (e.g., 'Beginner', 'Intermediate', 'Advanced')
    level = models.CharField(
        max_length=50,
        choices=[
            ('basic', 'Basic'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
            ('expert', 'Expert'),
        ],
        default='intermediate'
    )
    order = models.IntegerField(default=0, help_text="Order in which skills are displayed within their category.")

    class Meta:
        ordering = ['category', 'order', 'name'] # Order by category, then order, then name
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name

# Model for 'Experience' (e.g., work experience, professional roles)
class Experience(models.Model):
    title = models.CharField(max_length=200) # e.g., "Software Developer", "Head of Legal Department"
    company = models.CharField(max_length=200) # e.g., "Google", "LLC, Vesta Develop"
    location = models.CharField(max_length=100, blank=True, null=True) # e.g., "Dublin, Ireland"
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True) # Null for current roles
    description = models.TextField(help_text="Detailed description of responsibilities and achievements.")
    is_current = models.BooleanField(default=False, help_text="Check if this is a current role/education.")

    class Meta:
        ordering = ['-start_date'] # Order by most recent experience first
        verbose_name = "Work Experience Entry"
        verbose_name_plural = "Work Experience Entries"

    def __str__(self):
        return f"{self.title} at {self.company}"
