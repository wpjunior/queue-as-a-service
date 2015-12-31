from django.conf.urls import url, include

urlpatterns = [
    url(r'^services/', include('qaas.services.urls')),
    url(r'^consumers/', include('qaas.consumers.urls')),
]
