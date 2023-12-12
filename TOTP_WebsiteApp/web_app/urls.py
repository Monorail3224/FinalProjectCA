from django.urls import path, include
from . import views
#Register the App Namespace
app_name = 'web_app'

urlpatterns = [

    
    # App level URL configuration. This file is used to route URLs to the appropriate views within 'web_app'.

    # User Registration and Authentication
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),  
    path('account_info/', views.AccountInfoView.as_view(), name='account_info'),
    path('add_account/', views.AccountInfoView.as_view(), name='add_account'),

]