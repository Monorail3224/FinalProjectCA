from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)  # Store hashed passwords securely

    def save(self, *args, **kwargs):
        # Hash the password before saving it
        if not self.password.startswith('sha256$'):
            self.password = make_password(self.password)
        super(PasswordEntry, self).save(*args, **kwargs)

    def check_password(self, raw_password):
        """
        Check if the provided password matches the stored hashed password.
        """
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.user.username}'s {self.website_name} Password"
