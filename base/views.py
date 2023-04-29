from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

rooms = [
    {id:1, "name": 'Python Chatroom'},
    {id:2, "name": 'JavaScript Chatroom'}, 
    {id:3, "name": 'Ruby Chatroom'}, 
    {id:4, "name": 'Java Chatroom'},
]

def home(request):
    return render(request,"base/home.html",{'chatrooms' : rooms})
    #return HttpResponse('Home Page')


def rooms(request):
    return render(request, "base/room.html")
    #return HttpResponse('Rooms')