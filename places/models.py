from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        db_index=True,
        max_length=200,
        unique=True,
    )
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)
    latitude = models.FloatField()  # Широта
    longitude = models.FloatField()  # Долгота

    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'

    def __str__(self):
        return self.title


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
