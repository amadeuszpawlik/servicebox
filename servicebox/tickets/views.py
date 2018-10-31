from django.http import HttpResponse
from django.shortcuts import render

from .models import Ticket

def index(request):
    latest_tickets_list = Ticket.objects.order_by('-created')[:10]
    context = {
        'latest_tickets_list': latest_tickets_list,
    }
    return render(request, 'tickets/index.html', context) 
