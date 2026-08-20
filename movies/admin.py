from django.contrib import admin
from .models import Movie, Comment, Message

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('year',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'movie', 'created_at')
    search_fields = ('text', 'author__username')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'created_at', 'is_read')
    search_fields = ('sender__username', 'recipient__username', 'text')