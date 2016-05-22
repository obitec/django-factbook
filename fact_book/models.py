from django.db import models
from django.utils.translation import ugettext_lazy as _
from logging import getLogger

# LOGGING
# ---------------------------------------------------------------------------------------------------------------------#
logger = getLogger('django')


# BASE MODELS
# ---------------------------------------------------------------------------------------------------------------------#
class NaturalManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class NaturalModel(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_('Name'))

    def natural_key(self):
        return (self.name,)

    objects = NaturalManager()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


# MODELS
# ---------------------------------------------------------------------------------------------------------------------#
class Continent(NaturalModel):
    """Continent model

    Just and an array field for alternative names
    """
    class Meta:
        verbose_name = _('Continent')
        verbose_name_plural = _('Continents')


class Region(NaturalModel):
    """Region model

    Just and an array field for alternative names
    """
    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')


class Country(NaturalModel):
    """Country model

    Just and an array field for alternative names
    """
    alpha2code = models.CharField(max_length=2, unique=True)
    alpha3code = models.CharField(max_length=3, unique=True, null=True, blank=True)
    continent = models.ForeignKey(Continent, null=True, blank=True, related_name='countries')
    region = models.ForeignKey(Region, null=True, blank=True, related_name='regions')
    capital = models.CharField(max_length=150, null=True, blank=True)
    demonym = models.CharField(max_length=150, null=True, blank=True)
    native_name = models.CharField(max_length=150, null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    display_name = models.CharField(max_length=150, null=True, blank=True)
    position = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.display_name if self.display_name else self.name

    class Meta:
        ordering = ['display_name', ]
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Currency(NaturalModel):
    code = models.CharField(max_length=3, unique=True, verbose_name=_('ISO code'))
    symbol = models.CharField(max_length=10, null=True, blank=True, verbose_name=_('Currency symbol'))

    def __str__(self):
        if self.symbol:
            return "%s - %s (%s)" % (self.code, self.name, self.symbol)
        else:
            return "%s - %s" % (self.code, self.name)

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
        ordering = ['name', ]


class UnitMeasure(NaturalModel):
    class Meta:
        verbose_name = _('Measure')
        verbose_name_plural = _('Measures')
