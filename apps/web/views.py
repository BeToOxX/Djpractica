from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    allpet = pet.objects.all()
    return render(request, 'index.html', {'allpet':allpet})
