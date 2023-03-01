from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    message = forms.CharField(max_length=100, widget=forms.Textarea)