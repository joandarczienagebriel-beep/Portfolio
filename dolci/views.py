from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='home_pg.html'

class AboutView(TemplateView):
    template_name='about_us_pg.html'

class ProductView(TemplateView):
    template_name='products_pg.html'

class ContactView(TemplateView):
    template_name='contact_pg.html'
# Create your views here.
