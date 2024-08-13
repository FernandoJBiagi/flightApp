from django import forms
from .models import MaintenanceRecord, ScheduledMaintenance

class MaintenanceRecordForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ['description', 'date', 'performed_by']

class ScheduledMaintenanceForm(forms.ModelForm):
    class Meta:
        model = ScheduledMaintenance
        fields = ['maintenance', 'start_date', 'end_date']
