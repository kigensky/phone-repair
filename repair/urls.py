from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='repair-home'),
    path('cards/new', views.repairCreateView, name='repair-create'),
    
]    