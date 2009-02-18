# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Chrbloodlines(models.Model):
    """
    Bloodlines for newly created characters with starting attributes. 
    """
    bloodlinename = models.CharField(max_length=100)
    race = models.ForeignKey('Chrraces')
    description = models.CharField(max_length=1000)
    maledescription = models.CharField(max_length=1000)
    femaledescription = models.CharField(max_length=1000)
    shiptype = models.ForeignKey('Invtypes')
    corporation = models.ForeignKey('Crpnpccorporations')
    perception = models.SmallIntegerField()
    willpower = models.SmallIntegerField()
    charisma = models.SmallIntegerField()
    memory = models.SmallIntegerField()
    intelligence = models.SmallIntegerField()
    graphic = models.ForeignKey('Evegraphics')
    shortdescription = models.CharField(max_length=500)
    shortmaledescription = models.CharField(max_length=500)
    shortfemaledescription = models.CharField(max_length=500)
    
    class Meta:
        db_table = u'chrbloodlines'
        
    def __unicode__(self):
        return self.bloodlinename

class Chrancestries(models.Model):
    """
    Available Ancestries with bonus skills and items. 
    """
    ancestryname = models.CharField(max_length=100)
    bloodline = models.ForeignKey('Chrbloodlines')
    description = models.CharField(max_length=1000)
    perception = models.SmallIntegerField()
    willpower = models.SmallIntegerField()
    charisma = models.SmallIntegerField()
    memory = models.SmallIntegerField()
    intelligence = models.SmallIntegerField()
    graphic = models.ForeignKey('Evegraphics')
    shortdescription = models.CharField(max_length=500)
    
    class Meta:
        db_table = u'chrancestries'
        
    def __unicode__(self):
        return self.ancestryname

class Chrcareerskills(models.Model):
    """
    List of skills and levels for each Career. 
    """
    career = models.ForeignKey('Chrcareers')
    skilltype = models.ForeignKey('Invtypes')
    levels = models.SmallIntegerField()
    
    class Meta:
        db_table = u'chrcareerskills'
        
    def __unicode__(self):
        return '%s (%s)' % (self.skilltype.typename, 
                            self.career.careername)

class Chrattributes(models.Model):
    """
    Five base Attrinutes annotated. 
    """
    attributename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphic = models.ForeignKey('Evegraphics')
    shortdescription = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)
    
    class Meta:
        db_table = u'chrattributes'
        
    def __unicode__(self):
        return self.attributename

class Chrfactions(models.Model):
    """
    All main Factions found in game. 
    """
    factionname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    raceids = models.IntegerField()
    solarsystem = models.ForeignKey('Mapsolarsystems')
    corporation = models.ForeignKey('Crpnpccorporations')
    sizefactor = models.FloatField()
    stationcount = models.SmallIntegerField()
    stationsystemcount = models.SmallIntegerField()
    militiacorporation = models.ForeignKey('Crpnpccorporations', 
                                           related_name='militia_corp_set')
    class Meta:
        db_table = u'chrfactions'
        
    def __unicode__(self):
        return self.factionname

class Chrschools(models.Model):
    race = models.ForeignKey('Chrraces')
    schoolname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphic = models.ForeignKey('Evegraphics')
    corporation = models.ForeignKey('Crpnpccorporations', 
                                    related_name='chrschools_set')
    newagent = models.ForeignKey('Agtagents')
    career = models.ForeignKey('Chrcareers')
    
    class Meta:
        db_table = u'chrschools'
        
    def __unicode__(self):
        return self.schoolname

class Chrraceskills(models.Model):
    race = models.ForeignKey('Chrraces')
    skilltype = models.ForeignKey('Invtypes')
    levels = models.SmallIntegerField()
    
    class Meta:
        db_table = u'chrraceskills'
        
    def __unicode__(self):
        return "%s (%s)" % (self.skilltype.typename, self.race.racename)

class Chrcareerspecialityskills(models.Model):
    speciality = models.ForeignKey('Chrcareerspecialities')
    skilltype = models.ForeignKey('Invtypes')
    levels = models.SmallIntegerField()
    
    class Meta:
        db_table = u'chrcareerspecialityskills'
        
    def __unicode__(self):
        return "%s (%s)" % (self.skilltype.typename, self.speciality.specialityname)

