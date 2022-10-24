from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    #comment
    #likes
    #dislikes
    #category many to many field
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return(self.caption)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})
