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


def add_image(dish_obj, categories: list):
    for category in categories:
        if category:
            category_obj, created = Image.objects.get_or_create(
                title=category,
            )
            dish_obj.categories.add(category_obj)

def add_place(place_notes: dict):
    place_obj, created = Place.objects.get_or_create(
        title=place_notes['title'],
        description_short=place_notes['description_short'],
        description_long=place_notes['description_long'],
        latitude=place_notes['coordinates']['lat'],
        longitude=place_notes['coordinates']['lng'],
    )

    if created:
        print('Add place:', place_obj)
    else:
        print(f'\033[93mDOUBLE:\033[0m place "{place_obj}" already exists!')


def download_image(image_url, path):
    response = requests.get(image_url)
    response.raise_for_status()

    file_name = f'{title}.jpg'.replace('"', '')
    save_img_path = path / file_name
    with open(save_img_path, 'wb') as file:
        file.write(response.content)
    return save_img_path.relative_to('media')


def main(url: str):
    images_save_path = Path('media/images')
    if not images_save_path.exists():
        images_save_path.mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()
    place_notes = response.json()
    add_place(place_notes)