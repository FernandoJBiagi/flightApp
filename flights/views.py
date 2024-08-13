from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Flight
from .forms import FlightForm
from .utils import send_telegram_message

@login_required
def flight_create(request):
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)
            flight.created_by = request.user
            flight.save()
            send_telegram_message("-4237083945", f"Novo voo criado: {flight.origin} para {flight.destination}")
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flights/flight_form.html', {'form': form})

@login_required
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/flight_list.html', {'flights': flights})

@login_required
def flight_detail(request, id):
    flight = get_object_or_404(Flight, id=id)
    is_crew = request.user.groups.filter(name='crew').exists()  # Verifica se o usuário é do grupo 'crew'
    return render(request, 'flights/flight_detail.html', {'flight': flight, 'is_crew': is_crew})

@login_required
def flight_update(request, id):
    flight = get_object_or_404(Flight, id=id)
    if request.method == "POST":
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flights/flight_form.html', {'form': form})

@login_required
def flight_delete(request, id):
    flight = get_object_or_404(Flight, id=id)
    if request.method == "POST":
        flight.delete()
        return redirect('flight_list')
    return render(request, 'flights/flight_confirm_delete.html', {'flight': flight})

@login_required
def approve_flight(request, id):
    flight = get_object_or_404(Flight, id=id)
    if request.user.groups.filter(name='crew').exists():
        flight.approval_status = 'A'  # Altera o status para "Aprovado"
        flight.approved_by_crew = True
        flight.save()
        send_telegram_message("YOUR_TELEGRAM_CHAT_ID", f"O voo de {flight.origin} para {flight.destination} foi aprovado.")
        return redirect('flight_list')
    else:
        return redirect('flight_list')
