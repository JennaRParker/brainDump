from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from the_app.forms import CommentForm
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post

def about(request):
    return render(request, 'about.html')

def home(request):
    output = Post.objects.all()
    context = {'output': output}
    return render(request, 'home.html', context)

def post_detail(request, post_id):
        post = Post.objects.get(id=post_id)
        comment_form = CommentForm()
        return render(request,'detail.html', {'post': post, 'comment_form': comment_form})

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'text',)
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/home/'

@login_required
def add_comment(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post_id=post_id
        new_comment.save()
    return redirect('detail', post_id=post_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      return redirect('login')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('login') 