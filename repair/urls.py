from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='repair-home'),
    path('repairs/new', views.repairCreateView, name='repair-create'),
    path('repairs/delete/<int:id>/', views.repairDelete, name='repair-delete'),
    path('repairs/update/<int:id>/', views.repairUpdate, name='repair-update'),
    path('register', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='repair/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='repair/registration/login.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('addprofile/<int:id>', views.addprof, name='addprofile'),
    
]    