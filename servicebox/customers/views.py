from django.views.generic import ListView, DetailView

from .models import Customer

class CustomerListView(ListView):
	paginate_by = 10
	context_object_name = 'customers_list'

	def get_mainlist(self):
		return self.request.user.company.customers.all()

	def get_queryset(self):
		order_by = 'name'
		query = self.get_mainlist()

		return query.order_by(order_by)