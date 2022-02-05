from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return "{}, {}".format(self.id, self.title)