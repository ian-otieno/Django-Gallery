from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name

    def save_photographer(self):
        self.save()

    def delete_photographer(self):
        self.delete()

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
class Location(models.Model):
    location_name = models.CharField(max_length=30)
    

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Images(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = CloudinaryField('image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
@classmethod
def update_image(cls, id,value):
        image = cls.objects.filter(id=id).update(image_name=value)
        return image
   

@classmethod
def get_image_by_id(cls, image_id):
        image= cls.objects.filter(id = image_id)
        return image
        
@classmethod
def search_image_by_category(cls,search_term):
        search_result = cls.objects.filter(category__category_name__icontains=search_term)
        return search_result
@classmethod
def get_images_by_location(cls,location):
        location_images = cls.objects.filter(location__location_name=location).all()
        return location_images

@classmethod
def get_images_by_category(cls,category):
        category_images = cls.objects.filter(category__category_name=category).all()
        return category_images

        
