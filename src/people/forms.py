from dal import autocomplete
from django import forms

from people.models import Contact, DirectSourceAuthor


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "tags": autocomplete.ModelSelect2Multiple(url="autocomplete-contacttag"),
        }


class DirectSourceAuthorAdminForm(forms.ModelForm):
    class Meta:
        model = DirectSourceAuthor
        fields = "__all__"
        widgets = {
            "collectives": autocomplete.ModelSelect2Multiple(
                url="autocomplete-collective"
            ),
        }


class DirectSourceAuthorInlineForm(forms.ModelForm):
    class Meta:
        model = DirectSourceAuthor.collectives.through
        fields = "__all__"
        widgets = {
            "directsourceauthor": autocomplete.ModelSelect2(
                url="autocomplete-directsourceauthor"
            ),
        }
