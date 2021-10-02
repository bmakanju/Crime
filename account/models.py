from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.


class Profile(models.Model):
     user = models.OneToOneField(User,   on_delete = models.CASCADE)
     fname = models.CharField(max_length = 500, blank=True)
     lname = models.CharField(max_length = 500, blank=True)
     profilepic = models.FileField(upload_to = "static/img/profile/pic/", default = "static/img/profile/pic/profile.png")
     dateofbirth = models.DateField(null = True, blank=True)
     phone = models.IntegerField(blank = True, null =True)
     bio = models.TextField(default = "Welcome to CrimeHeist")
     fb = models.CharField(blank=True,max_length=500)
     origin = CountryField(blank=True)
     bird = models.CharField(max_length=500,blank=True, default="Not on Twitter yet")
     gram = models.CharField(max_length=500,blank=True, default="Not on Instagram yet")
     gb = models.CharField(max_length=500, blank=True, default="Not on Google +")
     linkin = models.CharField(max_length=500,blank=True, default="Not on LinkedIn Yet")
     @receiver(post_save, sender = User)
     def create_user_profile(sender, instance, created, **kwargs):
          if created:
               Profile.objects.create(user = instance)
     
     @receiver(post_save, sender = User)
     def save_user_profile(sender, instance, **kwargs):
          instance.profile.save()





