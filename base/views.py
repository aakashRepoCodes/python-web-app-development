from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Room, Topic, User
from .forms import RoomForm

# Create your views here.

chatrooms = [
    {id: 1, "name": "Python Chatroom"},
    {id: 2, "name": "JavaScript Chatroom"},
    {id: 3, "name": "Ruby Chatroom"},
]


def home(request):
    queryParam = request.GET.get("q") if request.GET.get("q") != None else ""
    topics = Topic.objects.all()

    chatrooms = Room.objects.filter(
        Q(topic__name__icontains=queryParam)
        | Q(name__icontains=queryParam)
        | Q(description__icontains=queryParam)
    )

    room_count = chatrooms.count()

    return render(
        request,
        "base/home.html",
        {"rooms": chatrooms, "topics": topics, "room_count": room_count},
    )
    #    return HttpResponse('Home Page')


def rooms(request, pk):
    room = Room.objects.get(id=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)
    # return HttpResponse('Rooms')


def create_room(request):
    form = RoomForm()
    context = {"form": form}

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    return render(request, "base/room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
        return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == "POST":
        room.delete()
        return redirect("home")

    context = {"obj": room}

    return render(request, "base/delete_room.html", context)


def signin_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            print("no such user")

        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            print("Login sucesss...")
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password is incorrect !")
    return render(request, "base/signin_signup.html", {})


def sign_out(request):
    logout(request)
    return redirect("home")
