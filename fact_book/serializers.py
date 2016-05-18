from rest_framework import serializers
from .models import Country, Region, Currency
from logging import getLogger


# LOGGING
# ---------------------------------------------------------------------------------------------------------------------#
logger = getLogger('django')


# SERIALIZERS
# ---------------------------------------------------------------------------------------------------------------------#
class RegionSerializer(serializers.ModelSerializer):
    country_set = serializers.StringRelatedField(many=True, read_only=False)

    class Meta:
        model = Region
        fields = ('name', 'countries')


class CurrencySerializer(serializers.ModelSerializer):
    country_set = serializers.StringRelatedField(many=True, read_only=False)

    class Meta:
        model = Currency
        fields = ('code', 'name')


class CountrySerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField()

    class Meta:
        model = Country
        fields = ('name', 'region', 'sub_region', 'native_name', 'population', )
