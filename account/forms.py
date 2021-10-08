from account.models import Profile
from django import forms
from django.contrib.auth.models import User
from django_countries.widgets import CountrySelectWidget

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =  ("fname","lname","profilepic", "dateofbirth","phone", "bio","origin","fb","bird", "gram","gb", "linkin")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)

class ContactForm (forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50 )
    email_address = forms.EmailField(max_length = 150 )
    message = forms.CharField(widget = forms.Textarea, max_length = 2000 )
    