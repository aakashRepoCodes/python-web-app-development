from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request=request, template_name="home.html")
    #return HttpResponse('Home Page')


def rooms(request):
    return render(request, "room.html")
    #return HttpResponse('Rooms')