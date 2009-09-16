#!/usr/bin/env python
"""
Import character data.

Tables imported:
chrRaces
"""
import os
import sqlite3
import constants
# Setup the Django environment if this is being executed directly.
if __name__ == "__main__":
    constants.setup_environment()
from apps.eve_db.models import *

def do_import_races(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from chrRaces'):
        imp_obj, created = EVERace.objects.get_or_create(id=row['raceID'])
        imp_obj.name = row['raceName']
        imp_obj.short_description = row['shortDescription']
        imp_obj.description = row['description']
        
        graphic_id = row['graphicID']
        if graphic_id:
            imp_obj.graphic = EVEGraphic.objects.get(id=graphic_id)

        imp_obj.save()
    c.close()
    
def do_import_factions(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from chrFactions'):
        imp_obj, created = Faction.objects.get_or_create(id=row['factionID'])
        imp_obj.name = row['factionName']
        imp_obj.description = row['description']
        
        if row['solarSystemID']:
            solar_system, ss_created = SolarSystem.objects.get_or_create(id=row['solarSystemID'])
            imp_obj.solar_system = solar_system
            
        if row['corporationID']:
            corp, corp_created = NPCCorporation.objects.get_or_create(id=row['corporationID'])
            imp_obj.corporation = corp
            
        imp_obj.size_factor = row['sizeFactor']
        imp_obj.station_count = row['stationCount']
        imp_obj.station_system_count = row['stationSystemCount']

        imp_obj.save()
    c.close()

def do_import():
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    
    do_import_races(conn)
    do_import_factions(conn)

if __name__ == "__main__":
    do_import()