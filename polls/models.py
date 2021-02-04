from django.db import models

# Create your models here.

class RestaurantLocation(models.Model):
    name        =   models.CharField(max_length=250)
    location    =   models.CharField(max_length=120, null=True, blank=True)
    category    =   models.CharField(max_length=120, null=True,blank=True)
    timestamp   =   models.DateTimeField(auto_now=False, auto_now_add=False)
    updated     =   models.DateTimeField(auto_now=True)
    mydate_f    =   models.DateField(auto_now=False,auto_now_add=False)
    slug        =   models.SlugField(unique=True)

    def __str__(self):
        return self.name
