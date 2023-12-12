from django.db import models
from django.contrib.auth.models import User
import hashlib

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # You should use a secure way to store passwords in production, such as hashing.

    def set_password(self, raw_password):
        """
        Set the password using SHA-256 hashing.
        """
        self.password = hashlib.sha256(raw_password.encode()).hexdigest()

    def check_password(self, raw_password):
        """
        Check if the provided password matches the stored hashed password.
        """
        return self.password == hashlib.sha256(raw_password.encode()).hexdigest()

    def save(self, *args, **kwargs):
        """
        Automatically hash the password before saving.
        """
        if not self.password.startswith('sha256$'):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s {self.website_name} Password"

