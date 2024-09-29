from django.urls import path
from . import views
app_name='contact'
urlpatterns = [
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('our-services/',views.ourservices,name='services'),
    path('',views.home,name='home'),
]
