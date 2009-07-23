#!/usr/bin/env python
"""
Import race data.

Tables imported:
chrRaces
"""
import os
import sqlite3
import constants
# Setup the Django environment if this is being executed directly.
if __name__ == "__main__":
    constants.setup_environment()
from apps.eve_db.models import EVERace, EVEGraphic

def do_import():
    """
    Handle the import.
    """
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    for row in c.execute('select * from chrRaces'):
        race, created = EVERace.objects.get_or_create(id=row['raceID'])
        race.name = row['raceName']
        race.short_description = row['shortDescription']
        race.description = row['description']
        
        graphic_id = row['graphicID']
        if graphic_id:
            race.graphic = EVEGraphic.objects.get(id=graphic_id)

        race.save()

    # Clean up.
    c.close()

if __name__ == "__main__":
    do_import()