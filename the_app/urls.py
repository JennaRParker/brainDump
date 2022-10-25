from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add/', views.PostCreate.as_view(), name='post_create'),
    path('posts/<int:post_id>/', views.post_detail, name='detail'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('accounts/signup/', views.signup, name='signup'),
    path('posts/<int:post_id>/assoc_category/<int:category_id>/', views.assoc_category, name='assoc_category'),
]