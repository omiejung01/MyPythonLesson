from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('register_account', views.register_account, name='register_account'),
    path('transfer', views.transfer, name='transfer'),
    path('check_balance', views.check_balance, name='check_balance'),
    path('transfer_list', views.transfer_list, name='transfer_list'),
]