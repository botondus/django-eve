#!/usr/bin/env python
"""
Import inventory data.
"""
import os
import sqlite3
import constants
# Setup the Django environment if this is being executed directly.
if __name__ == "__main__":
    constants.setup_environment()
from apps.eve_db.models import *

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

def do_import_meta_groups(conn):
    """
    invMetaGroup
    """
    c = conn.cursor()
    
    for row in c.execute('select * from invMetaGroups'):
        imp_obj, created = EVEInventoryMetaGroup.objects.get_or_create(id=row['metaGroupID'])
        imp_obj.name = row['metaGroupName']
        imp_obj.description = row['description']
        
        graphic_id = row['graphicID']
        if graphic_id:
            imp_obj.graphic = EVEGraphic.objects.get(id=graphic_id)
        imp_obj.save()

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
    
def do_import_metatypes(conn):
    """
    invMetaTypes
    """
    c = conn.cursor()
    
    for row in c.execute('select * from invMetaTypes'):
        type = EVEInventoryType.objects.get(id=row['typeID'])
        parent_type = EVEInventoryType.objects.get(id=row['parentTypeID'])
        meta_group = EVEInventoryMetaGroup.objects.get(id=row['metaGroupID'])
        
        imp_obj, created = EVEInventoryMetaType.objects.get_or_create(type=type,
                                                                      parent_type=parent_type,
                                                                      meta_group=meta_group)
        imp_obj.save()
    c.close()
    
def do_import_effects(conn):
    """
    dgmEffects
    """
    c = conn.cursor()
    
    for row in c.execute('select * from dgmEffects'):
        imp_obj, created = EVEInventoryEffect.objects.get_or_create(id=row['effectID'])
        imp_obj.name = row['effectName']
        imp_obj.category = row['effectCategory']
        imp_obj.pre_expression = row['preExpression']
        imp_obj.post_expression = row['postExpression']
        imp_obj.description = row['description']
        
        if row['guid']:
            imp_obj.guid = row['guid']
        
        if row['graphicID']:
            imp_obj.graphic = EVEGraphic.objects.get(id=row['graphicID'])
            
        if row['isOffensive'] == 1:
            imp_obj.is_offensive = True
            
        if row['isAssistance'] == 1:
            imp_obj.is_assistance = True
            
        if row['durationAttributeID']:
            imp_obj.duration_attribute = EVEInventoryAttributeType.objects.get(id=row['durationAttributeID'])
            
        if row['trackingSpeedAttributeID']:
            imp_obj.tracking_speed_attribute = EVEInventoryAttributeType.objects.get(id=row['trackingSpeedAttributeID'])
            
        if row['dischargeAttributeID']:
            imp_obj.discharge_attribute = EVEInventoryAttributeType.objects.get(id=row['dischargeAttributeID'])
            
        if row['rangeAttributeID']:
            imp_obj.range_attribute = EVEInventoryAttributeType.objects.get(id=row['rangeAttributeID'])
            
        if row['falloffAttributeID']:
            imp_obj.falloff_attribute = EVEInventoryAttributeType.objects.get(id=row['falloffAttributeID'])            
            
        if row['disallowAutoRepeat'] == 1:
            imp_obj.disallow_autorepeat = True
            
        if row['published'] == 1:
            imp_obj.is_published = True
            
        imp_obj.display_name = row['displayName']
        
        if row['isWarpSafe'] == 1:
            imp_obj.is_warp_safe = True
            
        if row['rangeChance'] == 1:
            imp_obj.has_range_chance = True
            
        if row['electronicChance'] == 1:
            imp_obj.has_electronic_chance = True
            
        if row['propulsionChance'] == 1:
            imp_obj.has_propulsion_chance = True
            
        imp_obj.distribution = row['distribution']
        
        if row['sfxName']:
            imp_obj.sfx_name = row['sfxName']
        
        if row['npcUsageChanceAttributeID']:
            imp_obj.npc_usage_chance_attribute = EVEInventoryAttributeType.objects.get(id=row['npcUsageChanceAttributeID'])
    
        if row['npcActivationChanceAttributeID']:
            imp_obj.npc_activation_chance_attribute = EVEInventoryAttributeType.objects.get(id=row['npcActivationChanceAttributeID'])

        if row['fittingUsageChanceAttributeID']:
            imp_obj.fitting_usage_chance_attribute = EVEInventoryAttributeType.objects.get(id=row['fittingUsageChanceAttributeID'])

        imp_obj.save()

    # Clean up.
    c.close()
    
def do_import_type_effects(conn):
    """
    dgmTypeEffects
    """
    c = conn.cursor()
    
    for row in c.execute('select * from dgmTypeEffects'):
        type = EVEInventoryType.objects.get(id=row['typeID'])
        effect = EVEInventoryEffect.objects.get(id=row['effectID'])        
        imp_obj, created = EVEInventoryTypeEffect.objects.get_or_create(
                                                                type=type,
                                                                effect=effect)
        imp_obj.is_default = row['isDefault']
        imp_obj.save()
    c.close()
    
def do_import_flags(conn):
    """
    invFlags
    """
    c = conn.cursor()
    
    for row in c.execute('select * from invFlags'):        
        imp_obj, created = EVEInventoryFlag.objects.get_or_create(id=row['flagID'])
        imp_obj.name = row['flagName']
        imp_obj.text = row['flagText']
        imp_obj.type_text = row['flagType']
        imp_obj.order = row['orderID']
        imp_obj.save()
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
    
def do_import_type_reactions(conn):
    """
    Import POS reactions.
    
    invTypeReactions
    """
    c = conn.cursor()

    for row in c.execute('select * from invTypeReactions'):
        reaction_type = EVEInventoryType.objects.get(id=row['reactionTypeID'])
        type = EVEInventoryType.objects.get(id=row['typeID'])
        imp_obj, created = EVEInventoryTypeReactions.objects.get_or_create(reaction_type=reaction_type,
                                                                           type=type)
        imp_obj.input = row['input']
        imp_obj.quantity = row['quantity']
        
        imp_obj.save()
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

    do_import_categories(conn)
    do_import_groups(conn)
    do_import_market_groups(conn)
    do_import_invtypes(conn)
    do_import_blueprint_types(conn)
    do_import_activity_materials(conn)
    do_import_eve_names(conn)
    do_import_meta_groups(conn)
    do_import_metatypes(conn)
    do_import_flags(conn)
    do_import_effects(conn)
    do_import_type_effects(conn)
    do_import_type_reactions(conn)

if __name__ == "__main__":
    do_import()
