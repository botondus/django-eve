"""
This module holds data from the EVE XML API.
"""
from django.db import models
from eve_proxy.models import CachedDocument
from eve_api.managers import EVEPlayerCorporationManager, EVEPlayerAllianceManager, EVEPlayerCharacterManager

class EVEPlayerCharacter(models.Model):
    """
    Represents an individual player character within the game. Not to be
    confused with an account.
    """
    name = models.CharField(max_length=255, blank=True, null=False)
    corporation = models.ForeignKey('EVEPlayerCorporation', blank=True, null=True)
    # TODO: Choices field
    race = models.IntegerField(blank=True, null=True)
    # TODO: Choices field
    gender = models.IntegerField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    attrib_intelligence = models.IntegerField(blank=True, null=True)
    attrib_memory = models.IntegerField(blank=True, null=True)
    attrib_charisma = models.IntegerField(blank=True, null=True)
    attrib_perception = models.IntegerField(blank=True, null=True)
    attrib_willpower = models.IntegerField(blank=True, null=True)
    
    objects = EVEPlayerCharacterManager()
    
    class Meta:
        app_label = 'eve_db'
        verbose_name = 'Member Corporation'
        verbose_name_plural = 'Member Corporations'

class EVEPlayerAlliance(models.Model):
    """
    Represents a player-controlled alliance. Updated from the alliance
    EVE XML API puller at intervals.
    """
    name = models.CharField(max_length=255, blank=True, null=False)
    ticker = models.CharField(max_length=15, blank=True, null=False)
    #executor_character = models.ForeignKey(EVECharacter, blank=True, null=False)
    member_count = models.IntegerField(blank=True, null=True)
    date_founded = models.DateField(blank=True, null=True)
    
    objects = EVEPlayerAllianceManager()
    
    class Meta:
        app_label = 'eve_db'
        ordering = ['date_founded']
        verbose_name = 'Player Alliance'
        verbose_name_plural = 'Player Alliances'
    
    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "Alliance #%d" % self.id
        
    def __str__(self):
        return self.__unicode__()

class EVEPlayerCorporation(models.Model):
    """
    Represents a player-controlled corporation. Updated from a mixture of
    the alliance and corporation API pullers.
    """
    name = models.CharField(max_length=255, blank=True, null=True)
    ticker = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(verify_exists=False, blank=True, null=True)
    ceo_character = models.ForeignKey(EVEPlayerCharacter, blank=True, null=True)
    #home_station = models.ForeignKey(EVEStation, blank=True, null=False)
    alliance = models.ForeignKey(EVEPlayerAlliance, blank=True, null=True)
    alliance_join_date = models.DateField(blank=True, null=True)
    tax_rate = models.FloatField(blank=True, null=True)
    member_count = models.IntegerField(blank=True, null=True)
    shares = models.IntegerField(blank=True, null=True)
    
    # Logo generation stuff
    logo_graphic_id = models.IntegerField(blank=True, null=True)
    logo_shape1 = models.IntegerField(blank=True, null=True)
    logo_shape2 = models.IntegerField(blank=True, null=True)
    logo_shape3 = models.IntegerField(blank=True, null=True)
    logo_color1 = models.IntegerField(blank=True, null=True)
    logo_color2 = models.IntegerField(blank=True, null=True)
    logo_color3 = models.IntegerField(blank=True, null=True)
    
    objects = EVEPlayerCorporationManager()
    
    class Meta:
        app_label = 'eve_db'
        verbose_name = 'Player Corporation'
        verbose_name_plural = 'Player Corporations'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "Corp #%d" % self.id
        
    def query_and_update_corp(self):
        """
        Takes an EVEPlayerCorporation object and updates it from the 
        EVE API service.
        """
        # Pull XML from the EVE API via eve_proxy.
        dom = EVEPlayerCorporation.objects.api_corp_sheet_xml(self.id)
        
        # Tuples of pairings of tag names and the attribute on the Corporation
        # object to set the data to.
        tag_mappings = (
            ('corporationName', 'name'),
            ('ticker', 'ticker'),
            ('url', 'url'),
            ('description', 'description'),
            ('memberCount', 'member_count'),
            ('graphicID', 'logo_graphic_id'),
            ('shape1', 'logo_shape1'),
            ('shape2', 'logo_shape2'),
            ('shape3', 'logo_shape3'),
            ('color1', 'logo_color1'),
            ('color2', 'logo_color2'),
            ('color3', 'logo_color3'),
        )
        
        # Iterate through the tag mappings, setting the values of the tag names
        # (first member of the tuple) to the attribute named in the second member
        # of the tuple on the EVEPlayerCorporation object.
        for tag_map in tag_mappings:
            try:
                setattr(self, tag_map[1], 
                        dom.getElementsByTagName(tag_map[0])[0].firstChild.nodeValue)
            except AttributeError:
                # This tag has no value, skip it.
                continue
            except IndexError:
                # Something weird has happened
                print " * Index Error:", tag_map[0]
                continue

        print "Updating", self.id, self.name
        self.save()