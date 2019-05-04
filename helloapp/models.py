from django.db import models


# Create your models here.
class Message(models.Model):
    subject = models.CharField(max_length=150)
    body = models.TextField()
    datetime_received = models.DateTimeField(auto_now_add=True)
