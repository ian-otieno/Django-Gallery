
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
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
