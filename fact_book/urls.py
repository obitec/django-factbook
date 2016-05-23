from django.conf.urls import url
from .views import country_lookup

urlpatterns = [
    url(r'^country/lookup/$', country_lookup),
]
