from django.contrib import admin

# Register your models here.
from .models import Movie, Attend

# Register your models here.
admin.site.register(Movie)
admin.site.register(Attend)
