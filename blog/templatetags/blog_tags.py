from django import template
from blog.models import posts
from blog.models import category
register=template.Library()


@register.simple_tag(name= "plusino" )
def function():
    Post=posts.objects.filter(status=1).count()
    return Post
@register.simple_tag(name= "posts" )
def function():
    Post=posts.objects.filter(status=1)
    return Post

@register.filter
def snippet (value , arg:20):
    return value[:arg] + "...."

@register.inclusion_tag('blog-popular-post.html')
def latestposts(arg=4):
    Post=posts.objects.filter(status=1).order_by('published_date')[:arg]
    return {'Post':Post}
@register.inclusion_tag('blog-post-category.html')
def postscategories():
    Post=posts.objects.filter(status=1)
    Categories=category.objects.all()
    cate_dict={}
    for name in Categories:
      cate_dict[name]=Post.filter(category=name).count()
    return {'Categories':cate_dict}  
@register.inclusion_tag('recent-blog.html')
def recentblog(arg=6):
    Post=posts.objects.filter(status=1).order_by('published_date')[:arg]
    return {'Post':Post}    
    
     