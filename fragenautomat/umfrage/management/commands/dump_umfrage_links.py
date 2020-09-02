import json

from django.core.management.base import BaseCommand

from umfrage.models import Umfrage


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        objects = []
        for umfrage in Umfrage.objects.all():
            for step in umfrage.umfragestep_set.all():
                if not hasattr(step, 'umfrageviolation'):
                    continue
                violation = step.umfrageviolation.violation
                objects.append({
                    'identifier': violation.rule.identifier,
                    'url': f'https://fragenautom.at/umfrage/{umfrage.key}/'
                })
        self.stdout.write(json.dumps(objects))
