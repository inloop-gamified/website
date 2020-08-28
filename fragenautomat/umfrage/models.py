from django.db import models


class Medic(models.Model):
    name = models.TextField(primary_key=True)
    profession = models.TextField()


class Rule(models.Model):
    identifier = models.TextField(primary_key=True)
    explanation = models.TextField()
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE)


class Violation(models.Model):
    user = models.TextField()
    task = models.TextField()
    message = models.TextField()
    priority = models.TextField()
    start_line = models.TextField(null=True, blank=True)
    end_line = models.TextField(null=True, blank=True)
    start_column = models.TextField(null=True, blank=True)
    end_column = models.TextField(null=True, blank=True)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
    file_contents = models.TextField()


class Umfrage(models.Model):
    key = models.CharField(max_length=32)
    is_completed = models.BooleanField(default=False)

class UmfrageStep(models.Model):
    number = models.PositiveIntegerField()
    umfrage = models.ForeignKey(Umfrage, on_delete=models.CASCADE)


class UmfrageExplanation(UmfrageStep):
    umfrage_typ = 'explanation'

    text = models.TextField()


class UmfrageRating(UmfrageStep):
    umfrage_typ = 'rating'

    text = models.TextField()
    min_value = models.PositiveIntegerField(default=1)
    min_value_hint = models.TextField()
    max_value = models.PositiveIntegerField(default=5)
    max_value_hint = models.TextField()
    value = models.PositiveIntegerField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    @property
    def mid_value(self):
        return (self.max_value + self.min_value) / 2


class UmfrageViolation(UmfrageStep):
    umfrage_typ = 'violation'

    text = models.TextField()
    violation = models.ForeignKey(Violation, on_delete=models.CASCADE)
