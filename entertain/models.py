from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField




#
#Eomment Model
class Eomment(models.Model):
    names = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(default="")
    time = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    post = models.ForeignKey('Entertain', on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ["-pk"]
    
    def __str__(self):
        return self.names.username
    

#Draft Model or Save for later

#Category
class EntertainCate(models.Model):
    category = models.CharField(max_length=500)
    
    class Meta:
        ordering = ["-pk"]
    
    def __str__(self):
        return self.category
    

#Entertain Model
class Entertain(models.Model):
    title = models.CharField(max_length=9999999)
    category = models.ForeignKey(EntertainCate,on_delete=models.CASCADE, default='')
    bommentie = models.ForeignKey(Eomment, on_delete=models.SET_NULL, null=True, blank=True, related_name="commentes")
    headline = models.CharField(max_length=999999999999)
    content = RichTextField()
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)
    #feature_image = models.FileField(upload_to="Entertain", default="")
    views = models.IntegerField(default=0)
    
    class Meta:
        ordering = ["-pk"]

    
    
    
    

#Draft 
class ReadLaterEntertain(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(Entertain, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.username

