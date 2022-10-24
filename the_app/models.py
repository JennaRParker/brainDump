from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

OPTIONS = (
    ('S', 'Storytime'),
    ('V', 'Vent'),
    ('C', 'Confession'),
    ('I', 'Idea'),
    ('A', 'Advice'),
    ('O', 'Opionion'),
    ('W', 'Creative Writing')
)

class Post(models.Model):
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, default='That time when..')
    #comment
    #likes
    #dislikes
    #category many to many field
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return(self.caption)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

class Category(models.Model):
    option = models.CharField(
        max_length=1,
        choices=OPTIONS,
        default=OPTIONS[0][1]
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_option_display()}"