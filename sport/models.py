from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField

#Like Model
class Like(models.Model):
    likies = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        ordering = ["-pk"]


#Dislike Model
class Dislike(models.Model):
    dislikes = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Dislike"
        verbose_name_plural = "Dislikes"
        ordering = ["-pk"]

#Love Model
class Love(models.Model):
    lovies = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = "Love"
        verbose_name_plural = "Loves"
        ordering = ["-pk"]
#Views Model
class Views(models.Model):
    viewes = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "View"
        verbose_name_plural = "Views"
        ordering = ["-pk"]
#Reply Model
class Seply(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    senton = models.DateTimeField(auto_now_add=True)
    commenties = models.ForeignKey('Somment', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name.user.username
#Somment Model
class Somment(models.Model):
    names = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(default="")
    time = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    replies = models.ForeignKey(Seply, on_delete=models.SET_NULL, null=True, blank=True, related_name="replyeis")
    post = models.ForeignKey('Sport' , to_field="slug", on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ["-pk"]
    
    def __str__(self):
        return self.names.username
    

#Draft Model or Save for later

#Category


#Sport Model
class Sport(models.Model):
    title = models.CharField(max_length=9999999)
    slug = models.SlugField(max_length=9999999, unique=True)
    #category = models.ForeignKey(Category, default="", to_field="category",on_delete=models.CASCADE)
    sommentie = models.ForeignKey(Somment, on_delete=models.SET_NULL, null=True, blank=True, related_name="commentes")
    headline = models.CharField(max_length=999999999999)
    content = RichTextField()
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)
    feature_image = models.FileField(upload_to="static/img/sport/", default="")
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(Like, blank=True, related_name="likes")
    dislike = models.ManyToManyField(Dislike, blank=True, related_name="dislike")
    love = models.ManyToManyField(Love, blank=True, related_name="love")
   
    class Meta:
        ordering = ["-pk"]

    
    
    
    

#Draft 
class ReadLaterSport(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(Sport, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.username

