from dal import autocomplete

from items.models import Category


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
