from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.signin_signup, name="login"),
    path("register/", views.sign_up, name="register"),
    path("logout/", views.sign_out, name="logout"),
    path("room/<str:pk>/", views.rooms, name="room"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<str:pk>", views.update_room, name="update-room"),
    path("delete-room/<str:pk>", views.delete_room, name="delete-room"),
    path("delete-message/<str:pk>", views.delete_message, name="delete-message"),
    path("profile/<str:pk>/", views.user_profile, name="user-profile"),
]
