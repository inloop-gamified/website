import json

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from umfrage.models import Violation, Medic, Rule
from umfrage.models import Umfrage, UmfrageRating, UmfrageViolation, UmfrageExplanation, UmfrageStep


class Command(BaseCommand):
    violations_json_dir = 'fragenautomat/umfrage/management/commands/data/violations.json'

    def load_violations(self):
        with open(self.violations_json_dir) as f:
            violations_json = json.load(f)

        violations = []
        for violation in violations_json:
            violations.append(Violation(
                user=violation['user'],
                task=violation['task'],
                message=violation['message'],
                priority=violation['priority'],
                start_line=violation.get('start_line'),
                end_line=violation.get('end_line'),
                start_column=violation.get('start_column'),
                end_column=violation.get('end_column'),
                rule_id=violation['rule']['identifier'],
                file_contents=violation['file_contents']
            ))

        Violation.objects.bulk_create(violations)

        self.stdout.write(self.style.SUCCESS(
            f'Created {len(violations)} Violations.'
        ))

    def handle(self, *args, **kwargs):
        self.load_violations()
