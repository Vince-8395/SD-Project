from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('About/', views.About),
    path('LandingPage/', views.LandingPage),
    path('', views.Homepage)
]
