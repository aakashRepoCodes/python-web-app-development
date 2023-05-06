from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

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


def create_room(request):
    form = RoomForm()
    context = {'form': form}

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'base/room_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance = room)

    if request.method == "POST":
        form = RoomForm(request.POST , instance=room )
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id = pk)

    if request.method == 'POST': 
        room.delete()
        return redirect('home')
         
    context = {'obj': room}

    return render(request, 'base/delete_room.html', context)