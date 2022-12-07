from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from pathlib import Path

import requests

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Start adding places'

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_notes = response.json()
        try:
            self.add_place(place_notes)
        except KeyError as error:
            self.stdout.write(f'\033[91mERROR:\033[0m No required key {error}.')

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='?',
            type=str,
        )

    @staticmethod
    def add_images(place: Place, images_urls: list):
        for num, image_url in enumerate(images_urls, 1):
            response = requests.get(image_url)
            response.raise_for_status()

            file = ContentFile(
                content=response.content,
                name=Path(image_url).name,
            )

            Image.objects.create(position=num, place=place, file=file)

    def add_place(self, place_notes: dict):
        place, created = Place.objects.get_or_create(
            title=place_notes['title'],
            latitude=place_notes['coordinates']['lat'],
            longitude=place_notes['coordinates']['lng'],
            defaults={
                'description_short': place_notes.get('description_short'),
                'description_long': place_notes.get('description_long'),
            }
        )

        if created:
            self.add_images(place, place_notes.get('imgs', []))
            self.stdout.write(f'Added place "{place}".')
        else:
            self.stdout.write(f'\033[93mDOUBLE:\033[0m place "{place}" already exists!')
