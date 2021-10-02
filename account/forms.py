from account.models import Profile
from django import forms
from django.contrib.auth.models import User
from django_countries.widgets import CountrySelectWidget

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ("fname","lname","profilepic", "dateofbirth","phone", "bio")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)

