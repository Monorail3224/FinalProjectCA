from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404

# Default Homepage View
def web_app_home(request):
    # Your index view logic here
    return render(request, 'homepage/index.html')

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

# Define your view functions for reset_password, manage_2fa_settings, etc.
# Replace the placeholders with actual view logic

def reset_password(request):
    # Your reset_password view logic here
    return render(request, 'reset_password.html')

def manage_2fa_settings(request):
    # Your manage_2fa_settings view logic here
    return render(request, 'manage_2fa_settings.html')

# Define your view functions for manage_users, view_logs, etc.
# Replace the placeholders with actual view logic

def manage_users(request):
    # Your manage_users view logic here
    return render(request, 'manage_users.html')

def view_logs(request):
    # Your view_logs view logic here
    return render(request, 'view_logs.html')

# Define your view functions for generate_token, etc.
# Replace the placeholders with actual view logic

def generate_token(request):
    # Your generate_token view logic here
    return render(request, 'generate_token.html')
