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
from apps.eve_db.models import EVEName, EVERace, EVEGraphic, EVEInventoryCategory, EVEInventoryGroup, EVEMarketGroup, EVEInventoryType, EVEInventoryBlueprintType, EVETypeActivityMaterials, EVEResearchMfgActivities

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
    
def do_import_invtypes(conn):
    """
    Handle the import.
    """
    c = conn.cursor()
    
    for row in c.execute('select * from invTypes'):
        invtype, created = EVEInventoryType.objects.get_or_create(id=row['typeID'])
        invtype.name = row['typeName']
        invtype.description = row['description']
        invtype.group = EVEInventoryGroup.objects.get(id=row['groupID'])
        invtype.radius = row['radius']
        invtype.mass = row['mass']
        invtype.volume = row['volume']
        invtype.capacity = row['capacity']
        invtype.portion_size = row['portionSize']
        
        if row['marketGroupID']:
            invtype.market_group = EVEMarketGroup.objects.get(id=row['marketGroupID'])
        
        if row['published'] == 1:
            invtype.is_published = True
        
        if row['raceID']:
            invtype.race = EVERace.objects.get(id=row['raceID'])
            
        if row['graphicID']:
            #print row['graphicID']
            invtype.graphic = EVEGraphic.objects.get(id=row['graphicID'])
            
        invtype.chance_of_duplicating = row['chanceOfDuplicating']
        invtype.save()

    # Clean up.
    c.close()
    
def do_import_blueprint_types(conn):
    """
    Import blueprint types.
    """
    c = conn.cursor()
    
    for row in c.execute('select * from invBlueprintTypes'):
        blueprint_type = EVEInventoryType.objects.get(id=row['blueprintTypeID'])
        product_type = EVEInventoryType.objects.get(id=row['productTypeID'])
        invtype, created = EVEInventoryBlueprintType.objects.get_or_create(blueprint_type=blueprint_type,
                                                                           product_type=product_type)
        if row['parentBlueprintTypeID']:
            invtype.parent_blueprint_Type = EVEInventoryType.objects.get(id=row['parentBlueprintTypeID'])
            
        invtype.tech_level = row['techLevel']
        invtype.research_productivity_time = row['researchProductivityTime']
        invtype.research_material_time = row['researchMaterialTime']
        invtype.research_copy_time = row['researchCopyTime']
        invtype.research_tech_time = row['researchTechTime']
        invtype.productivity_modifier = row['productivityModifier']
        invtype.material_modifier = row['materialModifier']
        invtype.waste_factor = row['wasteFactor']
        invtype.max_production_limit = row['maxProductionLimit']

        invtype.save()

    # Clean up.
    c.close()

def do_import_activity_materials(conn):
    """
    Import the activity materials.
    """
    c = conn.cursor()

    for row in c.execute('select * from typeActivityMaterials'):
        blueprint_type = EVEInventoryType.objects.get(id=row['typeID'])
        activity = EVEResearchMfgActivities.objects.get(id=row['activityID'])
        required_type = EVEInventoryType.objects.get(id=row['requiredTypeID'])
        actmaterial, created = EVETypeActivityMaterials.objects.get_or_create(blueprint_type=blueprint_type,
                                                                              activity=activity,
                                                                              required_type=required_type)

        actmaterial.quantity = row['quantity']
        actmaterial.damage_per_job = row['damagePerJob']

        actmaterial.save()

    # Clean up.
    c.close()
    
def do_import_eve_names(conn):
    """
    Import eveNames table.
    """
    c = conn.cursor()
    for row in c.execute('select * from eveNames'):
        imp_obj, created = EVEName.objects.get_or_create(id=row['itemID'])
        imp_obj.name = row['itemName']
        imp_obj.category = EVEInventoryCategory.objects.get(id=row['categoryID'])
        imp_obj.group = EVEInventoryGroup.objects.get(id=row['groupID'])
        imp_obj.type = EVEInventoryType.objects.get(id=row['typeID'])
        imp_obj.save()
    c.close()
        
def do_import():
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    
    #do_import_categories(conn)
    #do_import_groups(conn)
    #do_import_market_groups(conn)
    #do_import_invtypes(conn)
    #do_import_blueprint_types(conn)
    #do_import_activity_materials(conn)
    do_import_eve_names(conn)

if __name__ == "__main__":
    do_import()
