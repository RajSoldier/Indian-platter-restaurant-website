from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,default='example@example.com')
    phone = models.CharField(max_length=15)
    persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"





class Chef(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def is_upcoming(self):
        return self.date > timezone.now()


#feedback system
class Feedback(models.Model):
    message = models.TextField()
    recommendation = models.BooleanField(help_text="Would you recommend us to others?")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id} - {'Recommended' if self.recommendation else 'Not Recommended'}"