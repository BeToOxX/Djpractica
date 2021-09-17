from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    allpet = pet.objects.all()
    return render(request, 'index.html', {'allpet':allpet})

def about(request):
    return render(request, 'about .html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')