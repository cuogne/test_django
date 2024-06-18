from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Person
        fields = ['name', 'age', 'message']
