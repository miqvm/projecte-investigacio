from django.db import models


class Item(models.Model):
    title = models.CharField(verbose_name="Títol", max_length=50)
    location = models.ForeignKey("items.Location", verbose_name="Ubicació", on_delete=models.CASCADE, null=True, blank=True)
    authors = models.ManyToManyField("people.Author", verbose_name="Autor")
    group = models.ForeignKey("people.AuthorGroup", verbose_name="Grup", on_delete=models.CASCADE, null=True, blank=True)
    categories = models.ManyToManyField("items.Category", verbose_name="Categories")
    material = models.ForeignKey("items.Material", verbose_name="Materials", on_delete=models.CASCADE, null=True, blank=True)
    dimensions = models.TextField(verbose_name="Dimensions", null=True, blank=True)
    description = models.TextField(verbose_name="Descripció", null=True, blank=True)
    date = models.DateField(verbose_name="Data", null=True, blank=True)
    origin = models.CharField(verbose_name="Origen", max_length=50, null=True, blank=True)


class Location(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    description = models.TextField(verbose_name="Descripció")


class Category(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    description = models.TextField(verbose_name="Descripció")


class Material(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    description = models.TextField(verbose_name="Descripció")
