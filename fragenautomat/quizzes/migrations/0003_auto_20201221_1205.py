# Generated by Django 3.0.8 on 2020-12-21 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_question_scoped_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number_of_views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='number_of_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
