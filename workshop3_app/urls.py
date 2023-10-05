from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('attend', views.attend, name='attend'),
#    path('movie_detail', views.movie_detail, name='movie detail'),
]