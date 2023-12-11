from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser
from .utils import send_sms
from . import models
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Replace with the path to your login template
    form_class = LoginForm  # Use the custom login form
    success_url = reverse_lazy('profile')  # Redirect to the user's profile page upon successful login

    def user_login_view(self):
        if self.request.user.is_authenticated:
            return redirect('profile')
        return LoginView.as_view()(self.request)

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

@login_required
def profile_view(request):
    # Implement the logic to display user's profile and password entries
    return render(request, 'profile.html')

@login_required
def change_password_view(request):
    # Implement the logic for changing the user's password
    return render(request, 'change_password.html')

@login_required
def delete_profile_view(request):
    # Implement the logic for deleting the user's profile
    return render(request, 'delete_profile.html')

# Model To create a new user
class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm  # Use the custom form
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        # Call the parent class's form_valid method to save the user
        response = super().form_valid(form)

        # Send an SMS after successful signup
        user = self.object  # The newly created user

        # Fetch the phone number from the database for the user who just signed up
        user_with_phone_number = CustomUser.objects.get(pk=user.pk)
        user_phone_number = user_with_phone_number.phone_number

        message = "Welcome to my Password Manager app! Thanks for signing up. We will take great care in managing your passwords. >:)"
        send_sms(user_phone_number, message)

        # Log the user in after signup
        login(self.request, user)

        return response
