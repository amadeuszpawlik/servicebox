from django.views.generic import ListView, DetailView
from django.db.models import Q
from functools import reduce
import operator

from .models import Ticket

class TicketListAllView(ListView):

	paginate_by = 10
	context_object_name = 'tickets_list'
	extra_context = {}

	def get_filtering(self, override=None):
		if(override):
			list_type = override
		else:
			list_type = self.request.GET.get('list', 'open')
			self.extra_context['list_type']=list_type

		if(list_type == 'open'):
			return [Q(closed__isnull=True)]
		elif(list_type == 'unassigned'):
			return [Q(assignee__isnull=True) & Q(closed__isnull=True)]
		elif(list_type == 'closed'):
			return [Q(closed__isnull=False)]
		else:
			return []

	def get_mainlist(self):
		return Ticket.objects.filter(company=self.request.user.company)

	def get_queryset(self):
		order_by = '-created' #self.request.GET.get('order_by', '-created') #must be validated
		filter_by = self.get_filtering()
		query = self.get_mainlist()

		extra_extra_context = {'open_count':query.filter(reduce(operator.or_, self.get_filtering('open'))).count(),
						      'unassigned_count':query.filter(reduce(operator.or_, self.get_filtering('unassigned'))).count(),
						      'closed_count':query.filter(reduce(operator.or_, self.get_filtering('closed'))).count()}
		self.extra_context = {**self.extra_context, **extra_extra_context}

		return query.order_by(order_by).filter(reduce(operator.or_, filter_by))

class TicketListMyView(TicketListAllView):

	def get_mainlist(self):
		return Ticket.objects.filter(assignee=self.request.user)

class TicketDetailView(DetailView):
	model = Ticket
	context_object_name = 'ticket'
