#!/usr/bin/env python
import os
import sys
from optparse import OptionParser
# Setup Django environment.
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import util

def list_tables(option, opt, value, parser):
    """
    Prints a list of tables that are available for import.
    """
    print "CCP Data Dump Table List"
    print "------------------------"
    for table in util.IMPORT_LIST:
        print "%s" % table.__name__.replace('import_', '')
    print "-- %d tables --" % len(util.IMPORT_LIST)

description = """
              This importer script will either import one or all tables from
              the CCP data dump.
              """

parser = OptionParser(usage="Usage: %prog [-i] table_name")
parser.add_option("-i", "--include-deps", action="store_true",
                  dest="include_deps", default=False,
                  help="Import the other tables that the specified table depends on.")
parser.add_option("-l", "--list", action="callback",
                  callback=list_tables,
                  help="List all of the tables in the CCP dump.")

(options, args) = parser.parse_args()
print "OPTIONS", options
print "ARGS:", args

if len(args) == 0:
    print "No table names specified, importing all."
    util.run_importers(util.IMPORT_LIST)
else:
    print "Importing: %s" % args