from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:post_id>/', views.post_detail, name='detail'),
]