from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post

def home(request):
    output = Post.objects.all()
    context = {'output': output}
    return render(request, 'home.html', context)

class PostCreate(CreateView):
    model = Post
    fields = ('text',)
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'about.html')