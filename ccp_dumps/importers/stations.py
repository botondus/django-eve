#!/usr/bin/env python
"""
Import station related data.
"""
import os
import sqlite3
import constants
# Setup the Django environment if this is being executed directly.
if __name__ == "__main__":
    constants.setup_environment()
from apps.eve_db.models import EVEResearchMfgActivities

def do_import_ram_activities(conn):
    """
    Handle the import.
    """
    c = conn.cursor()
    
    for row in c.execute('select * from ramActivities'):
        imp_obj, created = EVEResearchMfgActivities.objects.get_or_create(id=row['activityID'])
        imp_obj.name = row['activityName']
        imp_obj.description = row['description']
        
        if row['iconNo']:
            imp_obj.icon_filename = row['iconNo']
        
        if row['published'] == 1:
            imp_obj.is_published = True
        else:
            imp_obj.is_published = False

        imp_obj.save()

    # Clean up.
    c.close()

def do_import():
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    
    do_import_ram_activities(conn)

if __name__ == "__main__":
    do_import()