import json

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from umfrage.models import Violation, Medic, Rule
from umfrage.models import Umfrage, UmfrageRating, UmfrageViolation, UmfrageExplanation, UmfrageStep


class Command(BaseCommand):
    violations_json_dir = 'fragenautomat/umfrage/management/commands/data/violations.json'

    def load_rules(self):
        with open(self.violations_json_dir) as f:
            violations_json = json.load(f)

        rules = []
        for violation in violations_json:
            rule = Rule(
                identifier=violation['rule']['identifier'],
                explanation=violation['rule']['explanation'],
                medic_id=violation['rule']['medic']['name']
            )
            if rule not in rules:
                rules.append(rule)

        Rule.objects.bulk_create(rules)
        self.stdout.write(self.style.SUCCESS(
            f'Created {len(rules)} Rules.'
        ))

    def handle(self, *args, **kwargs):
        self.load_rules()
