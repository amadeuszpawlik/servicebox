import uuid
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from customers.models import Customer
from objects.models import Object
from users.models import User

class Ticket(models.Model):
    internal_id = models.IntegerField(editable=False, default='0')
    created = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(blank=True, null=True)
    message = models.TextField()

    customer = models.ForeignKey(Customer,
                                related_name='tickets',
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)

    referred_obj = models.ForeignKey(Object,
                                    related_name='tickets',
                                    null=True,
                                    blank=True,
                                    on_delete=models.CASCADE)

    assignee = models.ForeignKey(User,
                                 related_name='tickets',
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)

    reporter = models.CharField(max_length=70, blank=False)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.internal_id = Ticket.objects.count() + 1 
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.internal_id)

