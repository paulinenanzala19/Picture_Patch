from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.new_location = Location(title = 'Nairobi')
        self.new_location.save()
        self.new_category = Category(title = 'Food')
        self.new_category.save()
        self.new_image = Image(title = 'Smokie', description = " Ever heard of smokie pasua? huh!! You'll never look back.",location=self.new_location,category=self.new_category, image='image.jpeg')
        self.new_image.save()

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_food(self):
        self.new_image.save_image()
        image = Image.objects.all()

    def test_delete_food(self):
        self.new_image.save_image()
        self.new_image.delete_image()
class CategoryTestClass(TestCase):
    def setUp(self):
        self.Animals = Category(title = 'Animals')
        self.Animals.save_title()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Animals, Category))

    def test_save_category(self):
        self.test_category = Category(title= 'Travel')
        self.test_category.save_title()
        self.test_category.delete_title()

class LocationTestClass(TestCase):
    def setUp(self):
        self.Miami = Location(title='Miami')
        self.Miami.save_title()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Miami,Location))

    def test_save_method(self):
        self.Miami.save_title()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==1)

    def test_delete_method(self):
        self.Miami.delete_title()
        Station = Location.objects.all()
        print(Station)
        self.assertTrue(len(Station)==0)

    def test_update_location(self):
        updated_location = Location.objects.filter(title='Coloumbia')
        self.assertFalse(len(updated_location)> 0)