from django.db import models


class Item(models.Model):
    title = models.CharField(verbose_name="Títol", max_length=50)
    location = models.ForeignKey(
        "items.Location",
        verbose_name="Ubicació",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    authors = models.ManyToManyField("people.Author", verbose_name="Autor", blank=True)
    group = models.ForeignKey(
        "people.AuthorGroup",
        verbose_name="Grup",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    categories = models.ManyToManyField(
        "items.Category", verbose_name="Categories", blank=True
    )
    material = models.ForeignKey(
        "items.Material",
        verbose_name="Materials",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    dimensions = models.TextField(verbose_name="Dimensions", null=True, blank=True)
    description = models.TextField(verbose_name="Descripció", null=True, blank=True)
    date = models.DateField(verbose_name="Data", null=True, blank=True)
    origin = models.CharField(
        verbose_name="Origen", max_length=50, null=True, blank=True
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    description = models.TextField(verbose_name="Descripció", null=True, blank=True)

    class Meta:
        verbose_name = "Ubicació"
        verbose_name_plural = "Ubicacions"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    description = models.TextField(verbose_name="Descripció", null=True, blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    description = models.TextField(verbose_name="Descripció", null=True, blank=True)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"
        ordering = ["name"]

    def __str__(self):
        return self.name
