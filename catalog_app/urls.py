from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('register_account', views.register_account, name='register_account'),
    path('transfer', views.transfer, name='transfer'),

]