class Chrschoolagents(models.Model):
    school = models.ForeignKey('Chrschools')
    agentindex = models.SmallIntegerField()
    agent = models.ForeignKey('Agtagents')
    
    class Meta:
        db_table = u'chrschoolagents'
        
    def __unicode__(self):
        return "%s (%s)" % (self.agent, self.school)
        

class Crpactivities(models.Model):
    activityname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    
    class Meta:
        db_table = u'crpactivities'
        
    def __unicode__(self):
        return self.activityname

class Agtconfig(models.Model):
    # TODO: condense this into agtagents?
    agent = models.ForeignKey('Agtagents')
    k = models.CharField(max_length=50)
    v = models.CharField(max_length=4000)
    
    class Meta:
        db_table = u'agtconfig'
        
    def __unicode__(self):
        return "%s (%s %s)" % (self.agent, self.k, self.v)

class Agtresearchagents(models.Model):
    agent = models.ForeignKey('Agtagents')
    type = models.ForeignKey('Invtypes')
    
    class Meta:
        db_table = u'agtresearchagents'
        
    def __unicode__(self):
        return "%s (%s)" % (self.agent, self.type)

class Crpnpccorporationdivisions(models.Model):
    corporation = models.ForeignKey('Crpnpccorporations')
    division = models.ForeignKey('Crpnpcdivisions')
    size = models.SmallIntegerField()
    
    class Meta:
        db_table = u'crpnpccorporationdivisions'
        
    def __unicode__(self):
        return "%s (%s)" % (self.division, self.corporation)

class Chrcareerspecialities(models.Model):
    career = models.ForeignKey('Chrcareers')
    specialityname = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    shortdescription = models.CharField(max_length=500)
    graphic = models.ForeignKey('Evegraphics')
    
    class Meta:
        db_table = u'chrcareerspecialities'
        
    def __unicode__(self):
        return "%s (%s)" % (self.specialityname, self.career)

class Chrcareers(models.Model):
    race = models.ForeignKey('Chrraces')
    careername = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    shortdescription = models.CharField(max_length=500)
    graphic = models.ForeignKey('Evegraphics')
    school = models.ForeignKey('Chrschools')
    
    class Meta:
        db_table = u'chrcareers'
        
    def __unicode__(self):
        return self.careername

class Crpnpccorporationresearchfields(models.Model):
    skill = models.ForeignKey('Invtypes')
    corporation = models.ForeignKey('Crpnpccorporations')
    
    class Meta:
        db_table = u'crpnpccorporationresearchfields'
        
    def __unicode__(self):
        return "%s (%s)" % (self.skill, self.corporation)

class Crtrelationships(models.Model):
    parent = models.ForeignKey('Crtcertificates')
    parenttype = models.ForeignKey('Invtypes')
    parentlevel = models.SmallIntegerField()
    child = models.ForeignKey('Crtcertificates',
                                related_name='relationships_set')
    class Meta:
        db_table = u'crtrelationships'
        
    def __unicode__(self):
        return "%s %s %s -> %s" % (self.parent, self.parenttype, self.parentlevel,
                                self.child)

class Invcategories(models.Model):
    categoryname = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    graphic = models.ForeignKey('Evegraphics')
    published = models.SmallIntegerField()
    
    class Meta:
        db_table = u'invcategories'
        
    def __unicode__(self):
        return self.categoryname

class Dgmtypeeffects(models.Model):
    type = models.ForeignKey('Invtypes')
    effect = models.ForeignKey('Dgmeffects')
    isdefault = models.SmallIntegerField()
    
    class Meta:
        db_table = u'dgmtypeeffects'
        
    def __unicode__(self):
        return self.type.typename

class Dgmtypeattributes(models.Model):
    type = models.ForeignKey('Invtypes')
    attribute = models.ForeignKey('Dgmattributetypes')
    valueint = models.IntegerField()
    valuefloat = models.FloatField()
    
    class Meta:
        db_table = u'dgmtypeattributes'
        
    def __unicode__(self):
        return self.type.typename

class Invmarketgroups(models.Model):
    parentgroup = models.ForeignKey('self')
    marketgroupname = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    graphic = models.ForeignKey('Evegraphics')
    hastypes = models.SmallIntegerField()
    
    class Meta:
        db_table = u'invmarketgroups'
        
    def __unicode__(self):
        return self.marketgroupname

