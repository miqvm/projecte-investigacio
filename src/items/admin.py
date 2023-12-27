from django.contrib import admin
from items.forms import (
    BibliographicResourceInlineForm,
    DirectSourceAdminForm,
    BibliographicResourceAdminForm,
)
from items.models import (
    Location,
    Category,
    KeyWord,
    Material,
    BibliographicResource,
    DirectSource,
    Image,
    ConsultationDate,
)
from django.utils.html import format_html


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(KeyWord)
class KeyWordAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(BibliographicResource)
class BibliographicResourceAdmin(admin.ModelAdmin):
    form = BibliographicResourceAdminForm
    search_fields = ("title",)
    list_filter = (
        "authors",
        "categories",
        "key_words",
        "direct_sources",
    )
    list_display = (
        "title",
        "date",
        "get_categories",
        "get_authors",
        "get_direct_sources",
    )

    def get_categories(self, obj):
        if obj.categories.all().exists():
            return ", ".join([category.name for category in obj.categories.all()])
        return "-"

    get_categories.short_description = "Categories"

    def get_authors(self, obj):
        if obj.authors.all().exists():
            return ", ".join([author.fullname for author in obj.authors.all()])
        return "-"

    get_authors.short_description = "Autors"

    def get_direct_sources(self, obj):
        if obj.direct_sources.all().exists():
            return ", ".join(
                [direct_source.title for direct_source in obj.direct_sources.all()]
            )
        return "-"

    get_direct_sources.short_description = "Fonts directes"


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "url_redirect")

    def url_redirect(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>'.format(obj.url, obj.url)
        )

    url_redirect.short_description = "URL"


@admin.register(ConsultationDate)
class ConsultationDateAdmin(admin.ModelAdmin):
    pass


class ConsultationDateAdminInlineAdmin(admin.TabularInline):
    model = DirectSource.consultation_dates.through
    extra = 1
    classes = ("module aligned",)
    raw_id_fields = ("consultationdate",)
    fields = ("consultationdate", "consultationdate_notes")
    verbose_name_plural = "Dates de consulta"

    def consultationdate_notes(self, obj):
        return obj.consultationdate.notes

    consultationdate_notes.short_description = "Notes"

    def get_readonly_fields(self, request, obj=None):
        return ("consultationdate_notes",) + super().get_readonly_fields(request, obj)


class AuxPhotosAdminInlineAdmin(admin.TabularInline):
    model = DirectSource.aux_photos.through
    extra = 1
    classes = ("module aligned",)
    raw_id_fields = ("image",)
    fields = ("image", "image_thumb")
    verbose_name_plural = "Fotos auxiliars"

    def image_thumb(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>'.format(obj.image.url, obj.image.url)
        )

    image_thumb.short_description = "Enllaç"

    def get_readonly_fields(self, request, obj=None):
        return ("image_thumb",) + super().get_readonly_fields(request, obj)


class BibliographicResourceInlineAdmin(admin.TabularInline):
    model = BibliographicResource.direct_sources.through
    extra = 1
    classes = ("module aligned",)
    verbose_name_plural = "Recursos Bibliogràfics"
    form = BibliographicResourceInlineForm


@admin.register(DirectSource)
class DirectSourceAdmin(admin.ModelAdmin):
    form = DirectSourceAdminForm
    inlines = (
        AuxPhotosAdminInlineAdmin,
        ConsultationDateAdminInlineAdmin,
        BibliographicResourceInlineAdmin,
    )
    fields = [
        "title",
        "date",
        "location",
        "collective",
        "works_nature",
        "origin",
        "thematic",
        "critical_component",
        "message_lecture",
        "categories",
        "authors",
        ("main_photo", "main_photo_thumb"),
    ]
    search_fields = (
        "title",
        "location__name",
        "collective__name",
    )
    list_filter = (
        "location",
        "categories",
        "authors",
        "collective",
        "works_nature",
        "critical_component",
    )
    list_display = (
        "title",
        "date",
        "get_categories",
        "get_authors",
        "collective",
        "works_nature",
        "critical_component",
    )

    def get_categories(self, obj):
        if obj.categories.all().exists():
            return ", ".join([category.name for category in obj.categories.all()])
        return "-"

    get_categories.short_description = "Categories"

    def get_authors(self, obj):
        if obj.authors.all().exists():
            return ", ".join([author.fullname for author in obj.authors.all()])
        return "-"

    get_authors.short_description = "Autors"

    def main_photo_thumb(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>'.format(
                obj.main_photo.url, obj.main_photo.url
            )
        )

    main_photo_thumb.short_description = "Enllaç"

    def get_readonly_fields(self, request, obj=None):
        return ("main_photo_thumb",) + super().get_readonly_fields(request, obj)
