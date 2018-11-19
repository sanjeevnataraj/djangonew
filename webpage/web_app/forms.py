from django import forms
from django.contrib.auth.models import User
from web_app.models import Student_profile,Hobby_details
from django.forms import formset_factory

class SignUpForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class Register(forms.ModelForm):

    class Meta():
        model = Student_profile
        fields = ('PhoneNumber','qualification','subjects','percentage','Description','profile_pic')

class Hobbies(forms.ModelForm):

    class Meta():

        model = Hobby_details

        fields = ('hobby',)