class Crpnpcdivisions(models.Model):
    divisionname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    leadertype = models.CharField(max_length=100)
    
    class Meta:
        db_table = u'crpnpcdivisions'
        
    def __unicode__(self):
        return self.divisionname

class Invblueprinttypes(models.Model):
    blueprinttype = models.ForeignKey('Invtypes')
    parentblueprinttype = models.ForeignKey('Invtypes', 
                                      related_name='parent_blueprint_type_set')
    producttype = models.ForeignKey('Invtypes',
                                      related_name='blueprint_types_set')
    productiontime = models.IntegerField()
    techlevel = models.SmallIntegerField()
    researchproductivitytime = models.IntegerField()
    researchmaterialtime = models.IntegerField()
    researchcopytime = models.IntegerField()
    researchtechtime = models.IntegerField()
    productivitymodifier = models.IntegerField()
    materialmodifier = models.SmallIntegerField()
    wastefactor = models.SmallIntegerField()
    chanceofreverseengineering = models.FloatField()
    maxproductionlimit = models.IntegerField()
    
    class Meta:
        db_table = u'invblueprinttypes'
        
    def __unicode__(self):
        return self.blueprinttype.typename

class Invmetatypes(models.Model):
    type = models.ForeignKey('Invtypes')
    parenttype = models.ForeignKey('Invtypes', related_name='meta_types_set')
    metagroup = models.ForeignKey('Invmetagroups')
    
    class Meta:
        db_table = u'invmetatypes'
        
    def __unicode__(self):
        return self.type.typename

class Invflags(models.Model):
    flagname = models.CharField(max_length=100)
    flagtext = models.CharField(max_length=100)
    flagtype = models.CharField(max_length=20)
    orderid = models.SmallIntegerField()
    
    class Meta:
        db_table = u'invflags'
        
    def __unicode__(self):
        return self.flagname

class Invcontrabandtypes(models.Model):
    faction = models.ForeignKey('Chrfactions')
    type = models.ForeignKey('Invtypes')
    standingloss = models.FloatField()
    confiscateminsec = models.FloatField()
    finebyvalue = models.FloatField()
    attackminsec = models.FloatField()
    
    class Meta:
        db_table = u'invcontrabandtypes'
        
    def __unicode__(self):
        return self.type.typename

class Evegraphics(models.Model):
    url3d = models.CharField(max_length=100)
    urlweb = models.CharField(max_length=100)
    description = models.TextField()
    published = models.SmallIntegerField()
    obsolete = models.SmallIntegerField()
    icon = models.CharField(max_length=100)
    urlsound = models.CharField(max_length=100)
    explosion = models.ForeignKey('self')
    
    class Meta:
        db_table = u'evegraphics'
        
    def __unicode__(self):
        return self.description

class Invtypereactions(models.Model):
    reactiontype = models.ForeignKey('Invtypes')
    input = models.SmallIntegerField()
    type = models.ForeignKey('Invtypes', related_name='type_reactions_set')
    quantity = models.SmallIntegerField()
    
    class Meta:
        db_table = u'invtypereactions'
        
    def __unicode__(self):
        return self.reactiontype.typename

class Eveunits(models.Model):
    unitname = models.CharField(max_length=100)
    displayname = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    
    class Meta:
        db_table = u'eveunits'
        
    def __unicode__(self):
        return self.unitname

class Dgmattributecategories(models.Model):
    categoryname = models.CharField(max_length=50)
    categorydescription = models.CharField(max_length=200)
    
    class Meta:
        db_table = u'dgmattributecategories'
        
    def __unicode__(self):
        return self.categoryname

class Crtcertificates(models.Model):
    category = models.ForeignKey('Crtcategories')
    crtclass = models.ForeignKey('Crtclasses')
    grade = models.SmallIntegerField()
    corp = models.ForeignKey('Crpnpccorporations')
    iconid = models.SmallIntegerField()
    description = models.CharField(max_length=500)
    
    class Meta:
        db_table = u'crtcertificates'
        
    def __unicode__(self):
        return self.crtclass.classname

class Dgmattributetypes(models.Model):
    attributename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphic = models.ForeignKey('Evegraphics')
    defaultvalue = models.FloatField()
    published = models.SmallIntegerField()
    displayname = models.CharField(max_length=100)
    unit = models.ForeignKey('Eveunits')
    stackable = models.SmallIntegerField()
    highisgood = models.SmallIntegerField()
    category = models.ForeignKey('Dgmattributecategories')
    
    class Meta:
        db_table = u'dgmattributetypes'
        
    def __unicode__(self):
        return self.attributename

