from django.db import models

class FlightReport(models.Model):
    total_flights = models.IntegerField()
    total_hours_flown = models.FloatField()
    average_occupancy_rate = models.FloatField()

    def __str__(self):
        return f"Report on {self.total_flights} flights"
