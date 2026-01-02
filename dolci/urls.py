from django.urls import path
from .views import HomeView, AboutView, ProductView, ContactView

urlpatterns = [
    path('pastry/', HomeView.as_view(), name='home_pg'),
    path('about/', AboutView.as_view(), name='about_pg'),
    path('products/', ProductView.as_view(), name='products_pg'),
    path('contact/', ContactView.as_view(), name='contact_pg'),
]
