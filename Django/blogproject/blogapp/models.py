from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=200)
    datetime=models.DateTimeField()
    body=models.TextField()
    

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]