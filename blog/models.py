from django.db import models
from django.contrib.auth.models import  User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=150)
     
    def __str__(self):
      
        return self.name
    
    
 
class posts(models.Model):
    
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg') 
    counted_views = models.IntegerField(default=0 )
    category=models.ManyToManyField(category)
    status = models.BooleanField(max_length=100, default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()
    updated_date = models.DateTimeField(auto_now=True)
    search_fields=['content','title']
    class meta:
        ordering=['-created_date']
    
           
    
    
    def __str__(self):
      
          return self.title

    def snippest(self):
        return self.content[:100] + "..."
    
    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.pid})
        #pass
    