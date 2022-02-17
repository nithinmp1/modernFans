from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

def index(request):
    category = Products.objects.all()
    data = {'products' : category}
    return render(request,'index.html',data)
# Create your views here.

def about(request):
    category = Products.objects.all()
    data = {'Products' : category}
    return render(request,'about.html',data)

def contact(request):
    category = Products.objects.all()
    data = {'Products' : category}
    return render(request,'contact.html',data)

def product(request,cat_id):
    category = Products.objects.filter(id=cat_id)

    data = {'products':product}
    return render(request,'product.html',data)
