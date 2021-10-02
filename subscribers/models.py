from django.db import models

# Create your models here.

#NewsLetter
class NewsLetter(models.Model):
    email = models.EmailField()
    
    class Meta:
        ordering = ["-pk"]
        
    def __str__(self):
        return self.email
