from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField() 
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pages:post-detail", kwargs={"id": self.id})
    
