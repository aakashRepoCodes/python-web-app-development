from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

rooms = [
    {id:1, "name": 'Python Chatroom'},
    {id:1, "name": 'JavaScript Chatroom'}, 
    {id:1, "name": 'Ruby Chatroom'}, 
    {id:1, "name": 'Java Chatroom'},
]

def home(request):
    return render(request=request, template_name="base/home.html")
    #return HttpResponse('Home Page')


def rooms(request):
    return render(request, "base/room.html")
    #return HttpResponse('Rooms')