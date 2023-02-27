from django.db import models

# Create your models here.
class houseListingModel(models.Model):
    #the field attributes
    title = models.CharField(max_length=55)
    price = models.IntegerField()
    squareField = models.IntegerField()
    noBedrooms = models.IntegerField()
    address = models.CharField(max_length=55)
    image = models.ImageField(upload_to='uploads/')
    def __str__(self): #the dunder method
        return f'{self.title} with {self.noBedrooms} bedrooms'

