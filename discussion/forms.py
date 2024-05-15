from django import forms
from django.contrib.auth.forms import UserCreationForm
from .model import DiscussionRoom, Message

#class CustomUserCreationForm(UserCreationForm):


class DiscussionRoomForm(forms.ModelForm):
    class Meta:
        model = DiscussionRoom
        fields = ('name', 'description')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content',)
