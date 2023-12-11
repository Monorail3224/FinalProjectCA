from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PasswordEntry
from .utils import send_sms

# Model to create a new user
class SignUpView(CreateView):
    model = User  # Use the built-in User model
    form_class = CustomUserCreationForm  # Use the custom form
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Call the parent class's form_valid method to save the user
        response = super().form_valid(form)

        # Send an SMS after successful signup
        user = self.object  # The newly created user

        # Fetch the phone number from the form for the user who just signed up
        user_phone_number = form.cleaned_data.get('phone_number')

        message = "Welcome to my Password Manager app! Thanks for signing up. We will take great care in managing your passwords. >:)"
        send_sms(user_phone_number, message)

        # Log the user in after signup
        login(self.request, user)

        return response

class CustomLoginView(LoginView):
    template_name = 'registration/profile.html'  # Replace with the path to your login template
    success_url = reverse_lazy('profile')  # Replace with the URL to redirect to after login

@method_decorator(login_required, name='dispatch')
class AccountInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'account_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the user's information
        user = self.request.user
        context['user'] = user
        # Add any additional context data you need for the account_info.html template
        return context


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
