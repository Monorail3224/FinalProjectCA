from django.contrib import admin
from web_app.models import CustomUser, LoginHistory    
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(LoginHistory)


