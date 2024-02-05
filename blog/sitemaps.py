from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from blog.models import posts
from django.urls import reverse



class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return posts.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self,item):
       return reverse('blog:single', kwargs={'pid': item.pid})    
        
             
       