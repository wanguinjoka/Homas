from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Week(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='home_pics/', default='default.jpg')
    quote = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Breakfast(models.Model):
    image = models.ImageField(upload_to='home_pics/', default='default.jpg')
    description = models.CharField(max_length = 100)
    week = models.ForeignKey(Week, related_name='breakfast', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name} Breakfast'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Lunch(models.Model):
    image = models.ImageField(upload_to='home_pics/', default='default.jpg')
    description = models.CharField(max_length = 100)
    week = models.ForeignKey(Week, related_name='lunch', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name} Lunch'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Supper(models.Model):
    image = models.ImageField(upload_to='home_pics/', default='default.jpg')
    description = models.CharField(max_length = 100)
    week = models.ForeignKey(Week, related_name='supper', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name} Supper'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Clean(models.Model):
    room = models.CharField(max_length = 100)
    details = models.CharField(max_length = 100)
    week = models.ForeignKey(Week, related_name='room', on_delete=models.CASCADE)

    def __str__(self):
        return self.room

    def get_absolute_url(self):
        return reverse('week-detail', args={self.week.id})

class Item(models.Model):
    name = models.CharField(max_length = 100)
    quantity = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, related_name='item', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name } Items'

    def get_absolute_url(self):
        return reverse('week-detail', args={self.week.id})

class Note(models.Model):
    caption = models.CharField(max_length = 100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, related_name='note', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.week.name } Notes'

    def get_absolute_url(self):
        return reverse('week-detail', args={self.week.id})

class Supplier(models.Model):
    name = models.CharField(max_length = 100)
    email= models.EmailField()
    

    def __str__(self):
        return f'{self.name } Supplier'

    
