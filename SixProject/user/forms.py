from django import forms

class AddForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.IntegerField()
    gender = forms.BooleanField()
    birthDay = forms.DateField()