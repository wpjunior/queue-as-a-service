from django.conf.urls import url, include

from qaas.consumers.views import (
    ConsumerListView, ConsumerCreateView, ConsumerUpdateView,
)

urlpatterns = [
        url(r'^$', ConsumerListView.as_view(), name='consumer-list'),
        url(r'^add/$', ConsumerCreateView.as_view(), name='consumer-add'),
        url(r'^(?P<pk>\d+)/$', ConsumerUpdateView.as_view(), name='consumer-update'),
]
