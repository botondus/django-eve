#!/usr/bin/env python
"""
This module is primarily used directly by the developer to import one or more
tables from the CCP data dump. The best way to see how to use this as a
command-line utility is to run it with the -h option.
"""
import os
import sys
from optparse import OptionParser
# Setup Django environment.
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import util
import importers

def exit_with_error(error_msg):
    """
    Gracefully kills the script when an error was occured.
    """
    parser.error(error_msg)
    
def exit_with_succ():
    """
    Nothing to see here, move along.
    """
    sys.exit(0)

def instantiate_parser():
    """
    Instantiates and configures the OptionParser.
    """
    description = """This importer script will either import one or all tables from
                     the CCP data dump. If no arguments are specified, all
                     tables will be imported."""
    parser = OptionParser(description=description,
                          usage="Usage: %prog [-i] [table_name1] [table_name2] [...]")
    parser.add_option("-i", "--include-deps", action="store_true",
                      dest="include_deps", default=False,
                      help="""Import the other tables that the specified table 
                              [recursively] depends on.""")
    parser.add_option("-l", "--list", action="callback",
                      callback=list_tables,
                      help="List all of the tables in the CCP dump and exit.")
    return parser

def list_tables(option, opt, value, parser):
    """
    Prints a list of tables that are available for import.
    """
    print "CCP Data Dump Table List"
    print "------------------------"
    for table in util.IMPORT_LIST:
        print "%s" % table.__name__.replace('import_', '')
    print "-- %d tables --" % len(util.IMPORT_LIST)
    # The -l argument is just used for listing, proceed no further.
    exit_with_succ()

def get_importer_funcs_from_arg_list(arg_list):
    """
    Validates the user input for tables to import against the importer list.
    Returns a list of importer functions. In the event that one of the
    arguments does not match up against an importer function, raise an
    exception so the user may be notified.
    """
    importer_funcs = []
    for arg in arg_list:
        importer_func = getattr(importers, 'import_%s' % arg, False)
        if importer_func not in util.IMPORT_LIST:
            exit_with_error("No such table to import: %s" % arg)
        else:
            importer_funcs.append(importer_func)
    return importer_funcs

#==================
# Begin main logic
#==================
if __name__ == "__main__":
    parser = instantiate_parser()
    (options, args) = parser.parse_args()
    print "OPTIONS", options
    print "ARGS:", args
    
    if len(args) == 0:
        print "No table names specified, importing all."
        util.run_importers(util.IMPORT_LIST)
    else:
        print "Importing: %s" % args
        importers = get_importer_funcs_from_arg_list(args)
        util.run_importers(importers)