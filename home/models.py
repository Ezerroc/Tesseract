from django.db import models
from PIL import Image

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='carousel_images/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
