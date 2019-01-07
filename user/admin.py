from django.contrib import admin

# Register your models here.
#注册模块
from .models import User
admin.site.register(User)