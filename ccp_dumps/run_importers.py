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
# they appear in this list.
IMPORT_LIST = [importers.import_chrRaces,
               importers.import_chrFactions,
               importers.import_chrBloodlines,
               importers.import_chrAncestries,
               importers.import_eveGraphics,
               importers.import_invCategories,
               importers.import_invGroups,
               importers.import_invMetaGroups,
               importers.import_invMarketGroups,
               importers.import_invTypes,
               importers.import_invMetaTypes,
               importers.import_eveUnits,
               importers.import_dgmAttributeCategories,
               importers.import_dgmAttributeTypes,
               importers.import_dgmTypeAttributes,
               importers.import_dgmEffects,
               importers.import_dgmTypeEffects,
               importers.import_invFlags,
               importers.import_invBlueprintTypes,
               importers.import_invControlTowerResourcePurposes,
               importers.import_invControlTowerResources,
               importers.import_typeActivityMaterials,
               importers.import_invTypeReactions,
               importers.import_invContrabandTypes,
               importers.import_eveNames,
               importers.import_ramActivities,
               importers.import_staServices,
               importers.import_mapUniverse,
               importers.import_mapRegions,
               importers.import_mapConstellations,
               importers.import_mapSolarSystems,
               importers.import_crpActivities,
               importers.import_crpNPCCorporations,
               importers.import_crpNPCDivisions]

# Create the SQLite connection object.
conn = sqlite3.connect(constants.DB_FILE)
conn.row_factory = sqlite3.Row

# Carry out the imports in order.
for importer in IMPORT_LIST:
    print "  - %s" % importer.__name__
    importer(conn)
    
print "Importing complete."
