import json

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from umfrage.models import Violation, Medic, Rule
from umfrage.models import Umfrage, UmfrageRating, UmfrageViolation, UmfrageExplanation, UmfrageStep


class Command(BaseCommand):
    violations_json_dir = 'fragenautomat/umfrage/management/commands/data/violations.json'

    def load_medics(self):
        with open(self.violations_json_dir) as f:
            violations_json = json.load(f)

        medics = []
        for violation in violations_json:
            medic = Medic(
                name=violation['rule']['medic']['name'],
                profession=violation['rule']['medic']['profession']
            )
            if medic not in medics:
                medics.append(medic)

        Medic.objects.bulk_create(medics)
        self.stdout.write(self.style.SUCCESS(
            f'Created {len(medics)} Medics.'
        ))

    def handle(self, *args, **kwargs):
        self.load_medics()
