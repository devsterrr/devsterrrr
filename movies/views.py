from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Movie, Comment, Message
from .forms import MovieForm, CommentForm, MessageForm

def movie_list(request):
    movies = Movie.objects.all().order_by('-created_at')
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comments = movie.comments.all()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.author = request.user
            comment.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = CommentForm()

    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'comments': comments,
        'form': form
    })

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author == request.user:
        comment.delete()
    return redirect('movie_detail', pk=comment.movie.pk)

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Додати фільм'})

@login_required
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Редагувати фільм'})

# --- Представлення для особистих повідомлень ---

@login_required
def dialog_list(request):
    messages = Message.objects.filter(Q(sender=request.user) | Q(recipient=request.user))
    interlocutor_ids = set()
    for msg in messages:
        if msg.sender != request.user:
            interlocutor_ids.add(msg.sender.id)
        if msg.recipient != request.user:
            interlocutor_ids.add(msg.recipient.id)
            
    dialogs = User.objects.filter(id__in=interlocutor_ids)
    return render(request, 'messages/dialog_list.html', {'dialogs': dialogs})

@login_required
def chat_detail(request, username):
    recipient = get_object_or_404(User, username=username)
    if recipient == request.user:
        return redirect('dialog_list')

    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(recipient=recipient)) |
        (Q(sender=recipient) & Q(recipient=request.user))
    ).order_by('created_at')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.recipient = recipient
            msg.save()
            return redirect('chat_detail', username=username)
    else:
        form = MessageForm()

    return render(request, 'messages/chat_detail.html', {
        'recipient': recipient,
        'messages': messages,
        'form': form
    })