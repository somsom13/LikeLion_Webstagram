from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Content(models.Model):
    author=models.CharField(max_length=100)
    image=models.ImageField(upload_to='webimg/',blank=True,null=True)
