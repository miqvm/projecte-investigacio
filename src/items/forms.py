from dal import autocomplete
from django import forms

from items.models import Item


class ItemAdminForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
        widgets = {
            "authors": autocomplete.ModelSelect2Multiple(url="autocomplete-author"),
            "categories": autocomplete.ModelSelect2Multiple(
                url="autocomplete-category"
            ),
        }
