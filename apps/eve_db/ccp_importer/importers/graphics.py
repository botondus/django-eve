#!/usr/bin/env python
"""
Import graphic data.
"""
from apps.eve_db.models import EVEGraphic
from importer_classes import SQLImporter

class Importer_eveGraphics(SQLImporter):
    def run_importer(self, conn):
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
        c.close()