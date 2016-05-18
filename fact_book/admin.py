from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from reversion.admin import VersionAdmin
from logging import getLogger
from .models import Country, Continent, Region, Currency, UnitMeasure

logger = getLogger('django')


class CountryAdmin(ImportExportActionModelAdmin, VersionAdmin):
    # change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ['alpha2code', 'name', 'native_name', 'display_name', 'continent', 'population']
    list_filter = ['continent', 'region']
    search_fields = ['name', 'native_name', 'continent__name', 'region__name', 'alpha2code', 'display_name']


class RegionAdmin(ImportExportActionModelAdmin, VersionAdmin):
    search_fields = ['name', ]


class SubRegionAdmin(ImportExportActionModelAdmin, VersionAdmin):
    search_fields = ['name', ]


class CurrencyAdmin(ImportExportActionModelAdmin, VersionAdmin):
    search_fields = ['name', 'code', 'symbol']
    list_display = ['code', 'name', 'symbol']
    fields = ['code', 'name', 'symbol']


class UniteMeasureAdmin(ImportExportActionModelAdmin, VersionAdmin):
    pass

admin.site.register(Country, CountryAdmin)
admin.site.register(Continent, RegionAdmin)
admin.site.register(Region, SubRegionAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(UnitMeasure, UniteMeasureAdmin)

