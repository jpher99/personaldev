from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.items, name="item"),
    path('customer/<str:pk>/', views.customer, name="user"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('create_user/', views.create_user, name='create_user'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  # Add this line
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]