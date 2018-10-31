import uuid
from django.db import models

from customers.models import Customer

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(blank=True, null=True)
    message = models.TextField()

    customer = models.ForeignKey(Customer,
                                related_name='tickets',
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
