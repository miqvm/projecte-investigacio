from django.db import models


class Person(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    surnames = models.CharField(
        verbose_name="Cognoms", max_length=100, null=True, blank=True
    )

    class Meta:
        abstract = True

    @property
    def fullname(self):
        return f"{self.name} {self.surnames}"


class Contact(Person):
    phone = models.CharField(
        verbose_name="Telèfon", max_length=15, null=True, blank=True
    )
    phone_2 = models.CharField(
        verbose_name="Telèfon 2", max_length=15, null=True, blank=True
    )
    email = models.EmailField(
        verbose_name="Email", max_length=254, null=True, blank=True
    )
    email_2 = models.EmailField(
        verbose_name="Email 2", max_length=254, null=True, blank=True
    )
    comments = models.TextField(verbose_name="Comentaris", null=True, blank=True)
    date = models.DateField(verbose_name="Data", auto_now_add=True)
    tags = models.ManyToManyField(
        "people.ContactTag", verbose_name="Etiquetes", blank=True
    )

    class Meta:
        verbose_name = "Contacte"
        verbose_name_plural = "Contactes"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ContactTag(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=70)

    class Meta:
        verbose_name = "Tag de contacte"
        verbose_name_plural = "Tags de contactes"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Author(Person):
    birth_date = models.DateField(verbose_name="Data naixement", null=True, blank=True)
    death_date = models.DateField(verbose_name="Data defunció", null=True, blank=True)
    groups = models.ManyToManyField(
        "people.AuthorGroup", verbose_name="Grups", blank=True
    )

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autors"
        ordering = ["name"]

    def __str__(self):
        return self.name


class AuthorGroup(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    description = models.TextField(verbose_name="Descripció", null=True, blank=True)
    start_date = models.DateField(verbose_name="Data inici", null=True, blank=True)
    end_date = models.DateField(verbose_name="Data final", null=True, blank=True)

    class Meta:
        verbose_name = "Grup d'autors"
        verbose_name_plural = "Grups d'autors"
        ordering = ["name"]

    def __str__(self):
        return self.name
