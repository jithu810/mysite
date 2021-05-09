from django.db import models

# Create your models here.
class enquiry(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    message=models.TextField()