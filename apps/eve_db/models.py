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
    bloodlineid = models.SmallIntegerField(primary_key=True)
    bloodlinename = models.CharField(max_length=100)
    raceid = models.ForeignKey('Chrraces', db_column='raceid')
    description = models.CharField(max_length=1000)
    maledescription = models.CharField(max_length=1000)
    femaledescription = models.CharField(max_length=1000)
    shiptypeid = models.ForeignKey('Invtypes', db_column='shiptypeid')
    corporationid = models.ForeignKey('Crpnpccorporations', db_column='corporationid')
    perception = models.SmallIntegerField()
    willpower = models.SmallIntegerField()
    charisma = models.SmallIntegerField()
    memory = models.SmallIntegerField()
    intelligence = models.SmallIntegerField()
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    shortdescription = models.CharField(max_length=500)
    shortmaledescription = models.CharField(max_length=500)
    shortfemaledescription = models.CharField(max_length=500)
    class Meta:
        db_table = u'chrbloodlines'

class Chrancestries(models.Model):
    ancestryid = models.SmallIntegerField(primary_key=True)
    ancestryname = models.CharField(max_length=100)
    bloodlineid = models.ForeignKey('Chrbloodlines', db_column='bloodlineid')
    description = models.CharField(max_length=1000)
    perception = models.SmallIntegerField()
    willpower = models.SmallIntegerField()
    charisma = models.SmallIntegerField()
    memory = models.SmallIntegerField()
    intelligence = models.SmallIntegerField()
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    shortdescription = models.CharField(max_length=500)
    class Meta:
        db_table = u'chrancestries'

class Chrcareerskills(models.Model):
    careerid = models.ForeignKey('Chrcareers', db_column='careerid')
    skilltypeid = models.ForeignKey('Invtypes', db_column='skilltypeid')
    levels = models.SmallIntegerField()
    class Meta:
        db_table = u'chrcareerskills'

class Chrattributes(models.Model):
    attributeid = models.SmallIntegerField(primary_key=True)
    attributename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    shortdescription = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)
    class Meta:
        db_table = u'chrattributes'

class Chrfactions(models.Model):
    factionid = models.IntegerField(primary_key=True)
    factionname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    raceids = models.IntegerField()
    solarsystemid = models.ForeignKey('Mapsolarsystems', db_column='solarsystemid')
    corporationid = models.ForeignKey('Crpnpccorporations', db_column='corporationid')
    sizefactor = models.FloatField()
    stationcount = models.SmallIntegerField()
    stationsystemcount = models.SmallIntegerField()
    militiacorporationid = models.ForeignKey('Crpnpccorporations', 
                                             db_column='militiacorporationid',
                                             related_name='militia_corp_set')
    class Meta:
        db_table = u'chrfactions'

class Chrschools(models.Model):
    raceid = models.ForeignKey('Chrraces', db_column='raceid')
    schoolid = models.SmallIntegerField(primary_key=True)
    schoolname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    corporationid = models.ForeignKey('Crpnpccorporations', 
                                      db_column='corporationid',
                                      related_name='chrschools_set')
    newagentid = models.ForeignKey('Agtagents', db_column='newagentid')
    careerid = models.ForeignKey('Chrcareers', db_column='careerid')
    class Meta:
        db_table = u'chrschools'

class Chrraceskills(models.Model):
    raceid = models.ForeignKey('Chrraces', db_column='raceid')
    skilltypeid = models.ForeignKey('Invtypes', db_column='skilltypeid')
    levels = models.SmallIntegerField()
    class Meta:
        db_table = u'chrraceskills'

class Chrcareerspecialityskills(models.Model):
    specialityid = models.ForeignKey('Chrcareerspecialities', db_column='specialityid')
    skilltypeid = models.ForeignKey('Invtypes', db_column='skilltypeid')
    levels = models.SmallIntegerField()
    class Meta:
        db_table = u'chrcareerspecialityskills'

class Chrschoolagents(models.Model):
    schoolid = models.ForeignKey('Chrschools', db_column='schoolid')
    agentindex = models.SmallIntegerField()
    agentid = models.ForeignKey('Agtagents', db_column='agentid')
    class Meta:
        db_table = u'chrschoolagents'

class Crpactivities(models.Model):
    activityid = models.SmallIntegerField(primary_key=True)
    activityname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    class Meta:
        db_table = u'crpactivities'

