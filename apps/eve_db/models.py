from xml.dom import minidom
from django.db import models
from eve_proxy.models import CachedDocument
from apps.eve_db.managers import EVEPlayerCorporationManager, EVEPlayerAllianceManager, EVEPlayerCharacterManager
    
class EVEGraphic(models.Model):
    """
    Stored graphic model.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    # Name of the file, should be two numbers separated by underscore, no extension.
    icon_filename = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    is_obsolete = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Graphic'
        verbose_name_plural = 'Graphics'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class EVEMarketGroup(models.Model):
    """
    Market groups are used to group items together in the market browser.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    parent = models.ForeignKey('EVEMarketGroup', blank=True, null=True)
    has_items = models.BooleanField(default=True)
    graphic = models.ForeignKey(EVEGraphic, blank=True, null=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Market Group'
        verbose_name_plural = 'Market Groups'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class EVEInventoryCategory(models.Model):
    """
    Inventory categories are the top level classification for all items, be
    it planets, moons, modules, ships, or any other entity within the game
    that physically exists.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)
    graphic = models.ForeignKey(EVEGraphic, blank=True, null=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Inventory Category'
        verbose_name_plural = 'Inventory Categories'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class EVEInventoryGroup(models.Model):
    """
    Inventory groups are a further sub-classification within an 
    EVEInventoryCategory. For example, the 'Region' inventory group's
    category is 'Celestial'.
    """
    category = models.ForeignKey(EVEInventoryCategory, blank=True, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    graphic = models.ForeignKey(EVEGraphic, blank=True, null=True)
    use_base_price = models.BooleanField(default=False)
    allow_manufacture = models.BooleanField(default=True)
    allow_recycle = models.BooleanField(default=True)
    allow_anchoring = models.BooleanField(default=False)
    is_anchored = models.BooleanField(default=False)
    is_fittable_non_singleton = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Inventory Group'
        verbose_name_plural = 'Inventory Groups'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class EVEInventoryType(models.Model):
    """
    Inventory types are generally objects that can be carried in your
    inventory (with the exception of suns, moons, planets, etc.) These are mostly
    market items, along with some basic attributes of each that are common
    to all items. 
    """
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    group = models.ForeignKey(EVEInventoryGroup, blank=True, null=True)
    market_group = models.ForeignKey(EVEMarketGroup, blank=True, null=True)
    graphic = models.ForeignKey(EVEGraphic, blank=True, null=True)
    radius = models.FloatField(blank=True, null=True)
    mass = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    capacity = models.FloatField(blank=True, null=True)
    portion_size = models.IntegerField(blank=True, null=True)
    race = models.ForeignKey('EVERace', blank=True, null=True)
    base_price = models.FloatField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    chance_of_duplicating = models.FloatField(blank=True, null=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Inventory Type'
        verbose_name_plural = 'Inventory Types'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()
    
class EVEInventoryBlueprintType(models.Model):
    """
    Stores info about each kind of blueprint.
    """
    blueprint_type = models.ForeignKey(EVEInventoryType,
                                       related_name='blueprint_type_set')
    product_type = models.ForeignKey(EVEInventoryType,
                                     related_name='blueprint_product_type_set')
    # This is used for T2. Not always populated.
    parent_blueprint_type = models.ForeignKey(EVEInventoryType, blank=True,
                                              null=True,
                                              related_name='parent_blueprint_type_set')
    tech_level = models.IntegerField(blank=True, null=True)
    research_productivity_time = models.IntegerField(blank=True, null=True)
    research_material_time = models.IntegerField(blank=True, null=True)
    research_copy_time = models.IntegerField(blank=True, null=True)
    research_tech_time = models.IntegerField(blank=True, null=True)
    productivity_modifier = models.IntegerField(blank=True, null=True)
    material_modifier = models.IntegerField(blank=True, null=True)
    waste_factor = models.IntegerField(blank=True, null=True)
    max_production_limit = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Blueprint Type'
        verbose_name_plural = 'Blueprint Types'
        
    def __unicode__(self):
        return "BP: %s" % self.product_type
    
    def __str__(self):
        return self.__unicode__()

class EVERace(models.Model):
    """
    An EVE race.
    """
    name = models.CharField(max_length=30)
    short_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    graphic = models.ForeignKey(EVEGraphic, blank=True, null=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Race'
        verbose_name_plural = 'Races'
        
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.__unicode__()

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
        ordering = ['date_founded']
    
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