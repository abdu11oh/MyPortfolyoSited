from django.urls import path
from .views import Abdulloh, Asus, Hp, Jaxa, Jaxan, Lenovo

urlpatterns=[
    path('', Jaxa.as_view(),name="home"),
    path('about/', Jaxan.as_view(), name="about"),
    path('contact/', Abdulloh.as_view(), name="contact"),
    path('courses/', Lenovo.as_view(), name="courses"),
    path('portfolio/', Hp.as_view(), name="portfolio"),
    path("pricing/", Asus.as_view(), name="pricing")
 
]