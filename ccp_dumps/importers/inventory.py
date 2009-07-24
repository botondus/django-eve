#!/usr/bin/env python
"""
Import inventory data.

Tables imported:
invCategories
invGroups
"""
import os
import sqlite3
import constants
# Setup the Django environment if this is being executed directly.
if __name__ == "__main__":
    constants.setup_environment()
from apps.eve_db.models import EVEGraphic, EVEInventoryCategory, EVEInventoryGroup, EVEMarketGroup

def do_import_categories(conn):
    """
    Handle the import.
    """
    c = conn.cursor()
    
    for row in c.execute('select * from invCategories'):
        category, created = EVEInventoryCategory.objects.get_or_create(id=row['categoryID'])
        category.name = row['categoryName']
        category.description = row['description']
        
        graphic_id = row['graphicID']
        if graphic_id:
            category.graphic = EVEGraphic.objects.get(id=graphic_id)
            
        # Handle boolean.
        if row['published'] == 1:
            category.is_published = True
        else:
            category.is_published = False

        category.save()

    # Clean up.
    c.close()
    
def do_import_groups(conn):
    """
    Handle the import.
    """
    c = conn.cursor()
    
    for row in c.execute('select * from invGroups'):
        category_id = row['categoryID']
        category = EVEInventoryCategory.objects.get(id=category_id)

        group, created = EVEInventoryGroup.objects.get_or_create(id=row['groupID'],
                                                                 category=category)
        group.name = row['groupName']
        group.description = row['description']
        
        graphic_id = row['graphicID']
        if graphic_id:
            group.graphic = EVEGraphic.objects.get(id=graphic_id)
            
        # Handle boolean.
        group.use_base_price = constants.parse_int_bool(row['useBasePrice'])
        group.allow_manufacture = constants.parse_int_bool(row['allowManufacture'])
        group.allow_recycle = constants.parse_int_bool(row['allowRecycler'])
        group.allow_anchoring = constants.parse_int_bool(row['anchorable'])
        group.is_anchored = constants.parse_int_bool(row['anchored'])
        group.is_fittable_non_singleton = constants.parse_int_bool(row['fittableNonSingleton'])
        group.is_published = constants.parse_int_bool(row['published'])

        group.save()

    # Clean up.
    c.close()
    
def do_import_market_groups(conn):
    """
    Handle the import.
    """
    c = conn.cursor()
    
    for row in c.execute('select * from invMarketGroups'):
        group, created = EVEMarketGroup.objects.get_or_create(id=row['marketGroupID'])
        group.name = row['marketGroupName']
        group.description = row['description']
        
        graphic_id = row['graphicID']
        if graphic_id:
            group.graphic = EVEGraphic.objects.get(id=graphic_id)
            
        parent_id = row['parentGroupID']
        if parent_id:
            parent, created = EVEMarketGroup.objects.get_or_create(id=parent_id)
            group.parent = parent
            
        group.has_items = constants.parse_int_bool(row['hasTypes'])

        group.save()

    # Clean up.
    c.close()
    
def do_import():
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    
    do_import_categories(conn)
    do_import_groups(conn)
    do_import_market_groups(conn)

if __name__ == "__main__":
    do_import()