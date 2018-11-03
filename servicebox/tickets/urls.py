from django.urls import path, re_path
from django.contrib.auth.decorators import login_required, permission_required

from .views import TicketListAll, TicketListMy


urlpatterns = [
    path('', login_required(TicketListAll.as_view(template_name="tickets/index.html")), name='tickets_all'),
    path('tickets/', login_required(TicketListAll.as_view(template_name="tickets/index.html")), name='tickets_all'),
    path('tickets/my/', login_required(TicketListMy.as_view(template_name="tickets/index.html")), name='tickets_my'),
]