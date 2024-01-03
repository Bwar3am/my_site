from django.db import models

# Create your models here.
 
class posts(models.Model):
      # image =
    # author = 
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tags = 
    # category = 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    search_fields=['content','title']
    class meta:
        ordering=['-created_date']
            
    
    
    def __str__(self):
      
          return self.title

