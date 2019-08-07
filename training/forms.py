from django import forms


class AddForm(forms.Form):
    first = forms.IntegerField()
    second = forms.IntegerField()
