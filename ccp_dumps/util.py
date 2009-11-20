import sqlite3
from importers import *

# These are references to importer functions. They are ran in the order
# they appear in this list. Any lines that are commented out are importers
# that have not been written yet.
IMPORT_LIST = [import_chrFactions,
               import_mapRegions,
               #import_mapRegionJumps,
               import_mapConstellations,
               #import_mapConstellationJumps,
               #import_agtAgentTypes,
               import_crpNPCDivisions,
               import_crpActivities,
               import_eveGraphics,
               import_eveUnits,
               import_invMetaGroups,
               import_invFlags,
               import_invMarketGroups,
               import_invControlTowerResourcePurposes,
               import_mapUniverse,
               import_staServices,
               #import_ramCompletedStatuses,
               #import_ramAssemblyLineTypes,
               import_ramActivities,
               import_invCategories,
               import_invGroups,
               import_chrRaces,
               import_invTypes,
               import_invControlTowerResources,
               import_chrBloodlines,
               import_chrAncestries,
               import_mapSolarSystems,
               #import_mapSolarSystemJumps,
               #import_mapDenormalize,
               #import_mapJumps,
               #import_mapCelestialStatistics,
               #import_mapLandmarks,
               import_eveNames,
               import_invContrabandTypes,
               import_invTypeReactions,
               import_invBlueprintTypes,
               import_invMetaTypes,
               import_dgmAttributeCategories,
               import_dgmAttributeTypes,
               import_dgmTypeAttributes,
               import_dgmEffects,
               import_dgmTypeEffects,               
               #import_chrRaceSkills,
               #import_chrAttributes,
               #import_ramAssemblyLineTypeDetailPerCategory,
               #import_ramAssemblyLineTypeDetailPerGroup,
               import_typeActivityMaterials,
               import_crpNPCCorporations,
               #import_crpNPCCorporationDivisions,
               #import_crpNPCCorporationTrades,
               #import_crpNPCCorporationResearchFields,
               #import_staStationTypes,
               #import_staOperations,
               #import_staStations,
               #import_ramAssemblyLines,
               #import_staOperationServices,
               #import_ramAssemblyLineStations,
               #import_agtAgents,
               #import_agtConfig,
               #import_chrCareers,
               #import_chrCareerSkills,
               #import_chrSchools,
               #import_chrSchoolAgents,
               #import_chrCareerSpecialities,
               #import_chrCareerSpecialitySkills,
               ]
    
def run_importers(importer_funcs):
    """
    importer_funcs: (list) References to the importer functions to run.
    """     
    # Create the SQLite connection object.
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    
    # Carry out the imports in order.
    for importer in importer_funcs:
        print "  - %s" % importer.__name__
        importer(conn)
        
    print "Importing complete."
