from dal import autocomplete
from django import forms

from people.models import Contact, Author


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "tags": autocomplete.ModelSelect2Multiple(url="autocomplete-contacttag"),
        }


class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        widgets = {
            "groups": autocomplete.ModelSelect2Multiple(url="autocomplete-authorgroup"),
        }
