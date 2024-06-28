from django.urls import path
from . import views
from .views import SearchView, SigninView
urlpatterns = [
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('contactus', views.contactus, name='contactus'),
    path('signin', SigninView, name='signin'),
    path('signup', SigninView, name='signup'),
    path('destination', views.destination, name='destination'),
   path('search/', SearchView, name='search'),
]