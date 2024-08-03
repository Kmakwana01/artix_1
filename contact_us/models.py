from django.db import models


class contactemodel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fav_categori = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
