from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from qaas.services.models import Service


class ServiceListView(ListView):
    model = Service


class ServiceFormMixin(SuccessMessageMixin):
    model = Service
    fields = ['name']
    

class ServiceCreateView(ServiceFormMixin, CreateView):
    success_message = "%(name)s was created successfully"


class ServiceUpdateView(ServiceFormMixin, UpdateView):
    success_message = "%(name)s was updated successfully"

