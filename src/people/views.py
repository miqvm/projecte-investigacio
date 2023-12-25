from items.views import BasePublicationAutocomplete
from people.models import Author, AuthorGroup, ContactTag


class AuthorAutocomplete(BasePublicationAutocomplete):
    model = Author
    model_field_name = "name"

    def get_result_label(self, result):
        return result.fullname


class AuthorGroupAutocomplete(BasePublicationAutocomplete):
    model = AuthorGroup
    model_field_name = "name"


class ContactTagAutocomplete(BasePublicationAutocomplete):
    model = ContactTag
    model_field_name = "name"
