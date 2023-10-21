from django.http import HttpResponse
from django.shortcuts import render


def Homepage(request):
    # return HttpResponse('Welcome To Kaizen Application')
    return render(request, 'Homepage.html')


def LandingPage(request):
    # return HttpResponse('Welcome To Kaizen Application')
     return render(request, 'Landingpage.html')


def About(request):
    # return HttpResponse('Welcome To Kaizen Application')
     return render(request, 'About.html')

