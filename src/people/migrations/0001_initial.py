# Generated by Django 4.2.8 on 2023-12-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BibliographicResourceAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('surnames', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cognoms')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data naixement')),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='Data defunció')),
            ],
            options={
                'verbose_name': 'Autor recurs bibliogràfic',
                'verbose_name_plural': 'Autors recursos bibliogràfics',
            },
        ),
        migrations.CreateModel(
            name='Collective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripció')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data inici')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Data final')),
            ],
            options={
                'verbose_name': "Col·lectiu d'autors",
                'verbose_name_plural': "Col·lectius d'autors",
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ContactTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Etiqueta de contacte',
                'verbose_name_plural': 'Etiquetes de contactes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='VisitDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Dia i hora de visita')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Dia de visita',
                'verbose_name_plural': 'Dies de visita',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='DirectSourceAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('surnames', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cognoms')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data naixement')),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='Data defunció')),
                ('collectives', models.ManyToManyField(blank=True, to='people.collective', verbose_name='Col·lectius')),
            ],
            options={
                'verbose_name': 'Autor font directa',
                'verbose_name_plural': 'Autors fonts directes',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom')),
                ('surnames', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cognoms')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telèfon')),
                ('phone_2', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telèfon 2')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('email_2', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email 2')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comentaris')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Data')),
                ('pending_arrange', models.BooleanField(verbose_name='Pendent de concertar')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='Càrrec')),
                ('tags', models.ManyToManyField(blank=True, to='people.contacttag', verbose_name='Etiquetes')),
                ('visit_days', models.ManyToManyField(blank=True, to='people.visitday', verbose_name='Dies de visita')),
            ],
            options={
                'verbose_name': 'Contacte',
                'verbose_name_plural': 'Contactes',
                'ordering': ['name'],
            },
        ),
    ]
