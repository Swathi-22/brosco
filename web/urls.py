from unicodedata import name
from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('gallery/', views.gallery,name='gallery'),
    path('update/', views.update,name='update'),
    path('contact/',views.contact,name='contact')
]