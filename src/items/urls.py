from django.urls import path

from items.views import (
    CategoryAutocomplete,
    KeyWordAutocomplete,
    DirectSourceAutocomplete,
    LocationAutocomplete,
)

urlpatterns = [
    path(
        "autocomplete/category",
        CategoryAutocomplete.as_view(),
        name="autocomplete-category",
    ),
    path(
        "autocomplete/keyword",
        KeyWordAutocomplete.as_view(),
        name="autocomplete-keyword",
    ),
    path(
        "autocomplete/directsource",
        DirectSourceAutocomplete.as_view(),
        name="autocomplete-directsource",
    ),
    path(
        "autocomplete/location",
        LocationAutocomplete.as_view(),
        name="autocomplete-location",
    ),
]
