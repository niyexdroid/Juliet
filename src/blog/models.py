from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=200 )
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comments = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article-detail", kwargs={"id": self.id})
