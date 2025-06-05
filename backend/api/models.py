from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('p', 'pending'),
        ('c', 'completed'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='p')
