from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to = 'articles/', unique=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['description']

class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
       return self.name
