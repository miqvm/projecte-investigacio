from django.urls import path

from people.views import (
    AuthorAutocomplete,
    AuthorGroupAutocomplete,
    ContactTagAutocomplete,
)

urlpatterns = [
    path(
        "autocomplete/author",
        AuthorAutocomplete.as_view(),
        name="autocomplete-author",
    ),
    path(
        "autocomplete/authorgroup",
        AuthorGroupAutocomplete.as_view(),
        name="autocomplete-authorgroup",
    ),
    path(
        "autocomplete/contacttag",
        ContactTagAutocomplete.as_view(),
        name="autocomplete-contacttag",
    ),
]
