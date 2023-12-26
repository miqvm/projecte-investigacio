from dal import autocomplete
from django import forms

from items.models import DirectSource, BibliographicResource


class DirectSourceAdminForm(forms.ModelForm):
    class Meta:
        model = DirectSource
        fields = "__all__"
        widgets = {
            "authors": autocomplete.ModelSelect2Multiple(
                url="autocomplete-directsourceauthor"
            ),
            "categories": autocomplete.ModelSelect2Multiple(
                url="autocomplete-category"
            ),
            "location": autocomplete.ModelSelect2(url="autocomplete-location"),
            "collective": autocomplete.ModelSelect2(url="autocomplete-collective"),
        }


class BibliographicResourceAdminForm(forms.ModelForm):
    class Meta:
        model = BibliographicResource
        fields = "__all__"
        widgets = {
            "authors": autocomplete.ModelSelect2Multiple(
                url="autocomplete-bibliographicresourceauthor"
            ),
            "categories": autocomplete.ModelSelect2Multiple(
                url="autocomplete-category"
            ),
            "key_words": autocomplete.ModelSelect2Multiple(url="autocomplete-keyword"),
            "direct_sources": autocomplete.ModelSelect2Multiple(
                url="autocomplete-directsource"
            ),
        }
