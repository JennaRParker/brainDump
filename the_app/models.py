from calendar import c
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

OPTIONS = (
    ('S', 'STORY'),
    ('V', 'VENT'),
    ('C', 'CONFESSION'),
    ('I', 'IDEA'),
    ('A', 'ADVICE'),
    ('O', 'OPINION'),
    ('W', 'CREATIVE WRITING'),
    ('F', 'FUN FACT')
)

class Post(models.Model):
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, default='That time when..')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

class Comment(models.Model):
    text = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Category(models.Model):
    option = models.CharField(
        max_length=1,
        choices=OPTIONS,
        default=OPTIONS[0][1]
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_option_display()}"


    
