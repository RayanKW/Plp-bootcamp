from django.urls import path
from . import views

urlpatterns = [
    path('', views.house_listings, name='Home'),
]
