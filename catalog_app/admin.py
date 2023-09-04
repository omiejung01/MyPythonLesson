from django.contrib import admin

# Register your models here.
from .models import Account, Transfer

# Register your models here.
admin.site.register(Account)
admin.site.register(Transfer)