from django.urls import path, re_path
from django.contrib.auth.decorators import login_required, permission_required

from .views import CustomerListView

urlpatterns = [
	path('', login_required(CustomerListView.as_view(template_name="customers/customers_list.html")), name='customers_all'),
]