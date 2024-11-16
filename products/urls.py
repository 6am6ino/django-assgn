from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('', views.index, name='index'),  # Maps root URL to index view
    path('about/', views.about, name='about'),  # Maps /about/ URL to about view
]