from django.db import models 


class Passenger(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    rg = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)
    document = models.FileField(upload_to='documents/', blank=True, null=True)  # Campo adicionado

    def __str__(self):
        return self.full_name
