from django.urls import path, include
from . import views


urlpatterns = [

    
    # Add URL paths here

    # User Registration and Authentication
    path('<str:feature>/', views.account_settings, name='account_options'),
    path('<str:selection>/', views.totp_settings, name='totp_options'),

]