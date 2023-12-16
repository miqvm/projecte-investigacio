from django.db import models


class Person(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    surnames = models.CharField(verbose_name="Cognoms", max_length=100, null=True)

    class Meta:
        abstract = True


class Contact(Person):
    phone = models.CharField(verbose_name="Telèfon", max_length=15, null=True)
    phone_2 = models.CharField(verbose_name="Telèfon 2", max_length=15, null=True)
    email = models.EmailField(verbose_name="Email", max_length=254, null=True)
    email_2 = models.EmailField(verbose_name="Email 2", max_length=254, null=True)
    comments = models.TextField(verbose_name="Comentaris", null=True)
    date = models.DateField(verbose_name="Data", auto_now_add=True)
    tags = models.ManyToManyField("people.ContactTag", verbose_name="Etiquetes")


class ContactTag(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=70)


class Author(Person):
    birth_date = models.DateField(verbose_name="Data naixement", null=True, blank=True)
    death_date = models.DateField(verbose_name="Data defunció", null=True, blank=True)
    groups = models.ManyToManyField("people.AuthorGroup", verbose_name="Grups")


class AuthorGroup(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    description = models.TextField(verbose_name="Descripció", null=True)
    start_date = models.DateField(verbose_name="Data inici", null=True, blank=True)
    end_date = models.DateField(verbose_name="Data final", null=True, blank=True)
