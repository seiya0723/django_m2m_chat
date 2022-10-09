from django import forms
from .models import Topic, Chat

class TopicForm(forms.ModelForm):

    class Meta:
        model   = Topic
        fields  = [ "comment","user" ]



class ChatForm(forms.ModelForm):

    class Meta:
        model   = Chat
        fields  = [ "group","user","message" ]




