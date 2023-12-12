from django.db import models
from django.contrib.auth.models import User

# Exetending upon the User model to include a phone number
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
# Model defined to store website-specific passwords
class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)  # Store hashed passwords securely

    def __str__(self):
        return f"{self.user.username}'s {self.website_name} Password"
