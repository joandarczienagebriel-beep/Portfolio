from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='home.html'

class AboutView(TemplateView):
    template_name='about us.html'

class ProductView(TemplateView):
    template_name='products.html'
# Create your views here.
