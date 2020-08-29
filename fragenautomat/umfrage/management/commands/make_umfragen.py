import json

from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.db import transaction

from umfrage.models import Violation, Medic, Rule
from umfrage.models import Umfrage, UmfrageRating, UmfrageViolation, UmfrageExplanation, UmfrageStep


class Command(BaseCommand):
    def make_umfragen(self):
        count = Violation.objects.all().count()
        for i, violation in enumerate(Violation.objects.all()):
            umfrage = self.make_umfrage(violation)
            self.stdout.write(self.style.SUCCESS(
                f'Created {umfrage} ({i}/{count}).'
            ))

    def make_umfrage(self, violation):
        key = get_random_string(length=32)
        umfrage = Umfrage.objects.create(key=key)

        UmfrageExplanation.objects.create(
            number=0, umfrage=umfrage,
            text='Willkommen bei einer Umfrage zu Codequalität in INLOOP! Die Bearbeitung dieser Umfrage sollte nicht länger als 10 Minuten dauern.'
        )

        UmfrageRating.objects.create(
            number=1, umfrage=umfrage,
            text='Wie häufig haben Sie bei der Benutzung von INLOOP Rücksicht auf die Code-Qualität Ihrer Lösungen genommen?',
            min_value_hint='Noch nie',
            max_value_hint='Jederzeit'
        )

        UmfrageRating.objects.create(
            number=2, umfrage=umfrage,
            text='Wie wichtig ist Ihnen die Codequalität ihrer eigenen Lösungen?',
            min_value_hint='Unwichtig',
            max_value_hint='Sehr wichtig'
        )

        UmfrageExplanation.objects.create(
            number=3, umfrage=umfrage,
            text='Um Studierende zu motivieren, die Codequalität von eingereichten Lösungen auf INLOOP zu verbessern, sollen den Studierenden einige neue Funktionen bereitgestellt werden.'
        )

        UmfrageExplanation.objects.create(
            number=4, umfrage=umfrage,
            text='Ein Bestandteil dieser neuen Funktionen sind virtuelle Code-Doktoren, welche Sie konsultieren können, um die Codequalität Ihrer Lösung zu verbessern.'
        )

        UmfrageViolation.objects.create(
            number=5, umfrage=umfrage, violation=violation
        )

        UmfrageRating.objects.create(
            number=6, umfrage=umfrage,
            text='Für wie sinnvoll halten Sie die Anmerkung, welche Ihnen hier durch den Code-Doktor gezeigt wird?',
            min_value_hint='Nicht sinnvoll',
            max_value_hint='Sehr sinnvoll'
        )

        UmfrageRating.objects.create(
            number=7, umfrage=umfrage,
            text='Wie hilfreich ist die Erklärung, welche Ihnen der Code-Doktor zusätzlich zum Titel der Anmerkung gibt, um den ursprünglichen Grund der Anmerkung zu verstehen?',
            min_value_hint='Nicht hilfreich',
            max_value_hint='Sehr hilfreich'
        )

        UmfrageRating.objects.create(
            number=8, umfrage=umfrage,
            text='Wie oft würden Sie diese Funktionalität nutzen, um sich über die Codequalität Ihrer Lösungen zu informieren?',
            min_value_hint='Überhaupt nicht',
            max_value_hint='Sehr häufig'
        )

        UmfrageExplanation.objects.create(
            number=9, umfrage=umfrage,
            text='Bitte beantworten Sie nun noch die folgenden Fragen zu den weiteren Funktionen der Erweiterung für INLOOP.'
        )

        UmfrageRating.objects.create(
            number=10, umfrage=umfrage,
            text='Wie stark würde es Sie motivieren, Ihre Code-Qualität in INLOOP zu verbessern, wenn Sie hierbei Punkte erzielen, Level aufsteigen und sich schließlich mit Ihren Kommilitonen vergleichen könnten?',
            min_value_hint='Überhaupt nicht',
            max_value_hint='Sehr stark'
        )

        UmfrageRating.objects.create(
            number=11, umfrage=umfrage,
            text='Wenn Sie eine Aufgabe in INLOOP bestanden haben, wie gern würden Sie dann auch nach Anmerkungen in Lösungen anderer Studierender suchen und dafür Punkte erhalten?',
            min_value_hint='Überhaupt nicht',
            max_value_hint='Sehr gern'
        )

        UmfrageRating.objects.create(
            number=12, umfrage=umfrage,
            text='Wenn Sie nur eine begrenzte Zeit hätten, um die Codequalität einer Aufgabe zu verbessern, um Punkte zu erhalten, wie viel mehr Interesse hätten Sie dann an dieser Herausforderung?',
            min_value_hint='Eher weniger',
            max_value_hint='Eher mehr'
        )

        UmfrageRating.objects.create(
            number=13, umfrage=umfrage,
            text='Wie stark würde es Sie anspornen, wenn Sie beim Suchen, Auseinandersetzen und Verbessern der Codequalität bestimmte Errungenschaften erreichen und diese mit anderen Nutzern teilen könnten?',
            min_value_hint='Überhaupt nicht',
            max_value_hint='Sehr stark'
        )

        return umfrage

    def handle(self, *args, **kwargs):
        self.make_umfragen()
