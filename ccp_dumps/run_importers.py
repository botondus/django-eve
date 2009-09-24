#!/usr/bin/env python
import os
import sys

# Setup Django environment.
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Import the importer modules.
from importers import chr, graphics, inventory, station,  map, npc

print "NOTE: This is going to take anywhere from 15-30 minutes depending on the speed of your computer and DB server. You may abort it at any time and re-start it later via CTRL-D or CTRL-C, depending on your platform."
print "Importing from the CCP dump..."

# Carry out the imports in order.
for mod in [graphics, chr, station, inventory,  map, npc]:
    print "  - %s" % mod.__name__
    mod.do_import()
    
print "Importing complete."
