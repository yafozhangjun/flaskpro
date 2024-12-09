from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'description', 'docfile')

    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )