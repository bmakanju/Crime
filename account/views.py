from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import generic
from django.core.mail import send_mail, BadHeaderError
from django.contrib import auth
from django.contrib.auth.forms import PasswordChangeForm
from subscribers.models import NewsLetter
from django.http import HttpResponse
import random

#Card Profile 
def ProfileCard(request):
    return render(request, "DevCard.htm")

#Contavt Us form
def Contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            email = request.user.email
            message = request.POST.get("message")
            subject = "Message From CrimeHeist Contact us Form"
            try:
                send_mail(subject, message, email, ["CrimeHeist@gmail.com"], fail_silently=False)
                return HttpResponse("Your Message Have been sent over to CrimeHeist we get back to you as soon as possible.Thank You for been patient")
            except BadHeaderError:
                return HttpResponse("Invalid Response")
        else:
            email = request.POST.get("email")
            message = request.POST.get("message")
            subject = "Message From Crimeheist Contact us Form"
            try:
                send_mail(subject, message, email, ["Crimeheist@gmail.com"], fail_silently=True)
                return HttpResponse("Your Message Have been sent over to CrimeHeist we get back to you as soon as possible.Thank You for been patient")
            except BadHeaderError:
                return HttpResponse("Invalid Response")
                
        #form = ContactForm(request.POST)
        #if form.is_valid():
            #email=form.cleaned_data['email_address']
            #subject = "Website Inquiry"
         #   body = {
              #  'first_name' : form.cleaned_data['first_name'],
         #       'last_name' : form.cleaned_data[ 'last_name'],
             #   'email' : form.cleaned_data['email_address'],
            #    'message' :form.cleaned_data['message'],
          #  }
        #    message = "\n".join(body.values())
    else:
        form = ContactForm()
        context = {
            "form":form
        }
        return render(request, "Contact.htm", context)


#About Us Page
class About(generic.TemplateView):
	template_name = "About.htm"


#Settung 
def Settings(request):
    form = PasswordChangeForm(request.user)
    context = {
        "form":form
    }
    return render(request, "Setting/Settings.htm", context)

#Viewing other Profile 
def ViewOtherProfile(request, name):
    profile = User.objects.get(username=name)
    
    context = {
        "profile":profile
    }
    return render(request, "Profile/ViewOtherProfile.htm", context)
    
    
    

#Chamging Of Password
def PasswordUpdate(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:login")
        else:
            form = PasswordChangeForm(request.user)
            context = {
                "error":"New Password was not saved Try again",
                "form":form
            }
            return render(request, "Account/ChangePass.htm", context)
    #else:
       # form = PasswordChangeForm(request.user)
#context = {
       #     "form":form
      #  }
        #return render(request, "Account/ChangePass.htm", context)

#Profile updated
def UpdateProfile(request):
    if request.method == "POST" or request.method == "FILES":
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            userform = UserForm(instance=request.user)
            profileform = ProfileForm(instance=request.user.profile)
            context = {
                "Success":"Profile Updated Successfully",
                "userform":userform,
                "profileform":profileform
                
            }
            return render(request, "Account/AccountUpdate.htm", context)
        else:
            userform = UserForm(instance=request.user)
            profileform = ProfileForm(instance=request.user.profile)
            context = {
                "Error":"Profile Update Failed Try again ",
                "userform":userform,
                "profileform":profileform
                
            }
            return render(request, "Account/AccountUpdate.htm", context)
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=request.user.profile)
        context = {
            "userform":userform,
            "profileform":profileform
        }
        return render(request, "Account/AccountUpdate.htm", context)


#L9gout ©©©
def Logout(request):
    auth.logout(request)
    return redirect('account:login')	

#Login View
def Logging(request):
    if request.user.is_authenticated:
        return redirect('sport:sport')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credatials")
            return render(request, "Account/Login.htm")
    else:
        return render(request, "Account/Login.htm")



#Registration view
def Register(request):
    if request.user.is_authenticated:
        return redirect('sport:sport')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username Exists Already")
            return render(request, "Account/Register.htm")	
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email Exists Already")
            return render(request, "Account/Register.htm")
        else:
            success = User.objects.create_user(
                username,
                email,
                password
            )
            success.save()
            newsletter = NewsLetter.objects.create(email=email)
            newsletter.save()
            subject = "Signed Up on CrimeHeist"
            message = "Thank you for signing up with CrimeHeist. Enjoy all the service we provide and promise you the best.   Note:By Signing up with us you are automatically added to our newsletter to unsubscribe kindly login onto CrimeHeist and check the settings and click on the Unsubscribe button "
            from_user = "CrimeHeist@gmail.com"
            receiving_user = email
            send_mail(subject, message, from_user, [receiving_user], fail_silently=False,)
            return redirect('account:login')
    else:
        return render(request, "Account/Register.htm")









