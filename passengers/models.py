from django.db import models

class Passenger(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    rg_number = models.CharField(max_length=20)
    email = models.EmailField()
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.full_name
