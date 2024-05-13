from django.urls import path
from .views import products_list, create_product, update_product, delete_product
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', products_list, name='products_list'),
    path('create', create_product, name='create_product'),
    path('<int:pk>/update/', update_product, name='update_product'),
    path('<int:pk>/delete/', delete_product, name='delete_product'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
