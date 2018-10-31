from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=60, blank=False)
    adr_street = models.CharField(max_length=120, blank=False)
    adr_city = models.CharField(max_length=100, blank=False)
    adr_postal = models.CharField(max_length=5)

    def __str__(self):
        return self.name
