from django.contrib import admin
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
    VisitDay,
)


@admin.register(ContactTag)
class ContactTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(DirectSourceAuthor)
class DirectSourceAuthorAdmin(admin.ModelAdmin):
    form = DirectSourceAuthorAdminForm
    search_fields = (
        "name",
        "surnames",
    )
    list_filter = ("collectives",)
    list_display = ("name", "surnames", "get_collectives")

    def get_collectives(self, obj):
        if obj.collectives.all().exists():
            return ", ".join([collective.name for collective in obj.collectives.all()])
        return "-"

    get_collectives.short_description = "Col·lectius"


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


@admin.register(VisitDay)
class VisitDayAdmin(admin.ModelAdmin):
    pass


class VisitDayAdminInlineAdmin(admin.TabularInline):
    model = Contact.visit_days.through
    extra = 1
    classes = ("module aligned",)
    raw_id_fields = ("visitday",)
    fields = ("visitday", "visitday_notes")
    verbose_name_plural = "Dies de visita"

    def visitday_notes(self, obj):
        return obj.visitday.notes

    visitday_notes.short_description = "Notes"

    def get_readonly_fields(self, request, obj=None):
        return ("visitday_notes",) + super().get_readonly_fields(request, obj)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm
    inlines = (VisitDayAdminInlineAdmin,)
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


#    fields = ("visitday", "visitday_notes")
@admin.register(Collective)
class CollectiveAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "start_date", "end_date")
    inlines = (DirectSourceAuthorInline,)
