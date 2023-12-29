from dal import autocomplete

from items.models import (
    BibliographicResource,
    Category,
    DirectSource,
    KeyWord,
    Location,
    Material,
)


class BasePublicationAutocomplete(autocomplete.Select2QuerySetView):
    model = None
    model_field_name = None

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return self.model.objects.none()

        qs = self.model.objects.all()

        if self.q:
            qs = qs.filter(**{"{}__icontains".format(self.model_field_name): self.q})

        return qs.order_by(self.model_field_name)


class CategoryAutocomplete(BasePublicationAutocomplete):
    model = Category
    model_field_name = "name"


class KeyWordAutocomplete(BasePublicationAutocomplete):
    model = KeyWord
    model_field_name = "name"


class DirectSourceAutocomplete(BasePublicationAutocomplete):
    model = DirectSource
    model_field_name = "title"


class LocationAutocomplete(BasePublicationAutocomplete):
    model = Location
    model_field_name = "name"


class BibliographicResourceAutocomplete(BasePublicationAutocomplete):
    model = BibliographicResource
    model_field_name = "title"


class MaterialAutocomplete(BasePublicationAutocomplete):
    model = Material
    model_field_name = "name"
