from django import forms
from .models import Passenger

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['full_name', 'birth_date', 'rg_number', 'email', 'document']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'rg_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
