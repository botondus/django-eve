#!/usr/bin/env python
"""
Import attributes and effects.
"""
import os
import sqlite3
import constants
# Setup the Django environment if this is being executed directly.
if __name__ == "__main__":
    constants.setup_environment()
from apps.eve_db.models import EVEUnit, EVEInventoryAttributeCategory, EVEInventoryAttributeType, EVEInventoryTypeAttributes, EVEGraphic, EVEInventoryType

def do_import_eve_units(conn):
    """
    Handle the import.
    """
    c = conn.cursor()
    
    for row in c.execute('select * from eveUnits'):
        imp_obj, created = EVEUnit.objects.get_or_create(id=row['unitid'])
        imp_obj.name = row['unitname']
        imp_obj.display_name = row['displayname']
        imp_obj.description = row['description']

        imp_obj.save()

    # Clean up.
    c.close()

def do_import_attribute_categories(conn):
    """
    Handle the import.
    """

    c = conn.cursor()

    for row in c.execute('select * from dgmattributecategories'):
        imp_obj, created = EVEInventoryAttributeCategory.objects.get_or_create(id=row['categoryid'])
        imp_obj.name = row['categoryname']
        imp_obj.description = row['categorydescription']

        imp_obj.save()

    # Clean up.
    c.close()

def do_import_attribute_types(conn):
    """
    Handle the import.
    """

    c = conn.cursor()

    for row in c.execute('select * from dgmattributetypes'):
        imp_obj, created = EVEInventoryAttributeType.objects.get_or_create(id=row['attributeid'])
        imp_obj.name = row['attributename']
        imp_obj.description = row['description']
        imp_obj.default_value = row['defaultvalue']
        imp_obj.is_published = constants.parse_int_bool(row['published'])
        imp_obj.display_name = row['displayname']
        imp_obj.is_stackable = constants.parse_int_bool(row['stackable'])
        imp_obj.high_is_good = constants.parse_int_bool(row['highisgood'])

        category_id = row['categoryid']
        if category_id:
            imp_obj.category = EVEInventoryAttributeCategory.objects.get(id=category_id)

        unit_id = row['unitid']
        if unit_id:
            imp_obj.unit = EVEUnit.objects.get(id=unit_id)

        graphic_id = row['graphicID']
        if graphic_id:
            imp_obj.graphic = EVEGraphic.objects.get(id=graphic_id)

        imp_obj.save()
            
    # Clean up.
    c.close()

def do_import_inventory_type_attributes(conn):
    """
    Handle the import.
    """

    c = conn.cursor()

    for row in c.execute('select * from dgmtypeattributes'):    
        inventory_type = EVEInventoryType.objects.get(id=row['typeid'])
        attribute = EVEInventoryAttributeType.objects.get(id=row['attributeid'])
        imp_obj, created = EVEInventoryTypeAttributes.objects.get_or_create(inventory_type=inventory_type,
                                                                            attribute=attribute)

        if row['valueint']:
            imp_obj.value_int = row['valueint']

        if row['valuefloat']:
            imp_obj.value_float = row['valuefloat']

        imp_obj.save()

    # Clean up.
    c.close()

def do_import():
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    
    do_import_eve_units(conn)
    do_import_attribute_categories(conn)
    do_import_attribute_types(conn)
    do_import_inventory_type_attributes(conn)
    
if __name__ == "__main__":
    do_import()
