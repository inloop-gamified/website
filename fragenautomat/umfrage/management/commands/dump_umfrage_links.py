import json

from django.core.management.base import BaseCommand

from umfrage.models import Umfrage


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for umfrage in Umfrage.objects.all():
            self.stdout.write(f'https://fragenautom.at/umfrage/{umfrage.key}/')
