from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Flight(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pendente'),
        ('A', 'Aprovado'),
        ('R', 'Rejeitado'),
    ]
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    return_time = models.DateTimeField()  # Modificado de arrival_time para return_time
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    approved_by_crew = models.BooleanField(default=False)
    approval_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def clean(self):
        # Verifica se departure_time e return_time não são None antes de validar
        if self.departure_time and self.return_time:
            # Verifica se a data de partida é no futuro
            if self.departure_time < timezone.now():
                raise ValidationError('A data de partida deve ser no futuro.')
            
            # Verifica se a data de retorno é após a data de partida
            if self.return_time <= self.departure_time:
                raise ValidationError('A data de retorno deve ser após a data de partida.')
        else:
            raise ValidationError('As datas de partida e retorno são obrigatórias.')

    def __str__(self):
        return f"{self.origin} to {self.destination} at {self.departure_time}"

class Passenger(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    rg = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class FlightPassenger(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    has_luggage = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.passenger.full_name} on {self.flight.origin} to {self.flight.destination}"