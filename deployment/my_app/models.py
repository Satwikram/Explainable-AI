from django.db import models

# Create your models here.
class SceneImage(models.Model):

    image_path = models.CharField(max_length = 256)
    prediction = models.CharField(max_length = 256)

