from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='post-home'),
    path('posts/new', views.repairCreateView, name='post-create'),
    path('posts/delete/<int:id>/', views.repairDelete, name='post-delete'),
    path('posts/update/<int:id>/', views.repairUpdate, name='post-update'),
    path('register', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='repair/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='repair/registration/login.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('addprofile/<int:id>', views.addprof, name='addprofile'),
    # path('post/<slug:slug>/detail/', views.post_detail, name='post-detail'),
    path('posts/<slug:post>/', views.post_single, name='post_single'),
    path('posts/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('search',views.search, name='search'),
]    