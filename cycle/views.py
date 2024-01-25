from django.shortcuts import render
from offer.models import Banner

def home(request):
    d = Banner.objects.all()
    return render(request,'index.html', {'data' : d})

def about(request):
    return render(request,'shopnow.html')    


def about(request):
    return render(request,'about.html')    

def contact(request):
    return render(request,'contact.html')

def cycle(request):
    return render(request,'cycle.html')    

def news(request):
    return render(request,'news.html')