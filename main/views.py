from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from django.views import View
from django.db.models import Q
from .models import Destination
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.contrib import messages
from django.contrib.auth.models import User


def main(request):
    """
    Handle GET request to render the index page.
    """
    if request.method == 'GET':
        return render(request, 'index.html', context={})
    # Optionally handle other HTTP methods or return a 405 Method Not Allowed response
    return HttpResponseNotAllowed(['GET'])

def about(request):
    """
    Handle GET request to render the about page.
    """
    if request.method == 'GET':
        return render(request, 'about.html', context={})
    # Optionally handle other HTTP methods or return a 405 Method Not Allowed response
    return HttpResponseNotAllowed(['GET'])


def contactus(request):
    """
    Handle GET request to render the contactus page.
    """
    if request.method == 'GET':
        return render(request, 'contactus.html', context={})
    # Optionally handle other HTTP methods or return a 405 Method Not Allowed response
    return HttpResponseNotAllowed(['GET'])

    
def destination(request):
    """
    Handle GET request to render the destination page.
    """
    if request.method == 'GET':
        return render(request, 'destination.html', context={})
    # Optionally handle other HTTP methods or return a 405 Method Not Allowed response
    return HttpResponseNotAllowed(['GET'])


def SearchView(request):
    """
    Handle POST request to render the search results page.
    """
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        travel_date = request.POST.get('travel_date')
        return_date = request.POST.get('return_date')
        print(destination)
        # Query the database for matching destinations
        destinations = Destination.objects.filter(
            Q(name__icontains=destination)
        )

        # Render the results
        return render(request, 'search.html', context={
            'destinations': destinations,
            'source': source,
            'destination': destination,
            'travel_date': travel_date,
            'return_date': return_date,
        })

def SigninView(request):
    """
    Handle POST request to render the sign in page.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)

            # Redirect to a success page, e.g., home page
            return redirect('/')  # Replace 'home' with your actual URL name
        else:
            # Return an invalid login error message
            messages.error(request, 'Invalid email or password.')
            return render(request, 'signin.html')
    if request.method == 'GET':
        # For GET requests (initial render of the form)
        return render(request, 'signin.html',context={})
    
def SignUpView(request):
    """
    Handle POST request to render the sign up page.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        fullname = request.POST.get('fullname')
        if User.objects.filter(username=email).exists():
            # Return an user already exists error message
            messages.error(request, 'user already exists ')
            return render(request, 'signup.html')
        else:
            # Create a new user
            user = User.objects.create_user(username=email, email=email, first_name=fullname)
            user.set_password(password)
            user.save()
            # Redirect to a success page, e.g., home page
            return redirect('signin')  # Replace 'home' with your actual URL name
    if request.method == 'GET':
        # For GET requests (initial render of the form)
        return render(request, 'signup.html',context={})
    

def logoutView(request):
    if request.method == 'GET':
        # For GET requests (initial render of the form)
        
        logout(request)
        return render(request, 'index.html',context={})