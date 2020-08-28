# Generated by Django 3.0.8 on 2020-08-28 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umfrage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Umfrage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='UmfrageStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('umfrage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umfrage.Umfrage')),
            ],
        ),
        migrations.CreateModel(
            name='UmfrageExplanation',
            fields=[
                ('umfragestep_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='umfrage.UmfrageStep')),
                ('text', models.TextField()),
            ],
            bases=('umfrage.umfragestep',),
        ),
        migrations.CreateModel(
            name='UmfrageRating',
            fields=[
                ('umfragestep_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='umfrage.UmfrageStep')),
                ('text', models.TextField()),
                ('min_value', models.PositiveIntegerField(default=1)),
                ('min_value_hint', models.TextField()),
                ('max_value', models.PositiveIntegerField(default=5)),
                ('max_value_hint', models.TextField()),
                ('value', models.PositiveIntegerField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
            bases=('umfrage.umfragestep',),
        ),
        migrations.CreateModel(
            name='UmfrageViolation',
            fields=[
                ('umfragestep_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='umfrage.UmfrageStep')),
                ('text', models.TextField()),
                ('violation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='umfrage.Violation')),
            ],
            bases=('umfrage.umfragestep',),
        ),
    ]
