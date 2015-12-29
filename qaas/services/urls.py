from django.conf.urls import url, include

from qaas.services.views import (
    ServiceListView, ServiceCreateView, ServiceUpdateView,
)

urlpatterns = [
        url(r'^$', ServiceListView.as_view(), name='service-list'),
        url(r'^add/$', ServiceCreateView.as_view(), name='service-add'),
        url(r'^(?P<pk>\d+)/$', ServiceUpdateView.as_view(), name='service-update'),
]
