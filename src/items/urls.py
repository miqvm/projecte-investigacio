from django.urls import path

from items.views import CategoryAutocomplete

urlpatterns = [
    path(
        "autocomplete/category",
        CategoryAutocomplete.as_view(),
        name="autocomplete-category",
    )
]
