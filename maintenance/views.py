from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import MaintenanceRecord, ScheduledMaintenance
from .forms import MaintenanceRecordForm, ScheduledMaintenanceForm

@login_required
def maintenance_list(request):
    maintenances = MaintenanceRecord.objects.all()
    return render(request, 'maintenance/maintenance_list.html', {'maintenances': maintenances})

@login_required
def maintenance_detail(request, id):
    maintenance = get_object_or_404(MaintenanceRecord, id=id)
    return render(request, 'maintenance/maintenance_detail.html', {'maintenance': maintenance})

@login_required
def maintenance_create(request):
    if request.method == "POST":
        form = MaintenanceRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_list')
    else:
        form = MaintenanceRecordForm()
    return render(request, 'maintenance/maintenance_form.html', {'form': form})

@login_required
def maintenance_update(request, id):
    maintenance = get_object_or_404(MaintenanceRecord, id=id)
    if request.method == "POST":
        form = MaintenanceRecordForm(request.POST, instance=maintenance)
        if form.is_valid():
            form.save()
            return redirect('maintenance_list')
    else:
        form = MaintenanceRecordForm(instance=maintenance)
    return render(request, 'maintenance/maintenance_form.html', {'form': form})

@login_required
def maintenance_delete(request, id):
    maintenance = get_object_or_404(MaintenanceRecord, id=id)
    if request.method == "POST":
        maintenance.delete()
        return redirect('maintenance_list')
    return render(request, 'maintenance/maintenance_confirm_delete.html', {'maintenance': maintenance})
