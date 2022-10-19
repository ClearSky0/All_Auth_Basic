from django.shortcuts import render

# Create your views here.

def index(request, option='Home'):
    """The home page for Your Site"""
    page_title = option
    return render(request, "index.html", {'page_title': page_title} )