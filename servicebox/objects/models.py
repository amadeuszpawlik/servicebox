from django.db import models

from products.models import Product

class Object(models.Model):
	serial_no = models.CharField(max_length=100, blank=True)
	product = models.ForeignKey(Product,
								related_name='objects',
								null=False,
								blank=False,
								on_delete=models.CASCADE)

	def __str__(self):
		return str(self.product.name) + str(self.serial_no)