class Agtconfig(models.Model):
    agentid = models.ForeignKey('Agtagents', db_column='agentid')
    k = models.CharField(max_length=50)
    v = models.CharField(max_length=4000)
    class Meta:
        db_table = u'agtconfig'

class Agtresearchagents(models.Model):
    agentid = models.ForeignKey('Agtagents', db_column='agentid')
    typeid = models.ForeignKey('Invtypes', db_column='typeid')
    class Meta:
        db_table = u'agtresearchagents'

class Crpnpccorporationdivisions(models.Model):
    corporationid = models.ForeignKey('Crpnpccorporations', db_column='corporationid')
    divisionid = models.ForeignKey('Crpnpcdivisions', db_column='divisionid')
    size = models.SmallIntegerField()
    class Meta:
        db_table = u'crpnpccorporationdivisions'

class Chrcareerspecialities(models.Model):
    specialityid = models.SmallIntegerField(primary_key=True)
    careerid = models.ForeignKey('Chrcareers', db_column='careerid')
    specialityname = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    shortdescription = models.CharField(max_length=500)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    class Meta:
        db_table = u'chrcareerspecialities'

class Chrcareers(models.Model):
    raceid = models.ForeignKey('Chrraces', db_column='raceid')
    careerid = models.SmallIntegerField(primary_key=True)
    careername = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    shortdescription = models.CharField(max_length=500)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    schoolid = models.ForeignKey('Chrschools', db_column='schoolid')
    class Meta:
        db_table = u'chrcareers'

class Crpnpccorporationresearchfields(models.Model):
    skillid = models.ForeignKey('Invtypes', db_column='skillid')
    corporationid = models.ForeignKey('Crpnpccorporations', db_column='corporationid')
    class Meta:
        db_table = u'crpnpccorporationresearchfields'

class Crtrelationships(models.Model):
    relationshipid = models.SmallIntegerField(primary_key=True)
    parentid = models.ForeignKey('Crtcertificates', db_column='parentid')
    parenttypeid = models.ForeignKey('Invtypes', db_column='parenttypeid')
    parentlevel = models.SmallIntegerField()
    childid = models.ForeignKey('Crtcertificates', db_column='childid',
                                related_name='relationships_set')
    class Meta:
        db_table = u'crtrelationships'

class Invcategories(models.Model):
    categoryid = models.SmallIntegerField(primary_key=True)
    categoryname = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    published = models.SmallIntegerField()
    class Meta:
        db_table = u'invcategories'

class Dgmtypeeffects(models.Model):
    typeid = models.ForeignKey('Invtypes', db_column='typeid')
    effectid = models.ForeignKey('Dgmeffects', db_column='effectid')
    isdefault = models.SmallIntegerField()
    class Meta:
        db_table = u'dgmtypeeffects'

class Dgmtypeattributes(models.Model):
    typeid = models.ForeignKey('Invtypes', db_column='typeid')
    attributeid = models.ForeignKey('Dgmattributetypes', db_column='attributeid')
    valueint = models.IntegerField()
    valuefloat = models.FloatField()
    class Meta:
        db_table = u'dgmtypeattributes'

class Invmarketgroups(models.Model):
    marketgroupid = models.SmallIntegerField(primary_key=True)
    parentgroupid = models.ForeignKey('self', db_column='parentgroupid')
    marketgroupname = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    hastypes = models.SmallIntegerField()
    class Meta:
        db_table = u'invmarketgroups'

class Crpnpcdivisions(models.Model):
    divisionid = models.SmallIntegerField(primary_key=True)
    divisionname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    leadertype = models.CharField(max_length=100)
    class Meta:
        db_table = u'crpnpcdivisions'

