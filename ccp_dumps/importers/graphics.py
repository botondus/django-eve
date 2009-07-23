#!/usr/bin/env python
"""
Import graphic data.

Tables imported:
eveGraphics
"""
import os
import sqlite3
import constants
# Setup the Django environment if this is being executed directly.
if __name__ == "__main__":
    constants.setup_environment()
from apps.eve_db.models import EVEGraphic

def do_import():
    """
    Handle the import.
    """
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    for row in c.execute('select * from eveGraphics'):
        graphic, created = EVEGraphic.objects.get_or_create(id=row['graphicID'])
        graphic.name = row['urlWeb']
        graphic.icon_filename = row['icon']
        graphic.description = row['description']
        
        # Handle booleans
        if row['published'] == 1:
            graphic.is_published = True
        else:
            graphic.is_published = False
            
        if row['obsolete'] == 1:
            graphic.is_obsolete = True
        else:
            graphic.is_obsolete = False
        graphic.save()

    # Clean up.
    c.close()

if __name__ == "__main__":
    do_import()