from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('health', views.health_check, name='health-check'),
    path('users', views.get_users, name='get-users'),
    path('products', views.get_products, name='get-products'),
]