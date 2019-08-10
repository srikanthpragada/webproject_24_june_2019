from django import forms
from .models import Student


class AddForm(forms.Form):
    first = forms.IntegerField()
    second = forms.IntegerField()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
