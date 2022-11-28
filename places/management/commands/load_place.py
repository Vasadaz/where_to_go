from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from pathlib import Path

import requests

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Start adding places'

    def handle(self, *args, **options):
        main(options['url'])

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='?',
            type=str,
        )


def add_images(place: Place, image_urls: list):
    for num, image_url in enumerate(image_urls, 1):
        image = Image(
            position=num,
            place=place,
        )

        response = requests.get(image_url)
        response.raise_for_status()

        content = ContentFile(response.content)
        image_name = Path(image_url).name

        image.image.save(image_name, content, save=True)


def add_place(place_notes: dict):
    place, created = Place.objects.get_or_create(
        title=place_notes['title'],
        description_short=place_notes['description_short'],
        description_long=place_notes['description_long'],
        latitude=place_notes['coordinates']['lat'],
        longitude=place_notes['coordinates']['lng'],
    )

    if created:
        add_images(place, place_notes['imgs'])
        print(f'Added place "{place}".')
    else:
        print(f'\033[93mDOUBLE:\033[0m place "{place}" already exists!')


def main(url: str):
    response = requests.get(url)
    response.raise_for_status()
    place_notes = response.json()
    add_place(place_notes)
