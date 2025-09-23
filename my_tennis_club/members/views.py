from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Hello world!")

def about_page_view(request):
    return render(request, "about.html")

