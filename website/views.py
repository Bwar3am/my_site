from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from website.models import Contact
from website.forms import  ContactForm , NewsletterForm
from django.contrib import messages
 


def index_view(request):
    return render(request,'index.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.fields['subject'].required = False
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS , 'youre ticket has been submited successfully')  
        else:
            messages.add_message(request,messages.ERROR , 'error , please try again')
             
            
           

    form = ContactForm()         
    return render(request,'contact.html',{'form':form})


def Newsletter_view(request):
    if request.method == 'POST':
        form= NewsletterForm(request.POST)
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect("/")
        else:    
            return HttpResponseRedirect("/")
    form = NewsletterForm() 

def test_view(request):
       if request.method == 'POST':
           form = ContactForm(request.POST)
           if form.is_valid():
               form.save()      
               return HttpResponse("Successfully")
           else:
               return HttpResponse("Error")
       form = ContactForm()
       return render (request,'test.html',{'form':form})
   
   
 
    
            
           
  
    
    
    
#messages.add_message(request,messages.SUCCESS , 'youre ticket has been submited successfully')
#messages.add_message(request,messages.ERROR , 'youre ticket hasnt been submited successfully')
#messages.success(request,'message is invalid') 