class Dgmeffects(models.Model):
    effectname = models.CharField(max_length=400)
    effectcategory = models.SmallIntegerField()
    preexpression = models.IntegerField()
    postexpression = models.IntegerField()
    description = models.CharField(max_length=1000)
    guid = models.CharField(max_length=60)
    graphic = models.ForeignKey('Evegraphics')
    isoffensive = models.SmallIntegerField()
    isassistance = models.SmallIntegerField()
    durationattribute = models.ForeignKey('Dgmattributetypes', 
                                        related_name='duration_dmgeffects_set')
    trackingspeedattribute = models.ForeignKey('Dgmattributetypes', 
                                        related_name='trackingspeed_dmgeffects_set')
    dischargeattribute = models.ForeignKey('Dgmattributetypes', 
                                        related_name='discharge_dmgeffects_set')
    rangeattribute = models.ForeignKey('Dgmattributetypes', 
                                        related_name='range_dmgeffects_set')
    falloffattribute = models.ForeignKey('Dgmattributetypes', 
                                        related_name='falloff_dmgeffects_set')
    disallowautorepeat = models.SmallIntegerField()
    published = models.SmallIntegerField()
    displayname = models.CharField(max_length=100)
    iswarpsafe = models.SmallIntegerField()
    rangechance = models.SmallIntegerField()
    electronicchance = models.SmallIntegerField()
    propulsionchance = models.SmallIntegerField()
    distribution = models.SmallIntegerField()
    sfxname = models.CharField(max_length=20)
    npcusagechanceattribute = models.ForeignKey('Dgmattributetypes', 
                                        related_name='npcusage_chance_set')
    npcactivationchanceattribute = models.ForeignKey('Dgmattributetypes', 
                                    related_name='npcactivation_chance_set')
    fittingusagechanceattribute = models.ForeignKey('Dgmattributetypes', 
                                    related_name='fittingusage_chance_set')
    
    class Meta:
        db_table = u'dgmeffects'
        
    def __unicode__(self):
        return self.effectname

class Invcontroltowerresources(models.Model):
    controltowertype = models.ForeignKey('Invtypes')
    resourcetype = models.ForeignKey('Invtypes',
                                       related_name='controltower_resource_set')
    purpose = models.ForeignKey('Invcontroltowerresourcepurposes')
    quantity = models.IntegerField()
    minsecuritylevel = models.FloatField()
    faction = models.ForeignKey('Chrfactions')
    
    class Meta:
        db_table = u'invcontroltowerresources'
        
    def __unicode__(self):
        return "%s (%s)" % (self.resourcetype.typename,
                            self.controltowertype.typename)

class Invmetagroups(models.Model):
    metagroupname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphic = models.ForeignKey('Evegraphics')
    
    class Meta:
        db_table = u'invmetagroups'
        
    def __unicode__(self):
        return self.metagroupname

class Invcontroltowerresourcepurposes(models.Model):
    purposetext = models.CharField(max_length=100)
    
    class Meta:
        db_table = u'invcontroltowerresourcepurposes'
        
    def __unicode__(self):
        return self.purposetext

class Invgroups(models.Model):
    category = models.ForeignKey('Invcategories')
    groupname = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    graphic = models.ForeignKey('Evegraphics')
    usebaseprice = models.SmallIntegerField()
    allowmanufacture = models.SmallIntegerField()
    allowrecycler = models.SmallIntegerField()
    anchored = models.SmallIntegerField()
    anchorable = models.SmallIntegerField()
    fittablenonsingleton = models.SmallIntegerField()
    published = models.SmallIntegerField()
    
    class Meta:
        db_table = u'invgroups'
        
    def __unicode__(self):
        return self.groupname

class Maplandmarks(models.Model):
    landmarkname = models.CharField(max_length=100)
    description = models.CharField(max_length=7000)
    location = models.ForeignKey('Mapsolarsystems')
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    radius = models.FloatField()
    graphic = models.ForeignKey('Evegraphics')
    importance = models.SmallIntegerField()
    url2d = models.CharField(max_length=255)
    
    class Meta:
        db_table = u'maplandmarks'
        
    def __unicode__(self):
        return self.landmarkname

