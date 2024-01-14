from django.shortcuts import render,HttpResponse,get_object_or_404
from blog.models import posts
from django.utils import timezone
from django.views.generic import DetailView

# Create your views here.
def blog_view(request):
    Post=posts.objects.filter(status=1,published_date__lte=timezone.now()).order_by('published_date')
    context = {"Post":Post}
    return render(request,"blog-home.html",context)
    
        
def blog_single(request,pid):
    Post=get_object_or_404(posts,id=pid) 
    next_post=posts.objects.filter(status=1,id__gt=pid).order_by('id').first()
    pre_post=posts.objects.filter(status=1,id__lt=pid).order_by('-id').first()     
    context = {"Post":Post,"next_post":next_post,"pre_post":pre_post}
    Post.counted_views += 1
    Post.save()
    if Post.published_date <=timezone.now() and Post.status == 1:
        return render(request,"blog-single.html",context)
    else:
        return HttpResponse(" this post is not ready to be realeased yet")
    
def test(request,pid):
    Post=posts.objects.filter(status=1)
    Posts=get_object_or_404(Post,pk=pid)
    context = {"Post":Post}
    return render(request,'test.html',context)


    
         
#Post=posts.objects.get(id=pid)        
 #next_post=posts.objects.filter(id__gt=pid).order_by('id').first()
#    pre_post=posts.objects.filter(id__lt=pid).order_by('-id').first()                                            
 

       


   
  
