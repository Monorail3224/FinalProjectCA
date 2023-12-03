from django.urls import path
from . import views


urlpatterns = [

    # Add URL paths here
    path('',views.index,name='index'),

    # User Registration and Authentication
    path('api/register/', views.register_user, name='register_user'),
    path('api/login/', views.login_user, name='login_user'),
    path('api/logout/', views.logout_user, name='logout_user'),

    # TOTP Setup and Verification
    path('api/totp/setup/', views.setup_totp, name='setup_totp'),
    path('api/totp/verify/', views.verify_totp, name='verify_totp'),
    path('api/totp/reset/', views.reset_totp, name='reset_totp'),

    # User Profile Management
    path('api/profile/', views.get_profile, name='get_profile'),
    path('api/profile/update/', views.update_profile, name='update_profile'),

    # Password and 2FA Settings Management
    path('api/password/reset/', views.reset_password, name='reset_password'),
    path('api/2fa/', views.manage_2fa_settings, name='manage_2fa_settings'),

    # Admin User Management and Logs
    path('api/users/', views.manage_users, name='manage_users'),
    path('api/logs/', views.view_logs, name='view_logs'),

    # Token Management
    path('api/token/', views.generate_token, name='generate_token'),

    # API Versioning (if needed)
    # path('api/v1/register/', views.register_user, name='v1_register_user'),
    # path('api/v1/login/', views.login_user, name='v1_login_user'),
    # ...

    # Add more endpoints as needed for your project
]