class Mapuniverse(models.Model):
    universename = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    xmin = models.FloatField(db_column='xMin') # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax') # Field name made lowercase.
    ymin = models.FloatField()
    ymax = models.FloatField()
    zmin = models.FloatField()
    zmax = models.FloatField()
    radius = models.FloatField()
    
    class Meta:
        db_table = u'mapuniverse'
        
    def __unicode__(self):
        return self.universename

class Ramassemblylines(models.Model):
    assemblylinetype = models.ForeignKey('Ramassemblylinetypes', 
                                           related_name='assemble_lines_set')
    container = models.ForeignKey('Stastations')
    nextfreetime = models.DateTimeField()
    uigroupingid = models.SmallIntegerField()
    costinstall = models.FloatField()
    costperhour = models.FloatField()
    restrictionmask = models.SmallIntegerField()
    discountpergoodstandingpoint = models.FloatField()
    surchargeperbadstandingpoint = models.FloatField()
    minimumstanding = models.FloatField()
    minimumcharsecurity = models.FloatField()
    minimumcorpsecurity = models.FloatField()
    maximumcharsecurity = models.FloatField()
    maximumcorpsecurity = models.FloatField()
    owner = models.ForeignKey('Crpnpccorporations')
    activity = models.ForeignKey('Ramactivities')
    
    class Meta:
        db_table = u'ramassemblylines'
        
    def __unicode__(self):
        return self.assemblylinetype.assemblylinetypename

class Ramassemblylinetypes(models.Model):
    assemblylinetypename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    basetimemultiplier = models.FloatField()
    basematerialmultiplier = models.FloatField()
    volume = models.FloatField()
    activity = models.ForeignKey('Ramactivities')
    mincostperhour = models.FloatField()
    
    class Meta:
        db_table = u'ramassemblylinetypes'
        
    def __unicode__(self):
        return self.assemblylinetypename

class Staoperationservices(models.Model):
    operation = models.ForeignKey('Staoperations')
    service = models.ForeignKey('Staservices')
    
    class Meta:
        db_table = u'staoperationservices'
        
    def __unicode__(self):
        return "%s %s" % (self.operation, self.service)

class Stastationtypes(models.Model):
    stationtype = models.ForeignKey('Invtypes')
    dockingbaygraphic = models.ForeignKey('Evegraphics')
    hangargraphic = models.ForeignKey('Evegraphics', 
                                        related_name='station_types_set')
    dockentryx = models.FloatField()
    dockentryy = models.FloatField()
    dockentryz = models.FloatField()
    dockorientationx = models.FloatField()
    dockorientationy = models.FloatField()
    dockorientationz = models.FloatField()
    operation = models.ForeignKey('Staoperations')
    officeslots = models.SmallIntegerField()
    reprocessingefficiency = models.FloatField()
    conquerable = models.SmallIntegerField()
    
    class Meta:
        db_table = u'stastationtypes'
        
    def __unicode__(self):
        return self.stationtype.typename

class Mapcelestialstatistics(models.Model):
    celestial = models.ForeignKey('Mapdenormalize', 
                                  related_name='celestial_statistics_set')
    temperature = models.FloatField()
    spectralclass = models.CharField(max_length=10)
    luminosity = models.FloatField()
    age = models.FloatField()
    life = models.FloatField()
    orbitradius = models.FloatField()
    eccentricity = models.FloatField()
    massdust = models.FloatField()
    massgas = models.FloatField()
    fragmented = models.SmallIntegerField()
    density = models.FloatField()
    surfacegravity = models.FloatField()
    escapevelocity = models.FloatField()
    orbitperiod = models.FloatField()
    rotationrate = models.FloatField()
    locked = models.SmallIntegerField()
    pressure = models.FloatField()
    radius = models.FloatField()
    mass = models.FloatField()
    
    class Meta:
        db_table = u'mapcelestialstatistics'
        
    def __unicode__(self):
        return self.celestial.type.typename

class Ramassemblylinestations(models.Model):
    station = models.ForeignKey('Stastations')
    assemblylinetype = models.ForeignKey('Ramassemblylinetypes')
    quantity = models.SmallIntegerField()
    stationtype = models.ForeignKey('Invtypes')
    owner = models.ForeignKey('Crpnpccorporations')
    solarsystem = models.ForeignKey('Mapsolarsystems')
    region = models.ForeignKey('Mapregions')
    
    class Meta:
        db_table = u'ramassemblylinestations'
        
    def __unicode__(self):
        return self.station.stationname

