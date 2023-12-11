from django.shortcuts import render, redirect
from django.http.response import Http404
from django.urls import reverse, reverse_lazy
from . import models
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView 
from django.views.generic import CreateView
from .utils import send_sms
from .models import CustomUser 

# Model To create a new user
class SignUpView(CreateView):
    model = models.CustomUser
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

        message = "Welcome to our app! Thanks for signing up."
        send_sms(user_phone_number, message)

        # Log the user in after signup
        login(self.request, user)

        return response
    

class LoggedOutView(LogoutView):
    template_name = 'profile.html'

# Home view for login/registration

def web_app_home(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Handle form submission (e.g., authentication)
            # Redirect to the appropriate view
            pass  # Replace with your logic
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'index.html', {'form': form})


# Dictionary Defined for use in Dynamic URL Routing
account_options = {
    'profile': 'profile.html',
    'Account_info': 'Account_info',
    'logged_out': 'logged_out',
    'change_password': 'change_password',
    'update_profile': 'update_profile',
    'delete_profile': 'delete_profile',
}

# Define your view functions for register, login, logout, etc.

def account_settings(request, feature):
    try:
        template_name = account_options.get(feature)
        if template_name:
            return render(request, template_name)
        else:
            raise Http404("Invalid feature")
    except KeyError:
        raise Http404("Invalid feature")
