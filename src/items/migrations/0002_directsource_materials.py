# Generated by Django 4.2.8 on 2023-12-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directsource',
            name='materials',
            field=models.ManyToManyField(blank=True, to='items.material', verbose_name='Material'),
        ),
    ]