class Mapregionjumps(models.Model):
    fromregion = models.ForeignKey('Mapregions',
                                   related_name='from_region_jump_set')
    toregion = models.ForeignKey('Mapregions',
                                 related_name='to_region_jumps_set')
    
    class Meta:
        db_table = u'mapregionjumps'
        
    def __unicode__(self):
        return "%s -> %s" % (self.fromregion.regionname, 
                             self.toregion.regionname)

class Mapconstellationjumps(models.Model):
    # TODO: Is this supposed to be a FK?
    fromregion_id = models.IntegerField()
    fromconstellation = models.ForeignKey('Mapconstellations', 
                                          related_name='from_constellation_jumps_set')
    toconstellation = models.ForeignKey('Mapconstellations', 
                                        related_name='to_constellation_jumps_set')
    toregionid = models.IntegerField()
    
    class Meta:
        db_table = u'mapconstellationjumps'
        
    def __unicode__(self):
        return "%s -> %s" % (self.fromconstellation.constellationname,
                             self.toconstellation.constellationname)

class Ramassemblylinetypedetailpercategory(models.Model):
    assemblylinetype = models.ForeignKey('Ramassemblylinetypes')
    category = models.ForeignKey('Invcategories')
    timemultiplier = models.FloatField()
    materialmultiplier = models.FloatField()
    
    class Meta:
        db_table = u'ramassemblylinetypedetailpercategory'
        
    def __unicode__(self):
        return self.assemblylinetype.assemblylinetypename

class Mapjumps(models.Model):
    stargate = models.ForeignKey('Mapdenormalize',
                                 related_name='stargate_mapjumps_set')
    celestial = models.ForeignKey('Mapdenormalize',
                                  related_name='celestial_mapjumps_set')
    class Meta:
        db_table = u'mapjumps'

    def __unicode__(self):
        return self.stargate.type.typename

class Mapsolarsystemjumps(models.Model):
    # TODO: Is this supposed to be a FK?
    fromregion_id = models.IntegerField()
    # TODO: Is this supposed to be a FK?
    fromconstellation_id = models.IntegerField()
    fromsolarsystem = models.ForeignKey('Mapsolarsystems', 
                                        related_name='from_solarsystem_set')
    tosolarsystem = models.ForeignKey('Mapsolarsystems', 
                                      related_name='to_solarsystem_set')
    # TODO: Is this supposed to be a FK?
    toconstellation_id = models.IntegerField()
    # TODO: Is this supposed to be a FK?
    toregion_id = models.IntegerField()
    
    class Meta:
        db_table = u'mapsolarsystemjumps'
        
    def __unicode__(self):
        return "%s -> %s" % (self.fromsolarsystem.solarsystemname,
                             self.tosolarsystem.solarsystemname)

class Ramassemblylinetypedetailpergroup(models.Model):
    assemblylinetype = models.ForeignKey('Ramassemblylinetypes')
    group = models.ForeignKey('Invgroups')
    timemultiplier = models.FloatField()
    materialmultiplier = models.FloatField()
    
    class Meta:
        db_table = u'ramassemblylinetypedetailpergroup'
        
    def __unicode__(self):
        return "%s (%s)" % (self.assemblylinetype.assemblylinetypename,
                            self.group.groupname)

class Mapsolarsystems(models.Model):
    region = models.ForeignKey('Mapregions')
    constellation = models.ForeignKey('Mapconstellations')
    solarsystemname = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    xmin = models.FloatField(db_column='xMin') # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax') # Field name made lowercase.
    ymin = models.FloatField()
    ymax = models.FloatField()
    zmin = models.FloatField()
    zmax = models.FloatField()
    luminosity = models.FloatField()
    border = models.SmallIntegerField()
    fringe = models.SmallIntegerField()
    corridor = models.SmallIntegerField()
    hub = models.SmallIntegerField()
    international = models.SmallIntegerField()
    regional = models.SmallIntegerField()
    constellation = models.SmallIntegerField()
    security = models.FloatField()
    faction = models.ForeignKey('Chrfactions')
    radius = models.FloatField()
    suntype = models.ForeignKey('Invtypes')
    securityclass = models.CharField(max_length=2)
    
    class Meta:
        db_table = u'mapsolarsystems'
        
    def __unicode__(self):
        return self.solarsystemname