class Invblueprinttypes(models.Model):
    blueprinttypeid = models.ForeignKey('Invtypes', db_column='blueprinttypeid')
    parentblueprinttypeid = models.ForeignKey('Invtypes', 
                                              db_column='parentblueprinttypeid',
                                              related_name='parent_blueprint_type_set')
    producttypeid = models.ForeignKey('Invtypes', db_column='producttypeid',
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

class Invmetatypes(models.Model):
    typeid = models.ForeignKey('Invtypes', db_column='typeid')
    parenttypeid = models.ForeignKey('Invtypes', db_column='parenttypeid',
                                     related_name='meta_types_set')
    metagroupid = models.ForeignKey('Invmetagroups', db_column='metagroupid')
    class Meta:
        db_table = u'invmetatypes'

class Invflags(models.Model):
    flagid = models.SmallIntegerField(primary_key=True)
    flagname = models.CharField(max_length=100)
    flagtext = models.CharField(max_length=100)
    flagtype = models.CharField(max_length=20)
    orderid = models.SmallIntegerField()
    class Meta:
        db_table = u'invflags'

class Invcontrabandtypes(models.Model):
    factionid = models.ForeignKey('Chrfactions', db_column='factionid')
    typeid = models.ForeignKey('Invtypes', db_column='typeid')
    standingloss = models.FloatField()
    confiscateminsec = models.FloatField()
    finebyvalue = models.FloatField()
    attackminsec = models.FloatField()
    class Meta:
        db_table = u'invcontrabandtypes'

class Evegraphics(models.Model):
    graphicid = models.SmallIntegerField(primary_key=True)
    url3d = models.CharField(max_length=100)
    urlweb = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    published = models.SmallIntegerField()
    obsolete = models.SmallIntegerField()
    icon = models.CharField(max_length=100)
    urlsound = models.CharField(max_length=100)
    explosionid = models.ForeignKey('self', db_column='explosionid')
    class Meta:
        db_table = u'evegraphics'

class Invtypereactions(models.Model):
    reactiontypeid = models.ForeignKey('Invtypes', db_column='reactiontypeid')
    input = models.SmallIntegerField()
    typeid = models.ForeignKey('Invtypes', db_column='typeid',
                               related_name='type_reactions_set')
    quantity = models.SmallIntegerField()
    class Meta:
        db_table = u'invtypereactions'

class Eveunits(models.Model):
    unitid = models.SmallIntegerField(primary_key=True)
    unitname = models.CharField(max_length=100)
    displayname = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    class Meta:
        db_table = u'eveunits'

class Dgmattributecategories(models.Model):
    categoryid = models.SmallIntegerField(primary_key=True)
    categoryname = models.CharField(max_length=50)
    categorydescription = models.CharField(max_length=200)
    class Meta:
        db_table = u'dgmattributecategories'

class Crtcertificates(models.Model):
    certificateid = models.SmallIntegerField(primary_key=True)
    categoryid = models.ForeignKey('Crtcategories', db_column='categoryid')
    classid = models.ForeignKey('Crtclasses', db_column='classid')
    grade = models.SmallIntegerField()
    corpid = models.ForeignKey('Crpnpccorporations', db_column='corpid')
    iconid = models.SmallIntegerField()
    description = models.CharField(max_length=500)
    class Meta:
        db_table = u'crtcertificates'

class Dgmattributetypes(models.Model):
    attributeid = models.SmallIntegerField(primary_key=True)
    attributename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    defaultvalue = models.FloatField()
    published = models.SmallIntegerField()
    displayname = models.CharField(max_length=100)
    unitid = models.ForeignKey('Eveunits', db_column='unitid')
    stackable = models.SmallIntegerField()
    highisgood = models.SmallIntegerField()
    categoryid = models.ForeignKey('Dgmattributecategories', db_column='categoryid')
    class Meta:
        db_table = u'dgmattributetypes'

class Dgmeffects(models.Model):
    effectid = models.SmallIntegerField(primary_key=True)
    effectname = models.CharField(max_length=400)
    effectcategory = models.SmallIntegerField()
    preexpression = models.IntegerField()
    postexpression = models.IntegerField()
    description = models.CharField(max_length=1000)
    guid = models.CharField(max_length=60)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    isoffensive = models.SmallIntegerField()
    isassistance = models.SmallIntegerField()
    durationattributeid = models.ForeignKey('Dgmattributetypes', 
                                        db_column='durationattributeid',
                                        related_name='duration_dmgeffects_set')
    trackingspeedattributeid = models.ForeignKey('Dgmattributetypes', 
                                        db_column='trackingspeedattributeid',
                                        related_name='trackingspeed_dmgeffects_set')
    dischargeattributeid = models.ForeignKey('Dgmattributetypes', 
                                        db_column='dischargeattributeid',
                                        related_name='discharge_dmgeffects_set')
    rangeattributeid = models.ForeignKey('Dgmattributetypes', 
                                        db_column='rangeattributeid',
                                        related_name='range_dmgeffects_set')
    falloffattributeid = models.ForeignKey('Dgmattributetypes', 
                                        db_column='falloffattributeid',
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
    npcusagechanceattributeid = models.ForeignKey('Dgmattributetypes', 
                                        db_column='npcusagechanceattributeid',
                                        related_name='npcusage_chance_set')
    npcactivationchanceattributeid = models.ForeignKey('Dgmattributetypes', 
                                    db_column='npcactivationchanceattributeid',
                                    related_name='npcactivation_chance_set')
    fittingusagechanceattributeid = models.ForeignKey('Dgmattributetypes', 
                                    db_column='fittingusagechanceattributeid',
                                    related_name='fittingusage_chance_set')
    class Meta:
        db_table = u'dgmeffects'

class Invcontroltowerresources(models.Model):
    controltowertypeid = models.ForeignKey('Invtypes', db_column='controltowertypeid')
    resourcetypeid = models.ForeignKey('Invtypes', db_column='resourcetypeid',
                                       related_name='controltower_resource_set')
    purpose = models.ForeignKey('Invcontroltowerresourcepurposes', db_column='purpose')
    quantity = models.IntegerField()
    minsecuritylevel = models.FloatField()
    factionid = models.ForeignKey('Chrfactions', db_column='factionid')
    class Meta:
        db_table = u'invcontroltowerresources'

class Invmetagroups(models.Model):
    metagroupid = models.SmallIntegerField(primary_key=True)
    metagroupname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    class Meta:
        db_table = u'invmetagroups'

class Invcontroltowerresourcepurposes(models.Model):
    purpose = models.SmallIntegerField(primary_key=True)
    purposetext = models.CharField(max_length=100)
    class Meta:
        db_table = u'invcontroltowerresourcepurposes'

class Invgroups(models.Model):
    groupid = models.SmallIntegerField(primary_key=True)
    categoryid = models.ForeignKey('Invcategories', db_column='categoryid')
    groupname = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    usebaseprice = models.SmallIntegerField()
    allowmanufacture = models.SmallIntegerField()
    allowrecycler = models.SmallIntegerField()
    anchored = models.SmallIntegerField()
    anchorable = models.SmallIntegerField()
    fittablenonsingleton = models.SmallIntegerField()
    published = models.SmallIntegerField()
    class Meta:
        db_table = u'invgroups'

class Maplandmarks(models.Model):
    landmarkid = models.SmallIntegerField(primary_key=True)
    landmarkname = models.CharField(max_length=100)
    description = models.CharField(max_length=7000)
    locationid = models.ForeignKey('Mapsolarsystems', db_column='locationid')
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    radius = models.FloatField()
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    importance = models.SmallIntegerField()
    url2d = models.CharField(max_length=255)
    class Meta:
        db_table = u'maplandmarks'

class Mapuniverse(models.Model):
    universeid = models.IntegerField(primary_key=True)
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

class Ramassemblylines(models.Model):
    assemblylineid = models.IntegerField(primary_key=True)
    assemblylinetypeid = models.ForeignKey('Ramassemblylinetypes', 
                                           db_column='assemblylinetypeid',
                                           related_name='assemble_lines_set')
    containerid = models.ForeignKey('Stastations', db_column='containerid')
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
    ownerid = models.ForeignKey('Crpnpccorporations', db_column='ownerid')
    activityid = models.ForeignKey('Ramactivities', db_column='activityid')
    class Meta:
        db_table = u'ramassemblylines'

class Ramassemblylinetypes(models.Model):
    assemblylinetypeid = models.SmallIntegerField(primary_key=True)
    assemblylinetypename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    basetimemultiplier = models.FloatField()
    basematerialmultiplier = models.FloatField()
    volume = models.FloatField()
    activityid = models.ForeignKey('Ramactivities', db_column='activityid')
    mincostperhour = models.FloatField()
    class Meta:
        db_table = u'ramassemblylinetypes'

class Staoperationservices(models.Model):
    operationid = models.ForeignKey('Staoperations', db_column='operationid')
    serviceid = models.ForeignKey('Staservices', db_column='serviceid')
    class Meta:
        db_table = u'staoperationservices'

class Stastationtypes(models.Model):
    stationtypeid = models.ForeignKey('Invtypes', db_column='stationtypeid')
    dockingbaygraphicid = models.ForeignKey('Evegraphics', db_column='dockingbaygraphicid')
    hangargraphicid = models.ForeignKey('Evegraphics', 
                                        db_column='hangargraphicid',
                                        related_name='station_types_set')
    dockentryx = models.FloatField()
    dockentryy = models.FloatField()
    dockentryz = models.FloatField()
    dockorientationx = models.FloatField()
    dockorientationy = models.FloatField()
    dockorientationz = models.FloatField()
    operationid = models.ForeignKey('Staoperations', db_column='operationid')
    officeslots = models.SmallIntegerField()
    reprocessingefficiency = models.FloatField()
    conquerable = models.SmallIntegerField()
    class Meta:
        db_table = u'stastationtypes'

class Mapcelestialstatistics(models.Model):
    celestialid = models.ForeignKey('Mapdenormalize', 
                                    db_column='celestialid',
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

class Ramassemblylinestations(models.Model):
    stationid = models.ForeignKey('Stastations', db_column='stationid')
    assemblylinetypeid = models.ForeignKey('Ramassemblylinetypes', db_column='assemblylinetypeid')
    quantity = models.SmallIntegerField()
    stationtypeid = models.ForeignKey('Invtypes', db_column='stationtypeid')
    ownerid = models.ForeignKey('Crpnpccorporations', db_column='ownerid')
    solarsystemid = models.ForeignKey('Mapsolarsystems', db_column='solarsystemid')
    regionid = models.ForeignKey('Mapregions', db_column='regionid')
    class Meta:
        db_table = u'ramassemblylinestations'

class Mapregionjumps(models.Model):
    fromregionid = models.ForeignKey('Mapregions', db_column='fromregionid',
                                     related_name='from_region_jump_set')
    toregionid = models.ForeignKey('Mapregions', db_column='toregionid',
                                   related_name='to_region_jumps_set')
    class Meta:
        db_table = u'mapregionjumps'

class Mapconstellationjumps(models.Model):
    fromregionid = models.IntegerField()
    fromconstellationid = models.ForeignKey('Mapconstellations', 
                                            db_column='fromconstellationid',
                                            related_name='from_constellation_jumps_set')
    toconstellationid = models.ForeignKey('Mapconstellations', 
                                          db_column='toconstellationid',
                                          related_name='to_constellation_jumps_set')
    toregionid = models.IntegerField()
    class Meta:
        db_table = u'mapconstellationjumps'

class Ramassemblylinetypedetailpercategory(models.Model):
    assemblylinetypeid = models.ForeignKey('Ramassemblylinetypes', 
                                           db_column='assemblylinetypeid')
    categoryid = models.ForeignKey('Invcategories', db_column='categoryid')
    timemultiplier = models.FloatField()
    materialmultiplier = models.FloatField()
    class Meta:
        db_table = u'ramassemblylinetypedetailpercategory'

class Mapjumps(models.Model):
    stargateid = models.ForeignKey('Mapdenormalize', db_column='stargateid',
                                   related_name='stargate_mapjumps_set')
    celestialid = models.ForeignKey('Mapdenormalize', db_column='celestialid',
                                    related_name='celestial_mapjumps_set')
    class Meta:
        db_table = u'mapjumps'

class Mapsolarsystemjumps(models.Model):
    fromregionid = models.IntegerField()
    fromconstellationid = models.IntegerField()
    fromsolarsystemid = models.ForeignKey('Mapsolarsystems', 
                                          db_column='fromsolarsystemid',
                                          related_name='from_solarsystem_set')
    tosolarsystemid = models.ForeignKey('Mapsolarsystems', 
                                        db_column='tosolarsystemid',
                                        related_name='to_solarsystem_set')
    toconstellationid = models.IntegerField()
    toregionid = models.IntegerField()
    class Meta:
        db_table = u'mapsolarsystemjumps'

class Ramassemblylinetypedetailpergroup(models.Model):
    assemblylinetypeid = models.ForeignKey('Ramassemblylinetypes', db_column='assemblylinetypeid')
    groupid = models.ForeignKey('Invgroups', db_column='groupid')
    timemultiplier = models.FloatField()
    materialmultiplier = models.FloatField()
    class Meta:
        db_table = u'ramassemblylinetypedetailpergroup'

class Mapsolarsystems(models.Model):
    regionid = models.ForeignKey('Mapregions', db_column='regionid')
    constellationid = models.ForeignKey('Mapconstellations', db_column='constellationid')
    solarsystemid = models.IntegerField(primary_key=True)
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
    factionid = models.ForeignKey('Chrfactions', db_column='factionid')
    radius = models.FloatField()
    suntypeid = models.ForeignKey('Invtypes', db_column='suntypeid')
    securityclass = models.CharField(max_length=2)
    class Meta:
        db_table = u'mapsolarsystems'

class Staservices(models.Model):
    serviceid = models.IntegerField(primary_key=True)
    servicename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    class Meta:
        db_table = u'staservices'

class Typeactivitymaterials(models.Model):
    typeid = models.ForeignKey('Invtypes', db_column='typeid',
                               related_name='activity_materials_set')
    activityid = models.ForeignKey('Ramactivities', db_column='activityid')
    requiredtypeid = models.ForeignKey('Invtypes', 
                                       db_column='requiredtypeid',
                                       related_name='required_type_set')
    quantity = models.IntegerField()
    damageperjob = models.FloatField()
    recycle = models.SmallIntegerField()
    class Meta:
        db_table = u'typeactivitymaterials'

class Mapregions(models.Model):
    regionid = models.IntegerField(primary_key=True)
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
    factionid = models.ForeignKey('Chrfactions', db_column='factionid')
    radius = models.FloatField()
    class Meta:
        db_table = u'mapregions'

class Ramactivities(models.Model):
    activityid = models.SmallIntegerField(primary_key=True)
    activityname = models.CharField(max_length=100)
    iconno = models.CharField(max_length=5)
    description = models.CharField(max_length=1000)
    published = models.SmallIntegerField()
    class Meta:
        db_table = u'ramactivities'

class Staoperations(models.Model):
    activityid = models.ForeignKey('Crpactivities', db_column='activityid')
    operationid = models.SmallIntegerField(primary_key=True)
    operationname = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    fringe = models.SmallIntegerField()
    corridor = models.SmallIntegerField()
    hub = models.SmallIntegerField()
    border = models.SmallIntegerField()
    ratio = models.SmallIntegerField()
    caldaristationtypeid = models.ForeignKey('Stastationtypes', 
                                             db_column='caldaristationtypeid',
                                             related_name='caldari_station_set')
    minmatarstationtypeid = models.ForeignKey('Stastationtypes', 
                                              db_column='minmatarstationtypeid',
                                              related_name='minmatar_station_set')
    amarrstationtypeid = models.ForeignKey('Stastationtypes', 
                                           db_column='amarrstationtypeid',
                                           related_name='amarr_station_set')
    gallentestationtypeid = models.ForeignKey('Stastationtypes', 
                                              db_column='gallentestationtypeid',
                                              related_name='gallente_station_set')
    jovestationtypeid = models.ForeignKey('Stastationtypes', 
                                          db_column='jovestationtypeid',
                                          related_name='jove_station_set')
    class Meta:
        db_table = u'staoperations'

class Agtagenttypes(models.Model):
    agenttypeid = models.SmallIntegerField(primary_key=True)
    agenttype = models.CharField(max_length=50)
    class Meta:
        db_table = u'agtagenttypes'

class Crpnpccorporations(models.Model):
    corporationid = models.IntegerField(primary_key=True)
    size = models.TextField() # This field type is a guess.
    extent = models.TextField() # This field type is a guess.
    solarsystemid = models.ForeignKey('Mapsolarsystems', db_column='solarsystemid')
    investorid1 = models.ForeignKey('self', db_column='investorid1',
                                    related_name='investor1_set')
    investorshares1 = models.SmallIntegerField()
    investorid2 = models.ForeignKey('self', db_column='investorid2',
                                    related_name='investor2_set')
    investorshares2 = models.SmallIntegerField()
    investorid3 = models.ForeignKey('self', db_column='investorid3',
                                    related_name='investor3_set')
    investorshares3 = models.SmallIntegerField()
    investorid4 = models.ForeignKey('self', db_column='investorid4',
                                    related_name='investor4_set')
    investorshares4 = models.SmallIntegerField()
    friendid = models.ForeignKey('self', db_column='friendid',
                                 related_name='friend_set')
    enemyid = models.ForeignKey('self', db_column='enemyid', 
                                related_name='enemy_set')
    publicshares = models.TextField() # This field type is a guess.
    initialprice = models.IntegerField()
    minsecurity = models.FloatField()
    scattered = models.SmallIntegerField()
    fringe = models.SmallIntegerField()
    corridor = models.SmallIntegerField()
    hub = models.SmallIntegerField()
    border = models.SmallIntegerField()
    factionid = models.ForeignKey('Chrfactions', db_column='factionid')
    sizefactor = models.FloatField()
    stationcount = models.SmallIntegerField()
    stationsystemcount = models.SmallIntegerField()
    class Meta:
        db_table = u'crpnpccorporations'

class Agtagents(models.Model):
    agentid = models.ForeignKey('Evenames', db_column='agentid')
    divisionid = models.ForeignKey('Crpnpcdivisions', db_column='divisionid')
    corporationid = models.ForeignKey('Crpnpccorporations', db_column='corporationid')
    stationid = models.ForeignKey('Stastations', db_column='stationid')
    level = models.SmallIntegerField()
    quality = models.SmallIntegerField()
    agenttypeid = models.ForeignKey('Agtagenttypes', db_column='agenttypeid')
    class Meta:
        db_table = u'agtagents'

class Crtcategories(models.Model):
    categoryid = models.SmallIntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    categoryname = models.CharField(max_length=256)
    class Meta:
        db_table = u'crtcategories'

class Crtclasses(models.Model):
    classid = models.SmallIntegerField(primary_key=True)
    description = models.CharField(max_length=500)
    classname = models.CharField(max_length=256)
    class Meta:
        db_table = u'crtclasses'

class Stastations(models.Model):
    stationid = models.IntegerField(primary_key=True)
    security = models.SmallIntegerField()
    dockingcostpervolume = models.FloatField()
    maxshipvolumedockable = models.FloatField()
    officerentalcost = models.IntegerField()
    operationid = models.ForeignKey('Staoperations', db_column='operationid')
    stationtypeid = models.ForeignKey('Stastationtypes', db_column='stationtypeid')
    corporationid = models.ForeignKey('Crpnpccorporations', db_column='corporationid')
    solarsystemid = models.ForeignKey('Mapsolarsystems', db_column='solarsystemid')
    constellationid = models.IntegerField()
    regionid = models.IntegerField()
    stationname = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    reprocessingefficiency = models.FloatField()
    reprocessingstationstake = models.FloatField()
    reprocessinghangarflag = models.SmallIntegerField()
    class Meta:
        db_table = u'stastations'

class Invtypes(models.Model):
    typeid = models.SmallIntegerField(primary_key=True)
    groupid = models.ForeignKey('Invgroups', db_column='groupid')
    typename = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    radius = models.FloatField()
    mass = models.FloatField()
    volume = models.FloatField()
    capacity = models.FloatField()
    portionsize = models.IntegerField()
    raceid = models.ForeignKey('Chrraces', db_column='raceid')
    baseprice = models.FloatField()
    published = models.SmallIntegerField()
    marketgroupid = models.ForeignKey('Invmarketgroups', db_column='marketgroupid')
    chanceofduplicating = models.FloatField()
    class Meta:
        db_table = u'invtypes'

class Mapdenormalize(models.Model):
    itemid = models.IntegerField(primary_key=True)
    typeid = models.ForeignKey('Invtypes', db_column='typeid',
                               related_name='denormalize_set')
    groupid = models.ForeignKey('Invgroups', db_column='groupid')
    solarsystemid = models.ForeignKey('Mapsolarsystems', db_column='solarsystemid')
    constellationid = models.ForeignKey('Mapconstellations', db_column='constellationid')
    regionid = models.ForeignKey('Mapregions', db_column='regionid')
    orbitid = models.ForeignKey('self', db_column='orbitid')
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

class Chrraces(models.Model):
    raceid = models.SmallIntegerField(primary_key=True)
    racename = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    graphicid = models.ForeignKey('Evegraphics', db_column='graphicid')
    shortdescription = models.CharField(max_length=500)
    class Meta:
        db_table = u'chrraces'

class Evenames(models.Model):
    itemid = models.IntegerField(primary_key=True)
    itemname = models.CharField(max_length=100)
    categoryid = models.ForeignKey('Invcategories', db_column='categoryid')
    groupid = models.ForeignKey('Invgroups', db_column='groupid')
    typeid = models.ForeignKey('Invtypes', db_column='typeid')
    class Meta:
        db_table = u'evenames'

class Mapconstellations(models.Model):
    regionid = models.ForeignKey('Mapregions', db_column='regionid')
    constellationid = models.IntegerField(primary_key=True)
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
    factionid = models.ForeignKey('Chrfactions', db_column='factionid')
    radius = models.FloatField()
    class Meta:
        db_table = u'mapconstellations'