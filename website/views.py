from django.http import HttpResponse,JsonResponse
from django.shortcuts import render



def index_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')

def test_view(request):
    context = {'name':'Barsam','lastname':'Hassazadeh-aski'}
    return render(request,'test.html',context)
