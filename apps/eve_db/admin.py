from django.contrib import admin
from apps.eve_db.models import *

class EVEInventoryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_published')
admin.site.register(EVEInventoryCategory, EVEInventoryCategoryAdmin)

class EVEInventoryMetaGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'graphic')
admin.site.register(EVEInventoryMetaGroup, EVEInventoryMetaGroupAdmin)

class EVEInventoryMetaTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'parent_type', 'meta_group')
admin.site.register(EVEInventoryMetaType, EVEInventoryMetaTypeAdmin)

class EVEInventoryGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(EVEInventoryGroup, EVEInventoryGroupAdmin)

class EVEInventoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'market_group', 'description')
admin.site.register(EVEInventoryType, EVEInventoryTypeAdmin)

class EVEInventoryFlagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'type_text', 'order')
admin.site.register(EVEInventoryFlag, EVEInventoryFlagAdmin)

class EVEInventoryBlueprintTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'blueprint_type', 'product_type', 'tech_level')
admin.site.register(EVEInventoryBlueprintType, EVEInventoryBlueprintTypeAdmin)

class EVEResearchMfgActivitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'icon_filename', 'is_published')
admin.site.register(EVEResearchMfgActivities, EVEResearchMfgActivitiesAdmin)

class EVETypeActivityMaterialsAdmin(admin.ModelAdmin):
    list_display = ('blueprint_type', 'activity', 'required_type', 'quantity')
admin.site.register(EVETypeActivityMaterials, EVETypeActivityMaterialsAdmin)    
 
class EVEUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_name', 'description')
admin.site.register(EVEUnit, EVEUnitAdmin)
 
class EVEInventoryAttributeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(EVEInventoryAttributeCategory, EVEInventoryAttributeCategoryAdmin)
 
class EVEInventoryAttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(EVEInventoryAttributeType, EVEInventoryAttributeTypeAdmin)
 
class EVEInventoryTypeAttributesAdmin(admin.ModelAdmin):
    list_display = ('inventory_type', 'attribute', 'value_int', 'value_float')
admin.site.register(EVEInventoryTypeAttributes, EVEInventoryTypeAttributesAdmin)

class EVEGraphicAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'name', 'icon_filename')
admin.site.register(EVEGraphic, EVEGraphicAdmin)

class EVENameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'group', 'type')
admin.site.register(EVEName, EVENameAdmin)

class EVERaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description')
admin.site.register(EVERace, EVERaceAdmin)

class EVEPlayerCorporationInline(admin.TabularInline):
    model = EVEPlayerCorporation
    fields = ('name', 'ticker')
    extra = 0

class EVEPlayerAllianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ticker', 'member_count', 'date_founded')
    search_fields = ['name', 'ticker']
    date_hierarchy = 'date_founded'
    inlines = [EVEPlayerCorporationInline]
admin.site.register(EVEPlayerAlliance, EVEPlayerAllianceAdmin)

class EVEPlayerCorporationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ticker', 'member_count', 'alliance')
    search_fields = ['name', 'ticker']
admin.site.register(EVEPlayerCorporation, EVEPlayerCorporationAdmin)
