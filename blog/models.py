from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
#from tinymce.models import HTMLField

#Like Model

#Reply Model
#class Beply(models.Model):
    #name = models.ForeignKey(User, on_delete=models.CASCADE)
    #content = models.TextField()
    #senton = models.DateTimeField(auto_now_add=True)
    #commenties = models.ForeignKey('Bomment', on_delete=models.CASCADE, null=True)
    
    #def __str__(self):
        #return self.name.user.username
#Blog Database
class Blog(models.Model):
     bmaster = models.ForeignKey(User,   related_name = "postauthor", on_delete = models.CASCADE)
     btitle = models.CharField(max_length = 255)
     descr = models.CharField(max_length = 1000)
     #bpic = models.FileField(upload_to = "static/img/blogpic/")
     #category = models.ForeignKey(Category,  related_name = "postcategory", on_delete = models.CASCADE)
     bpost = RichTextField()
     views = models.IntegerField(default = 0)
     heart = models.ManyToManyField(User, related_name = "postlovie", blank = True)
     likes = models.ManyToManyField(User, related_name = "postlikie", blank = True)
     hate = models.ManyToManyField(User, related_name = "posthatie", blank = True)
     created = models.DateTimeField(auto_now_add = True)
     
     class Meta:
          ordering = ['-created']
     
     def __str__(self):
          return self.btitle

class Comment(models.Model):
     cmaster = models.ForeignKey(User, on_delete = models.CASCADE, related_name="cmaster")
     post = models.ForeignKey(Blog, on_delete = models.CASCADE)
     comments = models.TextField()
     likes = models.ManyToManyField(User, related_name = "commentlikes", blank = True)
     love = models.ManyToManyField(User, related_name = "commentlovie", blank = True)
     hate = models.ManyToManyField(User, related_name = "commenthatie", blank = True)
     created = models.DateTimeField(auto_now_add = True)
     
     class Meta:
          ordering = ["-created"]
     
     def __str__(self):
          return self.cmaster.username
          
#Draft 
class ReadLaterBlog(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.username

