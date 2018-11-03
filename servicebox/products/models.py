from django.db import models

class Product(models.Model):
	def random_color():
		import random
		r = lambda: random.randint(50,255)
		return('#%02X%02X%02X' % (r(),r(),r()))


	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length = 100, blank=False, null=False)
	manufacturer = models.CharField(max_length = 100, blank=True, null=True)
	tag_color = models.CharField(max_length=7, default=random_color)

	def __str__(self):
		return str(self.name)