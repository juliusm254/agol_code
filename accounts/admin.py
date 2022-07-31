from django.contrib import admin
from .models import User, OperationsUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# @admin.register(User)
# class RequestDemoAdmin(admin.ModelAdmin):
#   list_display = ['username','name', 'email', 'type', 'customer_id']


# @admin.register(OperationsUser)
# class RequestDemoAdmin(admin.ModelAdmin):
#   list_display = ['username','name', 'email', 'type']

class OperationsUserAdmin(UserAdmin):
  pass

admin.site.register(OperationsUser, OperationsUserAdmin)
