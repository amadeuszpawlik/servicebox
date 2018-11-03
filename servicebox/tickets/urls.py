from django.urls import path, re_path
from django.contrib.auth.decorators import login_required, permission_required

from .views import TicketListAllView, TicketListMyView


urlpatterns = [
    path('', login_required(TicketListAllView.as_view(template_name="tickets/index.html")), name='tickets_all'),
    path('tickets/', login_required(TicketListAllView.as_view(template_name="tickets/index.html")), name='tickets_all'),
    path('tickets/my/', login_required(TicketListMyView.as_view(template_name="tickets/index.html")), name='tickets_my'),
]