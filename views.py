from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(request.META['REMOTE_ADDR'])
    return HttpResponse("<html>hello</html>")
def janakiraman(request): 
    return render(request,'hello.html',{'name':'janakiraman'})
def form(request):
    return render(request,'form.html')
def thank(request):
    message = request.GET['name']
    return render(request,'hello.html',{'name':message})
