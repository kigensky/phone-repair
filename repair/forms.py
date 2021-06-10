from .models import Comment, Post, Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','contact','bio']


class RepairForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','description','Operating_System']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)      