from django.db import models

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
    
    class Meta:
        ordering = ['date_founded']
    
    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "Alliance #%d" % self.id  

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

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "Corp #%d" % self.id