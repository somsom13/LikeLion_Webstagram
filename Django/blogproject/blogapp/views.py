from django.shortcuts import render
from .models import blog

# Create your views here.
def home(request):
    content=blog.objects
    return render(request,'home.html',{'content':content})

def detail(request,pk):
    content=blog.objects.get(pk=pk)
    return render(request,'detail.html',{'content':content})