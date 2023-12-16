from django.contrib import admin
from people.models import Contact, ContactTag, Author, AuthorGroup


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactTag)
class ContactTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(AuthorGroup)
class AuthorGroupAdmin(admin.ModelAdmin):
    pass
