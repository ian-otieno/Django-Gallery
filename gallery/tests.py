from django.test import TestCase
from .models import Photographer, Category, Location,Images

# Create your tests here.
class PhotographerTestClass(TestCase):
    def setUp(self):
        self.iano = Photographer(first_name = 'ian', last_name='owino', email='ianowino3@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.iano, Photographer))

    def test_save_method(self):
        self.iano.save_photographer()
        photogarphers = Photographer.objects.all()
        self.assertTrue(len(photogarphers)>0)

    def test_delete_method(self):
        self.iano.save_photographer()
        photographers = Photographer.objects.all()
        self.iano.delete_photographer()
        self.assertTrue(len(photographers)==0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category = Category(category_name="Food")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_category(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.new_category.delete_category()
        self.assertTrue(len(categories)==0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location = Location(location_name="Nairobi")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    def test_save_location(self):
        self.new_location.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_category(self):
        self.new_location.save_location()
        locations= Location.objects.all()
        self.new_location.delete_location()
        self.assertTrue(len(locations)==0)

class ImageTestCase(TestCase):
    def setUp(self):
        self.nairobi =Location(location_name='nairobi')
        self.nairobi.save_location()
        self.travel =Category(category_name='travel')
        self.travel.save_category()

        self.new_image = Images(image_name='leopard',image_description='lives in game park', location=self.nairobi, category=self.travel)
        self.new_image.save()