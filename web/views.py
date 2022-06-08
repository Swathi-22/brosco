from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context ={
        'is_index':True
    }
    return render(request,'web/index.html',context)


def about(request):
    context ={
        'is_about':True
    }
    return render(request,'web/about.html',context)


def services(request):
    context ={
        'is_services':True
    }
    return render(request,'web/services.html',context)


def gallery(request):
    context ={
        'is_gallery':True
    }
    return render(request,'web/gallery.html',context)


def update(request):
    context ={
        'is_update':True
    }
    return render(request,'web/update.html',context)


def contact(request):
    context = {
        'is_contact':True
    }
    return render(request,'web/contact.html',context)


def construction(request):
    context = {
    
    }
    return render(request,'web/under-construction.html',context)