from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

# Create your views here.

chatrooms = [
    {id:1, 'name': 'Python Chatroom'},
    {id:2, 'name': 'JavaScript Chatroom'}, 
    {id:3, 'name': 'Ruby Chatroom'}, 
]


def home(request):
    chatrooms = Room.objects.all
    return render(request,"base/home.html",{'rooms': chatrooms})
    #return HttpResponse('Home Page')


def rooms(request, pk):
    room = Room.objects.get(id = pk)
    context = {'room': room}
    return render(request, "base/room.html", context)
    #return HttpResponse('Rooms')