from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from qaas.services.models import Service


class ServiceListView(ListView):
    model = Service


class ServiceFormMixin(SuccessMessageMixin):
    model = Service
    fields = ['name', 'description']
    

class ServiceCreateView(ServiceFormMixin, CreateView):
    success_message = "%(name)s was created successfully"


class ServiceUpdateView(ServiceFormMixin, UpdateView):
    success_message = "%(name)s was updated successfully"


class ServiceDeleteView(ServiceFormMixin, DeleteView):
    success_message = "%(name)s was deleted successfully"
    protected_message = "This service has consumers"

    def get_success_url(self):
        return reverse('service-list')

    def post(self, request, *args, **kwargs):
        try:
            return super(ServiceDeleteView, self).delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(self.request, self.protected_message)
            return redirect('.')
