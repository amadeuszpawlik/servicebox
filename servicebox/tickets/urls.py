from django.urls import path, re_path
from django.contrib.auth.decorators import login_required, permission_required

from .views import TicketListAllView, TicketListMyView, TicketDetailView


urlpatterns = [
    path('', login_required(TicketListAllView.as_view(template_name="tickets/tickets_list.html")), name='tickets_all'),
    path('tickets/', login_required(TicketListAllView.as_view(template_name="tickets/tickets_list.html")), name='tickets_all'),
    path('tickets/my/', login_required(TicketListMyView.as_view(template_name="tickets/tickets_list.html")), name='tickets_my'),
    path('ticket/<int:pk>/', TicketDetailView.as_view(template_name="tickets/ticket_detail.html"), name='ticket_detail'),
]