from django.urls import path
from . import views

app_name    = "bbs"
urlpatterns = [ 
    path('', views.index, name="index"),
    path('chat/', views.chat, name="chat"),
    path('chat_message/<int:pk>/', views.chat_message, name="chat_message"),
]

