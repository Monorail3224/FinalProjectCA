from django.contrib import admin
from web_app.models import CustomUser, UserLog, AccessToken    
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(UserLog)
admin.site.register(AccessToken)

