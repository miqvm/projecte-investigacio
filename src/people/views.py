from items.views import BasePublicationAutocomplete
from people.models import (
    BibliographicResourceAuthor,
    DirectSourceAuthor,
    Collective,
    ContactTag,
)


class CollectiveAutocomplete(BasePublicationAutocomplete):
    model = Collective
    model_field_name = "name"


class ContactTagAutocomplete(BasePublicationAutocomplete):
    model = ContactTag
    model_field_name = "name"


class BibliographicResourceAuthorAutocomplete(BasePublicationAutocomplete):
    model = BibliographicResourceAuthor

    model_field_name = "name"

    def get_result_label(self, result):
        return result.fullname


class DirectSourceAuthorAutocomplete(BasePublicationAutocomplete):
    model = DirectSourceAuthor
    model_field_name = "name"

    def get_result_label(self, result):
        return result.fullname
