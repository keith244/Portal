from django import forms
# from .models import Jobs
class DocumentForm(forms.Form):
    document = forms.FileField(required=True, error_messages={'required': 'Please upload a document.'})
# class JobForm(forms.ModelForm):
#     class Meta:
#         model = Jobs
#         fields = ['title','responsibilities','requirements','adder']
