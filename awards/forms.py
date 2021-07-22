from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Projects, Comments


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['profile_pic', 'bio']


class  NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','project_id']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']