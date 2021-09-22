from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfoEdge

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoEdge
        fields = ('porfolio_site', 'profile_pic')