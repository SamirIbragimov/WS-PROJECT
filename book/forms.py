from django import forms


class Book(forms.Form):
    title = forms.CharField(
        max_length=255
    )
    author = forms.CharField(
        max_length=255
    )

