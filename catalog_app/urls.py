from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('product_list', views.product_list, name='product list'),
    path('product_detail', views.product_detail, name='product detail'),
    path('register', views.register, name='register'),
    path('register2', views.register2, name='register2'),
    path('login', views.login, name='login'),
    path('login2', views.login2, name='login2'),

]