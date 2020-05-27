from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("About Us Page")

def contact(request):
    return HttpResponse("Contact Us Page")

def tracker(request):
    return HttpResponse("Tracker Page")

def search(request):
    return HttpResponse("Search Page")

def productview(request):
    return HttpResponse("Product View  Page")

def checkout(request):
    return HttpResponse("checkout Page")

