from django.urls import path
from .views import products_list, create_product
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', products_list, name='products_list'),
    path('create', create_product, name='create_product'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
