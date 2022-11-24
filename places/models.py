from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        verbose_name='Изображение',
        blank=True,
        null=True,
        upload_to='images',
    )