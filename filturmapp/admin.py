from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


admin.site.register(Mainfilturm)
admin.site.register(filturm)
admin.site.register(EmpLeave)
admin.site.register(HrLogin)


