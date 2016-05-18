from rest_framework import viewsets
from .serializers import CountrySerializer, RegionSerializer, CurrencySerializer
from .models import Continent, Country, Currency
from logging import getLogger


# LOGGING
# ---------------------------------------------------------------------------------------------------------------------#
logger = getLogger('django')


# API VIEWS
# --------------------------------------------------------------------------------------------------------------------#
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = RegionSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

