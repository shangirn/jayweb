from django import forms

class NameForm(forms.Form):
    to_translate = forms.CharField(label='to_translate', max_length=1000)