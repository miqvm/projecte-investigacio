# Generated by Django 4.2.8 on 2024-04-29 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='visit_days',
        ),
        migrations.DeleteModel(
            name='VisitDay',
        ),
    ]