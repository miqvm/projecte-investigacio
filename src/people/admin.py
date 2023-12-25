from django.contrib import admin
from people.forms import AuthorAdminForm, ContactAdminForm
from people.models import Contact, ContactTag, Author, AuthorGroup


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    form = ContactAdminForm


@admin.register(ContactTag)
class ContactTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    form = AuthorAdminForm


@admin.register(AuthorGroup)
class AuthorGroupAdmin(admin.ModelAdmin):
    pass
