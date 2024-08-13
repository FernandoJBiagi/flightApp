from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import FlightReport
from .forms import FlightReportForm

@login_required
def report_list(request):
    reports = FlightReport.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

@login_required
def report_detail(request, id):
    report = get_object_or_404(FlightReport, id=id)
    return render(request, 'reports/report_detail.html', {'report': report})

@login_required
def report_create(request):
    if request.method == "POST":
        form = FlightReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = FlightReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

@login_required
def report_update(request, id):
    report = get_object_or_404(FlightReport, id=id)
    if request.method == "POST":
        form = FlightReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = FlightReportForm(instance=report)
    return render(request, 'reports/report_form.html', {'form': form})

@login_required
def report_delete(request, id):
    report = get_object_or_404(FlightReport, id=id)
    if request.method == "POST":
        report.delete()
        return redirect('report_list')
    return render(request, 'reports/report_confirm_delete.html', {'report': report})
