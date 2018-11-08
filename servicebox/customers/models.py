from django.db import models
from objects.models import Object
from products.models import Product

class Customer(models.Model):
    name = models.CharField(max_length=60, blank=False)
    adr_street = models.CharField(max_length=120, blank=False)
    adr_city = models.CharField(max_length=100, blank=False)
    adr_postal = models.CharField(max_length=5)

    service_objects = models.ManyToManyField(Object, blank=True)

    def __str__(self):
        return self.name

    def unassigned_tickets(self):
    	return self.tickets.filter(assignee__isnull=True).count()

    def products(self):
    	product_list = []
    	for ser_obj in self.service_objects.all():
    		if ser_obj.product not in product_list:
    			product_list.append(ser_obj.product)

    	return product_list

