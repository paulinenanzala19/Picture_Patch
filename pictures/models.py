from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to = 'images/', default='no image')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True,auto_now=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE) 
    location = models.ForeignKey('Location',on_delete=models.CASCADE,default=1) 

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['description']

    @classmethod
    def get_image(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def display_location(cls,name):
        location = cls.objects.filter(location=name)
        return location

    @classmethod
    def display_category(cls,cate):
        categorys=cls.objects.filter(categorys=cate)
        return categorys
    
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__title__icontains=search_term)
        return image

    def __str__(self):
        return self.title

    
class Location(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
       return self.title


    def save_title(self):
        self.save()
    
    def delete_title(self):
        self.delete() 

    @classmethod
    def find_location(cls):
        location=Location.objects.all()
        return location

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(title=value)

class Category(models.Model):
    title = models.CharField(max_length=60)


    def save_title(self):
        self.save()

    def delete_title(self):
        self.delete() 

    def __str__(self):
       return self.title 


    

    
