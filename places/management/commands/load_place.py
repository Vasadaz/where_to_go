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
        self.add_place(place_notes)

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='?',
            type=str,
        )

    @staticmethod
    def add_images(place: Place, image_urls: list):
        if not image_urls:
            return

        for num, image_url in enumerate(image_urls, 1):
            image = Image(
                position=num,
                place=place,
            )

            response = requests.get(image_url)
            response.raise_for_status()

            image.file.save(
                name=Path(image_url).name,
                content=ContentFile(requests.get(image_url).content),
                save=True
            )

    def add_place(self, place_notes: dict):
        if title := place_notes.get('title'):
            pass
        else:
            return self.stdout.write('\033[91mERROR:\033[0m No required key "title"!\n')

        if coordinates := place_notes.get('coordinates'):
            if latitude := coordinates.get('lat'):
                pass
            else:
                return self.stdout.write('\033[91mERROR:\033[0m No required key "latitude"\n')

            if longitude := coordinates.get('lng'):
                pass
            else:
                return self.stdout.write('\033[91mERROR:\033[0m No required key "longitude"\n')
        else:
            return self.stdout.write('\033[91mERROR:\033[0m No required key "coordinates"\n')

        place, created = Place.objects.get_or_create(
            title=title,
            latitude=latitude,
            longitude=longitude,
            defaults={
                'description_short': place_notes.get('description_short'),
                'description_long': place_notes.get('description_long'),
            }
        )

        if created:
            imgs = place_notes.get('imgs')

            if imgs:
                self.add_images(place, imgs)

            self.stdout.write(f'Added place "{place}".')
        else:
            self.stdout.write(f'\033[93mDOUBLE:\033[0m place "{place}" already exists!')
