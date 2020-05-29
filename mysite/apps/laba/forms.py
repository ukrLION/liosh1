from django import forms


class TestForms(forms.Form):
	name = forms.CharField()
	age = forms.IntegerField()


