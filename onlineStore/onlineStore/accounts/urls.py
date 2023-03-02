from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='Customer Login'),
    path('register/', views.register, name='Customer sign-up'),
]
