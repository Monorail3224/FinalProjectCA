from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    # Add profile fields like full name, profile picture, etc.

class TwoFactorAuthSettings(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    totp_secret_key = models.CharField(max_length=16)  # Store the TOTP secret key securely

class UserLog(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # Describe the user's action, e.g., login, logout
    timestamp = models.DateTimeField(auto_now_add=True)

class AccessToken(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    token = models.CharField(max_length=255)  # Store the access token
    timestamp = models.DateTimeField(auto_now_add=True)

# Additional fields for User model or a custom user model if needed
# class CustomUser(AbstractUser):
#     # Add custom fields here if necessary
#     pass
