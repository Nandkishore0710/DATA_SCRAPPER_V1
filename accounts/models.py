from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)
    
    # We use a string reference 'jobs.Package' to avoid circular imports
    package = models.ForeignKey('jobs.Package', on_delete=models.SET_NULL, null=True, blank=True)
    
    searches_left = models.IntegerField(default=5)
    leads_scraped = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
