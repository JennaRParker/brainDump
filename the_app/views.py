from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from the_app.forms import CategoryForm
from .models import Post

def home(request):
    output = Post.objects.all()
    context = {'output': output}
    return render(request, 'home.html', context)

def post_detail(request, post_id):
        post = Post.objects.get(id=post_id)
        category_form = CategoryForm()
        return render(request,'detail.html', {'post': post, 'category_form': category_form})

class PostCreate(CreateView):
    model = Post
    fields = ('text',)
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = ['text',]

class PostDelete(DeleteView):
    model = Post
    success_url = '/home/'

def about(request):
    return render(request, 'about.html')