from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Passenger
from .forms import PassengerForm

@login_required
def passenger_list(request):
    passengers = Passenger.objects.all()
    return render(request, 'passengers/passenger_list.html', {'passengers': passengers})

@login_required
def passenger_detail(request, id):
    passenger = get_object_or_404(Passenger, id=id)
    return render(request, 'passengers/passenger_detail.html', {'passenger': passenger})

@login_required
def passenger_create(request):
    if request.method == "POST":
        form = PassengerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('passenger_list')
    else:
        form = PassengerForm()
    return render(request, 'passengers/passenger_form.html', {'form': form})

@login_required
def passenger_update(request, id):
    passenger = get_object_or_404(Passenger, id=id)
    if request.method == "POST":
        form = PassengerForm(request.POST, request.FILES, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('passenger_list')
    else:
        form = PassengerForm(instance=passenger)
    return render(request, 'passengers/passenger_form.html', {'form': form})

@login_required
def passenger_delete(request, id):
    passenger = get_object_or_404(Passenger, id=id)
    if request.method == "POST":
        passenger.delete()
        return redirect('passenger_list')
    return render(request, 'passengers/passenger_confirm_delete.html', {'passenger': passenger})
