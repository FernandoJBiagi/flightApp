from django.db import models

class MaintenanceRecord(models.Model):
    description = models.TextField()
    date = models.DateField()
    performed_by = models.CharField(max_length=100)

    def __str__(self):
        return f"Maintenance on {self.date} by {self.performed_by}"

class ScheduledMaintenance(models.Model):
    maintenance = models.ForeignKey(MaintenanceRecord, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Scheduled from {self.start_date} to {self.end_date}"