class Staservices(models.Model):
    servicename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    
    class Meta:
        db_table = u'staservices'
        
    def __unicode__(self):
        return self.servicename

class Typeactivitymaterials(models.Model):
    type = models.ForeignKey('Invtypes', related_name='activity_materials_set')
    activity = models.ForeignKey('Ramactivities')
    requiredtype = models.ForeignKey('Invtypes', 
                                     related_name='required_type_set')
    quantity = models.IntegerField()
    damageperjob = models.FloatField()
    recycle = models.SmallIntegerField()
    
    class Meta:
        db_table = u'typeactivitymaterials'
        
    def __unicode__(self):
        return self.type.typename

class Mapregions(models.Model):
    regionname = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    xmin = models.FloatField(db_column='xMin') # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax') # Field name made lowercase.
    ymin = models.FloatField()
    ymax = models.FloatField()
    zmin = models.FloatField()
    zmax = models.FloatField()
    faction = models.ForeignKey('Chrfactions')
    radius = models.FloatField()
    
    class Meta:
        db_table = u'mapregions'
        
    def __unicode__(self):
        return self.regionname

class Ramactivities(models.Model):
    activityname = models.CharField(max_length=100)
    iconno = models.CharField(max_length=5)
    description = models.CharField(max_length=1000)
    published = models.SmallIntegerField()
    
    class Meta:
        db_table = u'ramactivities'
        
    def __unicode__(self):
        return self.activityname

class Staoperations(models.Model):
    activity = models.ForeignKey('Crpactivities')
    operationname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    fringe = models.SmallIntegerField()
    corridor = models.SmallIntegerField()
    hub = models.SmallIntegerField()
    border = models.SmallIntegerField()
    ratio = models.SmallIntegerField()
    caldaristationtype = models.ForeignKey('Stastationtypes', 
                                           related_name='caldari_station_set')
    minmatarstationtype = models.ForeignKey('Stastationtypes', 
                                            related_name='minmatar_station_set')
    amarrstationtype = models.ForeignKey('Stastationtypes', 
                                         related_name='amarr_station_set')
    gallentestationtype = models.ForeignKey('Stastationtypes', 
                                            related_name='gallente_station_set')
    jovestationtype = models.ForeignKey('Stastationtypes', 
                                        related_name='jove_station_set')
    class Meta:
        db_table = u'staoperations'
        
    def __unicode__(self):
        return self.operationname

class Agtagenttypes(models.Model):
    agenttype = models.CharField(max_length=50)
    
    class Meta:
        db_table = u'agtagenttypes'
        
    def __unicode__(self):
        return self.agenttype

class Crpnpccorporations(models.Model):
    size = models.CharField(max_length=1)
    extent = models.CharField(max_length=1)
    solarsystem = models.ForeignKey('Mapsolarsystems')
    investor1 = models.ForeignKey('self', related_name='investor1_set')
    investorshares1 = models.SmallIntegerField()
    investor2 = models.ForeignKey('self', related_name='investor2_set')
    investorshares2 = models.SmallIntegerField()
    investor3 = models.ForeignKey('self', related_name='investor3_set')
    investorshares3 = models.SmallIntegerField()
    investor4 = models.ForeignKey('self', related_name='investor4_set')
    investorshares4 = models.SmallIntegerField()
    friend = models.ForeignKey('self', related_name='friend_set')
    enemy = models.ForeignKey('self', related_name='enemy_set')
    publicshares = models.TextField() # This field type is a guess.
    initialprice = models.IntegerField()
    minsecurity = models.FloatField()
    scattered = models.SmallIntegerField()
    fringe = models.SmallIntegerField()
    corridor = models.SmallIntegerField()
    hub = models.SmallIntegerField()
    border = models.SmallIntegerField()
    faction = models.ForeignKey('Chrfactions')
    sizefactor = models.FloatField()
    stationcount = models.SmallIntegerField()
    stationsystemcount = models.SmallIntegerField()
    
    class Meta:
        db_table = u'crpnpccorporations'
        
    def __unicode__(self):
        return "Corp %s" % (self.id)

