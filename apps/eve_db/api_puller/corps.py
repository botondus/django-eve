#!/usr/bin/env python
"""
Module for updating corp information. If this is ran directly, the module will
iterate through all known alliances, looking at the corps in each alliance's
member list. This can be very time-consuming and should not be done often.

Within your applications, you may call query_and_update_corp() to update
an individual corp object as need be.

NOTE: To get corp data, it must be a member of an alliance.
"""
from xml.dom import minidom
import os
import sys
from datetime import datetime

if __name__ == "__main__":
    # Only mess with the environmental stuff if this is being ran directly.
    from importer_path import fix_environment
    fix_environment() 

from django.conf import settings
from apps.eve_db.models import EVEPlayerAlliance, EVEPlayerCorporation
from apps.eve_proxy.models import CachedDocument

def __update_corp(corp, xml_data):
    #print xml_data
    dom = minidom.parseString(xml_data)
    if len(dom.getElementsByTagName('error code')) > 0:
        # This corp is probably not in an alliance anymore. The API only lets
        # you get info on corps in alliances.
        return
    
    # Tuples of pairings of tag names and the attribute on the Corporation
    # object to set the data to.
    tag_mappings = (
        ('corporationName', 'name'),
        ('ticker', 'ticker'),
        ('url', 'url'),
        ('description', 'description'),
        ('memberCount', 'member_count'),
        ('graphicID', 'logo_graphic_id'),
        ('shape1', 'logo_shape1'),
        ('shape2', 'logo_shape2'),
        ('shape3', 'logo_shape3'),
        ('color1', 'logo_color1'),
        ('color2', 'logo_color2'),
        ('color3', 'logo_color3'),
    )
    
    # Iterate through the tag mappings, setting the values of the tag names
    # (first member of the tuple) to the attribute named in the second member
    # of the tuple on the EVEPlayerCorporation object.
    for tag_map in tag_mappings:
        try:
            setattr(corp, tag_map[1], dom.getElementsByTagName(tag_map[0])[0].firstChild.nodeValue)
        except AttributeError:
            # This tag has no value, skip it.
            continue
        except IndexError:
            # Something weird has happened
            print " * Index Error:", tag_map[0]
            print xml_data
            continue 
    print "Updating", corp.id, corp.name
    corp.save()
    
def query_and_update_corp(corp):
    """
    Just updates one corp object.
    
    corp: (EVEPlayerCorporation)
    """
    corp_doc = CachedDocument.objects.api_query('/corp/CorporationSheet.xml.aspx',
                                                params={'corporationID': corp.id})
    __update_corp(corp, corp_doc.body)

def __start_import():
    """
    Imports all of the corps that are in all of the known alliances.
    """
    for alliance in EVEPlayerAlliance.objects.all():
        member_corps = alliance.eveplayercorporation_set.all()
        # We're getting the list of corps to update from alliance memberships.
        for corp in member_corps:
            print "Querying", corp.id
            query_and_update_corp(corp)
    
if __name__ == "__main__":
    __start_import()