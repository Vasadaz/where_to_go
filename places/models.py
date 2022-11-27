from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        db_index=True,
        max_length=200,
        unique=True,
    )
    place_id = models.CharField(max_length=50, default='place_id')
    description_short = models.TextField(max_length=500)
    description_long = HTMLField()
    latitude = models.FloatField(default=0.0)  # Широта
    longitude = models.FloatField(default=0.0)  # Долгота

    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    position = models.PositiveSmallIntegerField(
        default=0,
        db_index=True,
    )
    image = models.ImageField(
        upload_to='images',
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
    )

    class Meta:
        ordering = ['position']
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return f'{self.place} {self.position} '
