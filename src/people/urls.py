from django.urls import path

from people.views import (
    CollectiveAutocomplete,
    ContactTagAutocomplete,
    BibliographicResourceAuthorAutocomplete,
    DirectSourceAuthorAutocomplete,
)

urlpatterns = [
    path(
        "autocomplete/collective",
        CollectiveAutocomplete.as_view(),
        name="autocomplete-collective",
    ),
    path(
        "autocomplete/contacttag",
        ContactTagAutocomplete.as_view(),
        name="autocomplete-contacttag",
    ),
    path(
        "autocomplete/bibliographicresourceauthor",
        BibliographicResourceAuthorAutocomplete.as_view(),
        name="autocomplete-bibliographicresourceauthor",
    ),
    path(
        "autocomplete/directsourceauthor",
        DirectSourceAuthorAutocomplete.as_view(),
        name="autocomplete-directsourceauthor",
    ),
]
