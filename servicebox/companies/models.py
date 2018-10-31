from django.db import models
from customers.models import Customer

class Company(models.Model):
    name = models.CharField(max_length=60, blank=False)

    customers = models.ManyToManyField(Customer, blank=True)
    
    def __str__(self):
        return self.name