class Agtagents(models.Model):
    agent = models.ForeignKey('Evenames')
    division = models.ForeignKey('Crpnpcdivisions')
    corporation = models.ForeignKey('Crpnpccorporations')
    station = models.ForeignKey('Stastations')
    level = models.SmallIntegerField()
    quality = models.SmallIntegerField()
    agenttype = models.ForeignKey('Agtagenttypes')

    class Meta:
        db_table = u'agtagents'
        
    def __unicode__(self):
        return self.agent.itemname

class Crtcategories(models.Model):
    description = models.CharField(max_length=500)
    categoryname = models.CharField(max_length=256)
    
    class Meta:
        db_table = u'crtcategories'
        
    def __unicode__(self):
        return self.categoryname

class Crtclasses(models.Model):
    description = models.CharField(max_length=500)
    classname = models.CharField(max_length=256)
    
    class Meta:
        db_table = u'crtclasses'

    def __unicode__(self):
        return self.classname

class Stastations(models.Model):
    security = models.SmallIntegerField()
    dockingcostpervolume = models.FloatField()
    maxshipvolumedockable = models.FloatField()
    officerentalcost = models.IntegerField()
    operation = models.ForeignKey('Staoperations')
    stationtype = models.ForeignKey('Stastationtypes')
    corporation = models.ForeignKey('Crpnpccorporations')
    solarsystem = models.ForeignKey('Mapsolarsystems')
    # TODO: FK?
    constellation_id = models.IntegerField()
    # TODO: FK?
    region_id = models.IntegerField()
    stationname = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    reprocessingefficiency = models.FloatField()
    reprocessingstationstake = models.FloatField()
    reprocessinghangarflag = models.SmallIntegerField()
    
    class Meta:
        db_table = u'stastations'
        
    def __unicode__(self):
        return self.stationname

class Invtypes(models.Model):
    group = models.ForeignKey('Invgroups')
    typename = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    graphic = models.ForeignKey('Evegraphics')
    radius = models.FloatField()
    mass = models.FloatField()
    volume = models.FloatField()
    capacity = models.FloatField()
    portionsize = models.IntegerField()
    race = models.ForeignKey('Chrraces')
    baseprice = models.FloatField()
    published = models.SmallIntegerField()
    marketgroup = models.ForeignKey('Invmarketgroups')
    chanceofduplicating = models.FloatField()
    
    class Meta:
        db_table = u'invtypes'
        
    def __unicode__(self):
        return self.typename

class Mapdenormalize(models.Model):
    type = models.ForeignKey('Invtypes', related_name='denormalize_set')
    group = models.ForeignKey('Invgroups')
    solarsystem = models.ForeignKey('Mapsolarsystems')
    constellation = models.ForeignKey('Mapconstellations')
    region = models.ForeignKey('Mapregions')
    orbit = models.ForeignKey('self')
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    radius = models.FloatField()
    itemname = models.CharField(max_length=100)
    security = models.FloatField()
    celestialindex = models.SmallIntegerField()
    orbitindex = models.SmallIntegerField()
    
    class Meta:
        db_table = u'mapdenormalize'
        
    def __unicode__(self):
        return self.type.typename

class Chrraces(models.Model):
    racename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphic = models.ForeignKey('Evegraphics')
    shortdescription = models.CharField(max_length=500)
    
    class Meta:
        db_table = u'chrraces'
        
    def __unicode__(self):
        return self.racename

class Evenames(models.Model):
    itemname = models.CharField(max_length=100)
    category = models.ForeignKey('Invcategories')
    group = models.ForeignKey('Invgroups')
    type = models.ForeignKey('Invtypes')
    
    class Meta:
        db_table = u'evenames'
        
    def __unicode__(self):
        return self.itemname

class Mapconstellations(models.Model):
    region = models.ForeignKey('Mapregions')
    constellationname = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    xmin = models.FloatField(db_column='xMin') # Field name made lowercase.
    xmax = models.FloatField(db_column='xMax') # Field name made lowercase.
    ymin = models.FloatField()
    ymax = models.FloatField()
    zmin = models.FloatField()
    zmax = models.FloatField()
    faction = models.ForeignKey('Chrfactions')
    radius = models.FloatField()
    
    class Meta:
        db_table = u'mapconstellations'
    
    def __unicode__(self):
        return self.constellationname