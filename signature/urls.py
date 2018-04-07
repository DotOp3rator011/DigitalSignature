from django.urls import path
from . import views

app_name = "signature"

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('signature', views.signature, name='signature'),
    path('identify', views.identify, name='identify'),
]
