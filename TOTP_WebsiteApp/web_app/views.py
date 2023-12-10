from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from . import models
from .forms import loginform

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
    'login' : 'login',
    'Account_info' : 'Account_info',
    'logout' : 'logout',
    'change_password' : 'change_password',
    'update_profile' : 'update_profile',
    'delete_profile' : 'delete_profile',
}

totp_options = {
    'totp_settings' : 'totp_settings',
    'verify_totp' : 'verify_totp',
    'reset_totp' : 'reset_totp',

}

# Define your view functions for register, login, logout, etc.


def account_settings(request, feature):
    try:
        result=account_options[feature]
        return HttpResponse(account_options[feature])
    except:
        raise Http404("Invalid feature")
    
    