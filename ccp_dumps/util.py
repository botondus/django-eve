import sqlite3
from importers import constants
from importers import *

# These are references to importer functions. They are ran in the order
# they appear in this list. Any lines that are commented out are importers
# that have not been written yet.
IMPORT_LIST = [Importer_chrFactions,
               Importer_mapRegions,
               #Importer_mapRegionJumps,
               Importer_mapConstellations,
               #Importer_mapConstellationJumps,
               #Importer_agtAgentTypes,
               Importer_crpNPCDivisions,
               Importer_crpActivities,
               Importer_eveGraphics,
               Importer_eveUnits,
               Importer_invMetaGroups,
               Importer_invFlags,
               Importer_invMarketGroups,
               Importer_invControlTowerResourcePurposes,
               Importer_mapUniverse,
               Importer_staServices,
               #Importer_ramCompletedStatuses,
               #Importer_ramAssemblyLineTypes,
               Importer_ramActivities,
               Importer_invCategories,
               Importer_invGroups,
               Importer_chrRaces,
               Importer_invTypes,
               Importer_invControlTowerResources,
               Importer_chrBloodlines,
               Importer_chrAncestries,
               Importer_mapSolarSystems,
               #Importer_mapSolarSystemJumps,
               #Importer_mapDenormalize,
               #Importer_mapJumps,
               #Importer_mapCelestialStatistics,
               #Importer_mapLandmarks,
               Importer_eveNames,
               Importer_invContrabandTypes,
               Importer_invTypeReactions,
               Importer_invBlueprintTypes,
               Importer_invMetaTypes,
               Importer_dgmAttributeCategories,
               Importer_dgmAttributeTypes,
               Importer_dgmTypeAttributes,
               Importer_dgmEffects,
               Importer_dgmTypeEffects,               
               #Importer_chrRaceSkills,
               #Importer_chrAttributes,
               #Importer_ramAssemblyLineTypeDetailPerCategory,
               #Importer_ramAssemblyLineTypeDetailPerGroup,
               Importer_typeActivityMaterials,
               Importer_crpNPCCorporations,
               #Importer_crpNPCCorporationDivisions,
               #Importer_crpNPCCorporationTrades,
               #Importer_crpNPCCorporationResearchFields,
               #Importer_staStationTypes,
               #Importer_staOperations,
               #Importer_staStations,
               #Importer_ramAssemblyLines,
               #Importer_staOperationServices,
               #Importer_ramAssemblyLineStations,
               #Importer_agtAgents,
               #Importer_agtConfig,
               #Importer_chrCareers,
               #Importer_chrCareerSkills,
               #Importer_chrSchools,
               #Importer_chrSchoolAgents,
               #Importer_chrCareerSpecialities,
               #Importer_chrCareerSpecialitySkills,
               ]
    
def run_importers(importer_classes):
    """
    importer_classes: (list) References to the importer classes to run.
    """     
    # Create the SQLite connection object.
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
        
    # Carry out the imports in order.
    for importer_class in importer_classes:
        importer = importer_class()
        importer_name = importer.__class__.__name__.split('_')[1]
        print "  - %s" % importer_name
        importer.run_importer(conn)
        
    print "Importing complete."
