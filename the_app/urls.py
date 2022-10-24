from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:post_id>/', views.post_detail, name='detail'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<int:post_id>/add_category/', views.add_category, name='add_category'),
    path('accounts/signup/', views.signup, name='signup'),
]