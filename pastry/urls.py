from django.urls import path
from .views import HomeView, AboutView, ProductView

urlpatterns = [
    path('pastry/', HomeView.as_view(), name='home_pastry'),
    path('about/pg/', AboutView.as_view(), name='about_pg'),
    path('products/pg/', ProductView.as_view(), name='products_pg'),
]
