from django.db import models

# Create your models here.
class Image(models.Model):
    images=models.ImageField(upload_to = 'images/', default='no image')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True,auto_now=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE) 
    location = models.ForeignKey('Location',on_delete=models.CASCADE,default=1) 

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    class Meta:
        ordering = ['description']

    @classmethod
    def display_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def display_category(cls,cate):
        categorys=cls.objects.filter(categorys=cate)
        return categorys
    
    @classmethod
    def search_image_cat(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images


    
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


    

    
