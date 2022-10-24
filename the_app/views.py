from django.shortcuts import render

from .models import Post

def home(request):
    output = Post.objects.all()
    context = {'output': output}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')