# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, AdminPasswordChangeForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import PasswordEntry
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Your CustomUserCreationForm remains unchanged
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number')


class LoginForm(AuthenticationForm):
     def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                _("This account is inactive."),
                code="inactive",)
        meta
        

