# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import Conversation

@login_required
def inbox(request):
    user = request.user

    # Obtener una lista de usuarios con los que el usuario ha intercambiado mensajes
    conversations = User.objects.filter(
        Q(sent_messages__recipient=user) | Q(received_messages__sender=user)
    ).distinct()

    context = {
        'conversations': conversations
    }
    return render(request, 'messages_app/inbox.html', context)

@login_required
def sent_messages(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'messages_app/sent_messages.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.save()
            return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'messages_app/send_message.html', {'form': form})

from django.shortcuts import get_object_or_404

@login_required
def conversation_detail(request, username):
    # Obtener el otro usuario con quien se está conversando
    other_user = get_object_or_404(User, username=username)

    # Obtener los mensajes entre el usuario actual y el otro usuario
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=other_user)) | 
        (Q(sender=other_user) & Q(recipient=request.user))
    ).order_by('timestamp')

    # Contexto para pasar a la plantilla
    context = {'messages': messages, 'other_user': other_user}
    
    return render(request, 'messages_app/conversation_detail.html', context)

