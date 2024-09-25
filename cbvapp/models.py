from django.db import models
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    ceo = models.CharField(max_length=100)
    started = models.IntegerField()
    origin = models.CharField(max_length=100)
    logo = models.ImageField(upload_to= "logos/", blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    
    
class Car(models.Model):
    company = models.ForeignKey(Company , related_name="companies", on_delete=models.CASCADE)
    car_name = models.CharField(max_length=100)
    milliege = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    seat_capicity = models.IntegerField()
    is_rooftoop = models.BooleanField(default=False)
    cars_img = models.ImageField(upload_to="cars/",blank=True, null=True)

    def __str__(self):
        return self.car_name
    
    # def get_absolute_url(self):
    #     return reverse("list", kwargs={"pk": self.pk})
    