from django.urls import path, include
from . import views
from django.urls import re_path

app_name = "chat"

urlpatterns = [
    path("dashboard", views.index, name="dashboard"),
    path("addfriend/<str:name>", views.addFriend, name="addFriend"),
    path("chat/<str:username>", views.chat, name="chat"),
    path('waiting-room', views.waiting_room, name="waiting-room"),
    path('api/room', views.room, name='room'),

]