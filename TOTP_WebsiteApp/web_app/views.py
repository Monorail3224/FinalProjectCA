from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from . import models
from .forms import loginform
from django.views.generic import CreateView, UpdateView, DeleteView

# Model To create a new user

class CustomUserCreate(CreateView):
    model = models.CustomUser
    fields = ['username', 'website', 'password']
    template_name = 'register.html'
    success_url = '/web_app/login'

# Home view for login/registration

def web_app_home(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            # Handle form submission (e.g., authentication)
            # Redirect to the appropriate view
            pass  # Replace with your logic
    else:
        form = loginform()
    
    return render(request, 'index.html', {'form': form})

#Dictionary Defined for use in Dynamic URL Routing
account_options = {
    'setup_totp' : 'setup_totp',
    'register' : 'register',
    'profile' : 'profile.html',
    'Account_info' : 'Account_info',
    'logout' : 'logout',
    'change_password' : 'change_password',
    'update_profile' : 'update_profile',
    'delete_profile' : 'delete_profile',
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
    
    