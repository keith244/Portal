from django import forms
from .models import FAQ

class DocumentForm(forms.Form):
    document = forms.FileField(required=True, error_messages={'required': 'Please upload a document.'})
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = [ 'question', 'answer']