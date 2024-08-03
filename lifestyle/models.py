from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField


class lifestylemodel(models.Model):
    main_img_src = models.CharField(max_length=200)
    categori = models.CharField(max_length=200)
    main_heading = models.CharField(max_length=200)
    description = HTMLField()
    img_src_two = models.CharField(max_length=200)
    description_two = HTMLField()
    img_src_three = models.CharField(max_length=200)
    description_three = HTMLField()
    img_src_four = models.CharField(max_length=200)
    img_src_five = models.CharField(max_length=200)
    description_four = HTMLField()
    img_src_six = models.CharField(max_length=200)
    new_slug = AutoSlugField(populate_from='main_heading',unique=True,null=True,default=None)  
    

    

    

# Create your models here.
