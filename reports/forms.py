from django import forms
from .models import FlightReport

class FlightReportForm(forms.ModelForm):
    class Meta:
        model = FlightReport
        fields = ['total_flights', 'total_hours_flown', 'average_occupancy_rate']
