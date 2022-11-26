from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    place_id = models.CharField(max_length=50, blank=True)
    description_short = models.CharField(max_length=500, blank=True)
    description_long = models.TextField(blank=True)
    details_url = models.CharField(max_length=50, default='path')
    latitude = models.FloatField(default=0.0)  # Широта
    longitude = models.FloatField(default=0.0)  # Долгота



    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        verbose_name='Изображение',
        blank=True,
        null=True,
        upload_to='images',
    )

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return f'{self.title}'
