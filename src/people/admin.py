from django.contrib import admin
from items.models import BibliographicResource, DirectSource
from people.forms import (
    DirectSourceAuthorAdminForm,
    ContactAdminForm,
    DirectSourceAuthorInlineForm,
)
from people.models import (
    Contact,
    ContactTag,
    DirectSourceAuthor,
    BibliographicResourceAuthor,
    Collective,
)


@admin.register(ContactTag)
class ContactTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


class DirectSourceAdminInlineAdmin(admin.TabularInline):
    model = DirectSource.authors.through
    extra = 0
    classes = ("module aligned",)
    raw_id_fields = ("directsource",)
    fields = ("directsource",)
    verbose_name_plural = "Obres"
    verbose_name = "Obres"
    readonly_fields = ("directsource",)
    can_delete = False
    max_num = 0


@admin.register(DirectSourceAuthor)
class DirectSourceAuthorAdmin(admin.ModelAdmin):
    form = DirectSourceAuthorAdminForm
    search_fields = (
        "name",
        "surnames",
    )
    list_filter = ("collectives",)
    list_display = ("name", "surnames", "get_collectives")
    inlines = [DirectSourceAdminInlineAdmin]

    def get_collectives(self, obj):
        if obj.collectives.all().exists():
            return ", ".join([collective.name for collective in obj.collectives.all()])
        return "-"

    get_collectives.short_description = "Col·lectius"


class BibliographicResourceAdminInlineAdmin(admin.TabularInline):
    model = BibliographicResource.authors.through
    extra = 0
    classes = ("module aligned",)
    raw_id_fields = ("bibliographicresource",)
    fields = ("bibliographicresource",)
    verbose_name_plural = "Obres"
    verbose_name = "Obres"
    readonly_fields = ("bibliographicresource",)
    can_delete = False
    max_num = 0


@admin.register(BibliographicResourceAuthor)
class BibliographicResourceAuthorAdmin(admin.ModelAdmin):
    search_fields = (
        "name",
        "surnames",
    )
    list_display = (
        "name",
        "surnames",
    )
    inlines = [BibliographicResourceAdminInlineAdmin]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    exclude = ["visit_days"]

    search_fields = (
        "name",
        "surnames",
        "phone",
        "phone_2",
        "email",
        "email_2",
    )
    list_filter = ("tags", "pending_arrange")
    list_display = (
        "name",
        "surnames",
        "phone",
        "email",
        "get_tags",
        "pending_arrange",
        "position",
    )

    def get_tags(self, obj):
        if obj.tags.all().exists():
            return ", ".join([tag.name for tag in obj.tags.all()])
        return "-"

    get_tags.short_description = "Etiquetes"


class DirectSourceAuthorInline(admin.TabularInline):
    model = DirectSourceAuthor.collectives.through
    extra = 1
    classes = ("module aligned",)
    form = DirectSourceAuthorInlineForm
    verbose_name_plural = "Autors"


@admin.register(Collective)
class CollectiveAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "start_date", "end_date")
    inlines = (DirectSourceAuthorInline,)
