from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator

class CustomUser(AbstractUser):
    # Add custom fields to the user model
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone_number = models.CharField(validators=[MinLengthValidator(7), MaxLengthValidator(15)], max_length=30, blank=False)

    # Add profile fields like full name, profile picture, etc.

    class Meta:
        # Add a unique constraint to avoid clashes with auth.User
        unique_together = ('username', 'email')

    # Specify custom related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True,
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username  # Customize the string representation as needed

class UserLog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # Describe the user's action, e.g., login, logout
    timestamp = models.DateTimeField(auto_now_add=True)

class AccessToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)  # Store the access token
    timestamp = models.DateTimeField(auto_now_add=True)
