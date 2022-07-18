from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['username','name', 'email', 'type', 'customer_id']

