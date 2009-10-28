#!/usr/bin/env python
import os
import sys
import sqlite3

# Setup Django environment.
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# Import the importer modules.
from importers import constants
import importers

print "NOTE: This is going to take anywhere from 15-30 minutes depending on the speed of your computer and DB server. You may abort it at any time and re-start it later via CTRL-D or CTRL-C, depending on your platform."
print "Importing from the CCP dump..."

# These are references to importer functions. They are ran in the order
# they appear in this list. Any lines that are commented out are importers
# that have not been written yet.
IMPORT_LIST = [importers.import_chrFactions,
               importers.import_mapRegions,
               #importers.import_mapRegionJumps,
               importers.import_mapConstellations,
               #importers.import_mapConstellationJumps,
               #importers.import_agtAgentTypes,
               importers.import_crpNPCDivisions,
               importers.import_crpActivities,
               importers.import_eveGraphics,
               importers.import_eveUnits,
               importers.import_invMetaGroups,
               importers.import_invFlags,
               importers.import_invMarketGroups,
               importers.import_invControlTowerResourcePurposes,
               importers.import_mapUniverse,
               importers.import_staServices,
               #importers.import_ramCompletedStatuses,
               #importers.import_ramAssemblyLineTypes,
               importers.import_ramActivities,
               importers.import_invCategories,
               importers.import_invGroups,
               importers.import_invTypes,
               importers.import_invControlTowerResources,
               importers.import_chrBloodlines,
               importers.import_chrAncestries,
               importers.import_mapSolarSystems,
               #importers.import_mapSolarSystemJumps,
               #importers.import_mapDenormalize,
               #importers.import_mapJumps,
               #importers.import_mapCelestialStatistics,
               #importers.import_mapLandmarks,
               importers.import_eveNames,
               importers.import_invContrabandTypes,
               importers.import_invTypeReactions,
               importers.import_invBlueprintTypes,
               importers.import_invMetaTypes,
               importers.import_dgmAttributeCategories,
               importers.import_dgmAttributeTypes,
               importers.import_dgmTypeAttributes,
               importers.import_dgmEffects,
               importers.import_dgmTypeEffects,               
               importers.import_chrRaces,
               #importers.import_chrRaceSkills,
               #importers.import_chrAttributes,
               #importers.import_ramAssemblyLineTypeDetailPerCategory,
               #importers.import_ramAssemblyLineTypeDetailPerGroup,
               importers.import_typeActivityMaterials,
               importers.import_crpNPCCorporations,
               #importers.import_crpNPCCorporationDivisions,
               #importers.import_crpNPCCorporationTrades,
               #importers.import_crpNPCCorporationResearchFields,
               #importers.import_staStationTypes,
               #importers.import_staOperations,
               #importers.import_staStations,
               #importers.import_ramAssemblyLines,
               #importers.import_staOperationServices,
               #importers.import_ramAssemblyLineStations,
               #importers.import_agtAgents,
               #importers.import_agtConfig,
               #importers.import_chrCareers,
               #importers.import_chrCareerSkills,
               #importers.import_chrSchools,
               #importers.import_chrSchoolAgents,
               #importers.import_chrCareerSpecialities,
               #importers.import_chrCareerSpecialitySkills,
               ]

# Create the SQLite connection object.
conn = sqlite3.connect(constants.DB_FILE)
conn.row_factory = sqlite3.Row

# Carry out the imports in order.
for importer in IMPORT_LIST:
    print "  - %s" % importer.__name__
    importer(conn)
    
print "Importing complete."
