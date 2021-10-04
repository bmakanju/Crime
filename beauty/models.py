from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField




#
#Bomment Model
class Bomment(models.Model):
    names = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(default="")
    time = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
   
    post = models.ForeignKey('Beauty' , to_field="slug", on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ["-pk"]
    
    def __str__(self):
        return self.names.username
    

#Draft Model or Save for later

#Category


#Beauty Model
class Beauty(models.Model):
    title = models.CharField(max_length=9999999)
    slug = models.SlugField(max_length=9999999, unique=True)
    #category = models.ForeignKey(Category, default="", to_field="category",on_delete=models.CASCADE)
    bommentie = models.ForeignKey(Bomment, on_delete=models.SET_NULL, null=True, blank=True, related_name="commentes")
    headline = models.CharField(max_length=999999999999)
    content = RichTextField()
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)
    feature_image = models.FileField(upload_to="static/img/sport/", default="")
    views = models.IntegerField(default=0)
    
    class Meta:
        ordering = ["-pk"]

    
    
    
    

#Draft 
class ReadLaterBeauty(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(Beauty, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.username

