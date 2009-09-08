#!/usr/bin/env python
import os
import sys

# Setup Django environment.
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# Import the importer modules.
from importers import chr, graphics, inventory, stations

print "Importing from the CCP dump..."

# Carry out the imports in order.
for mod in [graphics, chr, inventory, stations]:
    print "  - %s" % mod.__name__
    mod.do_import()
    
print "Importing complete."