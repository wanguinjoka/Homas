from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Week(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='home_pics', default='default.jpg')

    def __str__(self):
        return self.name

class Breakfast(models.Model):
    image = models.ImageField(upload_to='home_pics', default='default.jpg')
    description = models.CharField(max_length = 100)
    week = models.ForeignKey(Week, related_name='breakfast', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name} Breakfast'

class Lunch(models.Model):
    image = models.ImageField(upload_to='home_pics', default='default.jpg')
    description = models.CharField(max_length = 100)
    week = models.ForeignKey(Week, related_name='lunch', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name} Lunch'

class Supper(models.Model):
    image = models.ImageField(upload_to='home_pics', default='default.jpg')
    description = models.CharField(max_length = 100)
    week = models.ForeignKey(Week, related_name='supper', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name} Supper'

class Clean(models.Model):
    room = models.CharField(max_length = 100)
    details = models.CharField(max_length = 100)
    week = models.ForeignKey(Week, related_name='clean', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name , self.room }'

class Item(models.Model):
    name = models.CharField(max_length = 100)
    quantity = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, related_name='item', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name } Items'

class Note(models.Model):
    caption = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, related_name='note', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name } Notes'
