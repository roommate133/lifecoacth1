from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        fields=['name', 'email', 'subject', 'message']
        model=Contact
        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control mb-4','placeholder':'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-4','placeholder':'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control mb-4','placeholder':'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control mb-4','placeholder':'Message','rows':'8'}),
        }