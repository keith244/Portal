from django import forms

class DocumentForm(forms.Form):
    document = forms.FileField(required=True, error_messages={'required': 'Please upload a document.'})
