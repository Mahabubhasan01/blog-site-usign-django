from distutils.command.upload import upload
from secrets import choice
from unicodedata import category
from django.db import models

# Create your models here.

category_choice = (("Food", "Food"), ("Beauty", "Beauty"), ("Travel", "Travel"), ("Techonology", "Technology"))


class Fetured(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    info = models.TextField(max_length=500)
    avatar = models.ImageField()
    writter = models.CharField(max_length=100)
    choice = models.CharField(max_length=50,choices=category_choice)

    def __str__(self):
        return self.name
