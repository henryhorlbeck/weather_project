from django.db import models
from django.db import models

# defining database table for city
class City(models.Model):
    name = models.CharField(max_length=25, null=True)
    name_asci = models.CharField(max_length=25, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    country = models.CharField(max_length=25, null=True)
    iso2 = models.CharField(max_length=3, null=True)
    iso3 = models.CharField(max_length=4, null=True)
    admin_name = models.CharField(max_length=25, null=True)
    population = models.IntegerField(null=True)
    city_id = models.IntegerField(null=True)
    capital = models.CharField(max_length=25, null=True)
    

    # displays the city name on the dashboard
    def __str__(self):
        return self.name

    # this will let the database use the plural of 'city' as 'cities'
    class Meta:        
        verbose_name_plural = 'cities'

