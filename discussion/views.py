from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import DiscussionRoomForm, MessageForm
from .model import DiscussionRoom, Message


@login_required
def create_room_view(request):
    if request.method == 'POST':
        form = DiscussionRoomForm(request.POST)
        if form.is_valid():
            # Associate the room with the current user
            room = form.save(commit=False)
            room.user = request.user  # Set the user_id field
            room.save()
            return redirect('home')
    else:
        form = DiscussionRoomForm()
    return render(request, 'discussion_rooms/create_room.html', {'form': form})


@login_required
def discussion_room(request, room_id):
    # Retrieve the discussion room object using room_id
    room = get_object_or_404(DiscussionRoom, id=room_id)

    # Retrieve all messages associated with the discussion room
    messages = Message.objects.filter(discussion_room=room)

    # Handle message submission
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.discussion_room = room
            message.save()
            # Redirect to the same discussion room page after message submission
            return redirect('discussion_room', room_id=room_id)
    else:
        form = MessageForm()

    # Render the discussion room template with discussion room details and messages
    return render(request, 'discussion_rooms/discussion_room.html', {'room': room, 'messages': messages, 'form': form})


@login_required
def post_message_view(request, room_id):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.discussion_room_id = room_id
            message.save()
            return redirect('discussion_room', room_id=room_id)
    else:
        form = MessageForm()
    return render(request, 'discussion_rooms/post_message.html', {'form': form})

@login_required
def home(request):

    if request.method == 'POST':
        # Process the discussion room creation form
        form = DiscussionRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after creating the room
        else:
            error_message = "Please correct the errors below."
    else:
        # Display the discussion room creation form
        form = DiscussionRoomForm()

    rooms = DiscussionRoom.objects.all()

    # Render the home.html template and include the discussion room creation for_messagem and existing rooms
    return render(request, 'home.html', {'rooms': rooms, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user object returned by form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            return redirect(user_login)
            #login(request, user)
            #return redirect('home')  # Redirect to home page after successful registration and login
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

  
def search_rooms(request):
    query = request.GET.get('q')
    if query:
        rooms = DiscussionRoom.objects.filter(name__icontains=query)
    else:
        rooms = DiscussionRoom.objects.all()
    return render(request, 'discussion_rooms/search.html', {'query': query, 'rooms': rooms})

def delete_room(request, room_id):
    room = get_object_or_404(DiscussionRoom, id=room_id)
    if room.user == request.user:
        room.delete()
        return redirect("home")
    else:
        return HttpResponse("You are not autherized to delete this room.")
