from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_management.models import UserProfile

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = [ 'email', 'name','password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ['name', 'email']


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']