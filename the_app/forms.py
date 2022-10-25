from django.forms import ModelForm
from .models import Comment, Category

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['option',]