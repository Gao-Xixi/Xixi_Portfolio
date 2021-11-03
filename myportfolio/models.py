from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=255, default='NAME')
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('contact')

