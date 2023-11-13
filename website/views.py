from django.http import HttpResponse



def index_view(request):
    return HttpResponse('<h1>this is Home<h1>')

def about_view(request):
    return HttpResponse('<h1>this is about <h1>')

def contact_view(request):
    return HttpResponse('<h1>about contact<h1>')
