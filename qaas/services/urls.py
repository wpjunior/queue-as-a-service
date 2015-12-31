from django.conf.urls import url, include

from qaas.services.views import (
    ServiceListView, ServiceCreateView, ServiceUpdateView,
    ServiceDeleteView,
)

urlpatterns = [
        url(r'^$', ServiceListView.as_view(), name='service-list'),
        url(r'^add/$', ServiceCreateView.as_view(), name='service-add'),
        url(r'^(?P<pk>\d+)/$', ServiceUpdateView.as_view(), name='service-update'),
        url(r'^delete/(?P<pk>\d+)/$', ServiceDeleteView.as_view(), name='service-delete'),
]
