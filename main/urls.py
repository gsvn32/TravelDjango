from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about', views.about, name='about'),
    path('contactus', views.contactus, name='contactus'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('destination', views.destination, name='destination'),
]