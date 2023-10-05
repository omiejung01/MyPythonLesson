from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('movie_list', views.movie_list, name='movie list'),
    path('movie_detail', views.movie_detail, name='movie detail'),
]