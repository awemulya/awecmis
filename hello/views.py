from django import http

def home(request):
    return http.HttpResponse('Hello World!')

def dashboard(request):
    return http.HttpResponse('Hello Dashboard')
