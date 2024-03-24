from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def contactus(request):
    template = loader.get_template('contactus.html')
    return HttpResponse(template.render())

def signin(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def destination(request):
    template = loader.get_template('destination.html')
    return HttpResponse(template.render())