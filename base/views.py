from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Room, Topic, User, Message
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
    room_messages = room.message_set.all().order_by("-created")
    print(room_messages)
    context = {"room_messages": room_messages}

    if request.method == "POST":
        print(request.POST.get("body"))
        message = Message.objects.create(
            user=request.user, room=room, body=request.POST.get("body")
        )
        return redirect("room", pk=room.id)

    return render(request, "base/room.html", context)


@login_required(login_url="/login")
def create_room(request):
    form = RoomForm()
    context = {"form": form}

    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")
    return render(request, "base/room_form.html", context)


@login_required(login_url="/login")
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


@login_required(login_url="/login")
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == "POST":
        room.delete()
        return redirect("home")

    context = {"obj": room}

    return render(request, "base/delete_room.html", context)


def signin_signup(request):
    page = "login"
    context = {"page": page}
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
    return render(request, "base/signin_signup.html", context)


def sign_out(request):
    logout(request)
    return redirect("home")


def sign_up(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(user=user, request=request)
            return redirect("home")
        else:
            messages.error(request, "Error occured in registration...")

    context = {"form": form}
    return render(request, "base/signin_signup.html", context)
