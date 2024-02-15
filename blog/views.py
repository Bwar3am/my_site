from django.shortcuts import render,HttpResponse,get_object_or_404 , redirect
from blog.models import posts,category,comment 
from django.utils import timezone
from django.views.generic import DetailView
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect



def blog_view(request,**kwargs):
    Post=posts.objects.filter(status=1,published_date__lte=timezone.now()).order_by('published_date')
    if kwargs.get('cat_name') != None:
       Post=Post.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        Post=Post.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name'):
        Post=Post.filter(tags__name__in=kwargs['tag_name'])
        
        
    
    Post=Paginator(Post,3)
    try:    
       page_number=request.GET.get('page')
       Post=Post.get_page(page_number) 
      
    except PageNotAnInteger :
        Post=Post.get_page(1)
        
    except EmptyPage :
        Post=Post.get_page(1)
               
         
    context = {"Post":Post}
    return render(request,"blog-home.html",context)
    
        
def blog_single(request,pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS , 'youre ticket has been submited successfully')
        else:
            messages.add_message(request,messages.ERROR , 'error please try again')
    
        
       
    Post=get_object_or_404(posts,id=pid) 
    next_post=posts.objects.filter(status=1,id__gt=pid,published_date__lte=timezone.now()).order_by('id','published_date').first()
    pre_post=posts.objects.filter(status=1,id__gt=pid,published_date__lte=timezone.now()).order_by('id','published_date').first() 
    if not Post.login_required:
        comments=comment.objects.filter(post=Post.id,approach=True)
        form = CommentForm()
        context = {"Post":Post,"next_post":next_post,"pre_post":pre_post , "comments":comments , "form":form}
    else:
        return HttpResponseRedirect(reverse('accounts:login'))   
    Post.counted_views += 1
    Post.save()
    if Post.published_date <=timezone.now() and Post.status == 1:
        return render(request,"blog-single.html",context)
    else:
        return HttpResponse(" this post is not ready to be realeased yet")
    
def test(request):
    return render(request,'test.html')

def blog_category(request,cat_name):
    Post=posts.objects.filter(status=1)
    Post=Post.filter(category__name=cat_name)
    context={"Post":Post}
    return render(request,"blog-home.html",context)  

def blog_search(request):
    Post=posts.objects.filter(status=1)
    if request.method=="GET":
        
       if s := request.GET.get('s'):
           Post=Post.filter(content__contains=s)
    
    
    context={"Post":Post}
    return render(request,"blog-home.html",context)
    
      
         
                                           
 

       


   
  
