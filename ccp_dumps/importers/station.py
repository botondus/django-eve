#!/usr/bin/env python
"""
Import station related data.
"""
# Setup the Django environment if this is being executed directly.
if __name__ == "__main__":
    import os
    import sqlite3
    import constants
    constants.setup_environment()
from apps.eve_db.models import *

def import_ramActivities(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from ramActivities'):
        imp_obj, created = ResearchAndMfgActivity.objects.get_or_create(id=row['activityID'])
        imp_obj.name = row['activityName']
        imp_obj.description = row['description']
        
        if row['iconNo']:
            imp_obj.icon_filename = row['iconNo']
        
        if row['published'] == 1:
            imp_obj.is_published = True
        else:
            imp_obj.is_published = False

        imp_obj.save()
    c.close()
    
def import_staServices(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from staServices'):
        imp_obj, created = StationService.objects.get_or_create(id=row['serviceID'])
        imp_obj.name = row['serviceName']
        imp_obj.description = row['description']
        imp_obj.save()
    c.close()
    
if __name__ == "__main__":
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    
    import_ramActivities(conn)
    import_staServices(conn)
