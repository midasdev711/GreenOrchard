from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse("This is the expenses index")

def summary(request):
    return render(request, 'expenses/dummy.html')
    # return render(request, 'expenses/summary.html')

def month(request):
    # return render(request, 'expenses/dummy.html')
    return render(request, 'expenses/month.html')
    # return HttpResponse("This is the month part")

def category(request):
    return render(request, 'expenses/dummy.html')
    # return render(request, 'expenses/category.html')

def faq(request):
    # return HttpResponse("This is the faq part")
    # return render(request, 'expenses/dummy.html')
    return render(request, 'expenses/faq.html')

def login(request):
    return render(request, 'expenses/dummy.html')
    # return render(request, 'expenses/login.html')

def register(request):
    return render(request, 'expenses/dummy.html')
    # return render(request, 'expenses/register.html')
