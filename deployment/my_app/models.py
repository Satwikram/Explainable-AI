from django.db import models

# Create your models here.
class SceneImage(models.Model):

    imgage_path = models.ImageField(upload_to = 'media')
    prediction = models.CharField(max_length = 256)

