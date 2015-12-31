from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from qaas.consumers.models import Consumer


class ConsumerListView(ListView):
    model = Consumer


class ConsumerFormMixin(SuccessMessageMixin):
    model = Consumer
    fields = ('name',)
    

class ConsumerCreateView(ConsumerFormMixin, CreateView):
    success_message = "%(name)s was created successfully"
    fields = ConsumerFormMixin.fields + ('service',)

                                         
class ConsumerUpdateView(ConsumerFormMixin, UpdateView):
    success_message = "%(name)s was updated successfully"
