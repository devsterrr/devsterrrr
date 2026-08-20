from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/add/', views.movie_create, name='movie_create'),
    path('movie/<int:pk>/edit/', views.movie_update, name='movie_update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('messages/', views.dialog_list, name='dialog_list'),
    path('messages/<str:username>/', views.chat_detail, name='chat_detail'),
]