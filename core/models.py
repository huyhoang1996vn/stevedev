from django.db import models

# Create your models here.

class Post(models.Model):
    category = models.CharField(max_length=255)
    title = models.TextField()
    content = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)

    def __str__(self):
         return self.title