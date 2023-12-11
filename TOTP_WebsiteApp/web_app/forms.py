# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import CustomUser, PasswordEntry

# Your CustomUserCreationForm remains unchanged
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number')


class LoginForm(AuthenticationForm):
    username = UsernameField(label=("Your Username"),
                             widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password = forms.CharField(
        label=("Your Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
    )

# Modify the UpdatePasswordForm to work with the PasswordEntry model
class UpdatePasswordForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry  # Change the model to PasswordEntry
        fields = ['website', 'username', 'password', 'description']

        widgets = {
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Website URL',
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),
            'password': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description',
            }),
        }
