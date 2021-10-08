from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField

#Like Model
class Like(models.Model):
    likies = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        ordering = ["-pk"]


#Dislike Model
class Dislike(models.Model):
    dislikes = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = "Dislike"
        verbose_name_plural = "Dislikes"
        ordering = ["-pk"]

#Love Model
class Love(models.Model):
    lovies = models.IntegerField(default=0)
    
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
class Reply(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField()
    senton = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name.username
#Comment Model
class Comment(models.Model):
    name = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default="")
    commentes = models.TextField(default="")
    time = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    replies = models.ForeignKey(Reply, on_delete=models.SET_NULL, null=True, blank=True, related_name="replyes")
    post = models.ForeignKey('News' , to_field="slug", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name.username
    

#Draft Model or Save for later

#Category
class CrimeCategory(models.Model):
    category = models.CharField(max_length=250)
    
    def __str__(self):
        return self.category


#News Model
class News(models.Model):
    title = models.CharField(max_length=9999999)
    slug = models.SlugField(max_length=9999999, unique=True)
    category = models.ForeignKey(CrimeCategory, default="", on_delete=models.CASCADE, blank=True)
    commentds = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, blank=True, related_name="comment")
    headline = models.CharField(max_length=999999999999)
    content = RichTextField()
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)
    #feature_image = models.FileField(upload_to="static/img/news/", default="")
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(Like, blank=True, related_name="likes")
    dislike = models.ManyToManyField(Dislike, blank=True, related_name="dislike")
    love = models.ManyToManyField(Love, blank=True, related_name="love")
   
    class Meta:
        ordering = ["-pk"]

    
    
    
    

#Draft 
class ReadLater(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.username

