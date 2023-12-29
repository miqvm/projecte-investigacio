from django.db import models


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


class KeyWord(models.Model):
    name = models.CharField(verbose_name="Nom", max_length=50)
    description = models.TextField(verbose_name="Descripció", null=True, blank=True)

    class Meta:
        verbose_name = "Paraula clau"
        verbose_name_plural = "Paraules clau"
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


class BibliographicResource(models.Model):
    title = models.CharField(verbose_name="Títol", max_length=150)
    authors = models.ManyToManyField(
        "people.BibliographicResourceAuthor", verbose_name="Autors", blank=True
    )
    categories = models.ManyToManyField(
        "items.Category", verbose_name="Categories", blank=True
    )
    date = models.DateField(verbose_name="Data", null=True, blank=True)
    key_words = models.ManyToManyField(
        "items.KeyWord", verbose_name="Paraules clau", blank=True
    )
    direct_sources = models.ManyToManyField(
        "items.DirectSource", verbose_name="Fonts directes", blank=True
    )

    class Meta:
        verbose_name = "Recurs bibliogràfic"
        verbose_name_plural = "Recursos bibliogràfics"
        ordering = ["title"]

    def __str__(self):
        return self.title


class DirectSource(models.Model):
    title = models.CharField(verbose_name="Títol", max_length=150)
    date = models.DateField(verbose_name="Data", blank=True, null=True)
    location = models.ForeignKey(
        "items.Location",
        verbose_name="Ubicació",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    categories = models.ManyToManyField(
        "items.Category", verbose_name="Categories", blank=True
    )
    authors = models.ManyToManyField(
        "people.DirectSourceAuthor", verbose_name="Autors", blank=True
    )
    collective = models.ForeignKey(
        "people.Collective",
        verbose_name="Col·lectiu",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    WORKS_NATURE_CHOICES = [
        ("o", "Original"),
        ("rf", "Reproducció fotogràfica"),
        ("cp", "Copia"),
    ]
    works_nature = models.CharField(
        verbose_name="Naturalesa de l'obra",
        choices=WORKS_NATURE_CHOICES,
        max_length=3,
        blank=True,
        null=True,
    )
    origin = models.CharField(
        verbose_name="Origen", max_length=150, null=True, blank=True
    )
    thematic = models.CharField(
        verbose_name="Temàtica", max_length=150, null=True, blank=True
    )
    critical_component = models.BooleanField(
        verbose_name="Component crític", blank=True, null=True
    )
    message_lecture = models.TextField(
        verbose_name="Lectura del missatge", blank=True, null=True
    )
    main_photo = models.ForeignKey(
        "items.Image",
        verbose_name="Imatge principal",
        on_delete=models.SET_NULL,
        related_name="main_photo_directsource",
        blank=True,
        null=True,
    )
    aux_photos = models.ManyToManyField(
        "items.Image",
        verbose_name="Imatges auxiliars",
        related_name="aux_photos_directsource",
        blank=True,
    )
    consultation_dates = models.ManyToManyField(
        "items.ConsultationDate", verbose_name="Dates de consulta", blank=True
    )
    materials = models.ManyToManyField(
        "items.Material", verbose_name="Material", blank=True
    )

    class Meta:
        verbose_name = "Font directa"
        verbose_name_plural = "Fonts directes"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(verbose_name="Títol", max_length=150)
    url = models.URLField("URL", max_length=256)

    class Meta:
        verbose_name = "Imatge"
        verbose_name_plural = "Imatges"

    def __str__(self):
        return self.title


class ConsultationDate(models.Model):
    date = models.DateTimeField(verbose_name="Dia i hora de consulta")
    notes = models.TextField(verbose_name="Notes", null=True, blank=True)

    class Meta:
        verbose_name = "Data de consulta"
        verbose_name_plural = "Dates de consulta"
        ordering = ["date"]

    def __str__(self):
        return self.date.strftime(format="%d/%m/%Y")
