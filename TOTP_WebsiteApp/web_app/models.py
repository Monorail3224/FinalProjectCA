from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    # Other fields for user details (e.g., name, email)

    # Add profile fields like full name, profile picture, etc.

    # Add related_name to avoid clashes with auth.User's groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')


# Add related_name to the ForeignKey fields to resolve the clash
class PasswordEntry(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # Other fields for additional information (e.g., date created, notes)

class LoginHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    login_successful = models.BooleanField(default=True)

