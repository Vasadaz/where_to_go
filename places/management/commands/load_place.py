from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Start adding places'

    def handle(self, *args, **options):
        main()


def main():
    print('test')
