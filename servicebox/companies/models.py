from django.db import models
from customers.models import Customer
from tickets.models import Ticket
from products.models import Product
from objects.models import Object

class Company(models.Model):
    name = models.CharField(max_length=60, blank=False)

    customers = models.ManyToManyField(Customer, blank=True)
    tickets = models.ManyToManyField(Ticket, blank=True, related_name="company")
    products = models.ManyToManyField(Product, blank=True)
    service_objects = models.ManyToManyField(Object, blank=True)

    def __str__(self):
        return self.name
