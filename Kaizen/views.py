from django.http import HttpResponse
from django.shortcuts import render

def Homepage(request):
    # return HttpResponse('Welcome To Kaizen Website')
    return render(request, 'Homepage.html')

def Login(request):
    # return HttpResponse('Login Page')
    return render(request, 'Login.html')

def Register(request):
    # return HttpResponse('Registration Page')
    return render(request, 'Registration.html')

def About(request):
    # return HttpResponse('About Us')
    return render(request, 'About.html')