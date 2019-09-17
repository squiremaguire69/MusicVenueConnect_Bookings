from django.db import models

# Create your models here.
class Genre(models.Model):
    genre_category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.genre_category


class Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    base_location = models.ForeignKey('Location', on_delete=models.CASCADE)
    genre_category = models.ManyToManyField(Genre) 
    price = models.DecimalField(max_digits=5, decimal_places=2)
    booking_fee = models.DecimalField(max_digits=4, decimal_places=2)
    profile_image = models.ImageField(upload_to='images')
    profile_description = models.TextField()
    contact_name = models.CharField(max_length=60)
    contact_email = models.EmailField()
    contact_phone = models.IntegerField()
    
    def __str__(self):
        return self.artist_name
        
class Location(models.Model):
    town_name = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    
    def __str__(self):
        return self.town_name
        

    
   