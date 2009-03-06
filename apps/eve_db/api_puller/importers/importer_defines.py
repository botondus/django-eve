"""
Generally static configuration/definitions for the importers to reference.
"""
import os
import sys
import httplib
import urllib
from django.conf import settings

# Standard EVE API location
API_URL = 'api.eve-online.com'

def retrieve_api_xml(api_path, user_id=settings.EVE_API_USER_ID, 
                     api_key=settings.EVE_API_USER_KEY, other_parameters=None):
    # setup the parameters we will be sending to the webserver; note that all of this
    # information is gathered from the API Key page that the user should visit, and
    # the characterID is gathered from /account/Characters.xml.aspx
    param_dict = {}
    if user_id:
        param_dict['userID'] = user_id
    if api_key:
        param_dict['apikey'] = api_key
    if other_parameters:
        # Merge the parameters into param_dict, over-write from other_parameters
        # as needed.
        param_dict.update(other_parameters)

    # Encode the URL parameters (replace spaces with %20, etc.)
    params = urllib.urlencode(param_dict)
    
    # connect to server, POST our request, fairly simple stuff...
    headers = { "Content-type": "application/x-www-form-urlencoded" }
    conn = httplib.HTTPConnection(API_URL)
    conn.request("POST", api_path, params, headers)
    
    # now get response from server, print out the status code for debugging
    response = conn.getresponse()
    data = response.read()
    
    # Clean up
    conn.close()
    return data
    
