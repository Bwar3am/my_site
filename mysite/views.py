from django.http import HttpResponse
from django.http import JsonResponse
def http_test(request):
    return HttpResponse('hello')
def json_test(request):
    return JsonResponse({"name":"ali"})