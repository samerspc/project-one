from django import forms
from .models import Design, Contacts
class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ['bg_color', 'main_color', 'length', 'width', 'style', 'image']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'phone', 'email']