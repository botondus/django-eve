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
from apps.eve_db.models import EVERace

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
        race.save()

    # Clean up.
    c.close()

if __name__ == "__main__":
    do_import()