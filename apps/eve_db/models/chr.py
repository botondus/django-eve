"""
Character stuff. 
"""
from django.db import models

class EVERace(models.Model):
    """
    An EVE race.
    
    chrRaces
    """
    name = models.CharField(max_length=30)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    graphic = models.ForeignKey('EVEGraphic', blank=True, null=True)
    # TODO: Add allegiance to a Faction here.
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Race'
        verbose_name_plural = 'Races'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

class Faction(models.Model):
    """
    chrFactions
    """
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    solar_system = models.ForeignKey('SolarSystem', blank=True, null=True,
                                     related_name='faction_set')
    corporation = models.ForeignKey('NPCCorporation', blank=True, null=True,
                                    related_name='faction_set')
    size_factor = models.FloatField(blank=True, null=True)
    station_count = models.IntegerField(default=0)
    station_system_count = models.IntegerField(default=0)

    class Meta:
        app_label = 'eve_db'
        ordering = ['id']
        verbose_name = 'Faction'
        verbose_name_plural = 'Factions'

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "Faction #%d" % self.id

    def __str__(self):
        return self.__unicode__()