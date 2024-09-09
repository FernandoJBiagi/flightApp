from django import forms
from django.utils import timezone
from .models import Flight, FlightPassenger, Passenger

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'departure_time', 'return_time']
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'return_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_departure_time(self):
        departure_time = self.cleaned_data.get('departure_time')
        if departure_time < timezone.now():
            raise forms.ValidationError('A data de partida deve ser no futuro.')
        return departure_time

    def clean_return_time(self):
        return_time = self.cleaned_data.get('return_time')
        departure_time = self.cleaned_data.get('departure_time')
        if return_time <= departure_time:
            raise forms.ValidationError('A data de retorno deve ser após a data de partida.')
        return return_time

class FlightPassengerForm(forms.ModelForm):
    passenger = forms.ModelChoiceField(queryset=Passenger.objects.all(), empty_label="Selecione um passageiro")

    class Meta:
        model = FlightPassenger
        fields = ['passenger', 'has_luggage']

FlightPassengerFormSet = forms.inlineformset_factory(
    Flight, FlightPassenger, form=FlightPassengerForm, extra=1, can_delete=True
)

