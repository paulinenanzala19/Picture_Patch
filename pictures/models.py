from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to = 'images/', unique=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True,auto_now=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE) 
    location = models.ForeignKey('Location',on_delete=models.CASCADE,default=1) 


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['description']

    @classmethod
    def display_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def display_category(cls,cate):
        category=clas.ogjects.filter(category=cate)
        return category

class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
       return self.name


    def save_location(self):
        self.save()

    @classmethod
    def find_location(cls):
        location=Location.objects.all()
        return location

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
       return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()  


    

    
