"""
URL configuration for TOTP_WebsiteApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web_app import views
from django.views.generic import RedirectView

urlpatterns = [
    path('web_app/', include('web_app.urls')), 
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='accounts/login/')),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('profile/',views.CustomLoginView.as_view(), name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('account_info/', views.AccountInfoView.as_view(), name='account_info'),
    path('add_account/', views.AddAccountView.as_view(), name='add_account'),
    path('view_account/', views.ViewAccountView.as_view(), name='view_account'),
    path('view_account/<int:pk>/', views.PasswordEntryDetailView.as_view(), name='passwordentry_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
]
