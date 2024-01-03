from django.shortcuts import render,get_object_or_404
from blog.models import posts

# Create your views here.
def blog_view(request):
     Post=posts.objects.filter(status=1)
     context = {"Post":Post}
     return render(request,"blog-home.html",context)
def blog_single(request):
    return render(request,"blog-single.html")
def test(request,pid):
    Post=posts.objects.get(id=pid)
    context = {"Post":Post}
    return render(request,'test.html',context)
    
