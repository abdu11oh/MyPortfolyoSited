from django.views.generic import TemplateView

class Jaxa(TemplateView):
    template_name="index.html"

class Jaxan(TemplateView):
    template_name="about.html"

class Abdulloh(TemplateView):
    template_name="contact.html"

class Lenovo(TemplateView):
    template_name="courses.html"

class Hp(TemplateView):
    template_name="portfolio.html"

class Asus(TemplateView):
    template_name="pricing.html"