from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CountrySerializer, RegionSerializer, CurrencySerializer, CountryCodeSerializer
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


@api_view(['GET'])
def country_lookup(request):
    """
    List all snippets, or create a new snippet.
    """

    if request.method == 'GET':

        filter_str = request.GET.get('like')
        print(filter_str)

        raw_query = "SELECT * FROM fact_book_country " \
                    "WHERE display_name %% '{0}' or name %% '{0}' " \
                    "ORDER BY similarity(display_name, '{0}') DESC, similarity(name, '{0}') DESC " \
                    "LIMIT 2;".format(filter_str)

        countries = Country.objects.raw(raw_query)

        serializer = CountryCodeSerializer(countries, many=True)
        return Response(serializer.data)
