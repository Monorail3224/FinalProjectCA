from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from . import models

# Default Homepage View
def web_app_home(request):
    return render(request, 'index.html')

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
    
    
    # Define your view functions for register, login, logout, etc.

def totp_settings(request, selection):
    # Account Settings view logic here
    if selection in totp_options:
        return HttpResponse(totp_options[selection])
    else:
        return HttpResponse('Invalid feature')

def list_totpcodes(request):
    # List the TOTP codes for the user
    return HttpResponse('List TOTP Codes')  