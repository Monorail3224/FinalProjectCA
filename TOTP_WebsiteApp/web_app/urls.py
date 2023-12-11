from django.urls import path, include
from . import views
from django.views.generic import RedirectView

#Register the App Namespace
app_name = 'web_app'

urlpatterns = [

    
    # Add URL paths here

    # User Registration and Authentication
    path('<str:feature>/', views.account_settings, name='account_options'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    
]