"""
Some useful constants for the importers.
"""
import os
import sys

# Path to the SQLite dump to be imported.
DB_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       'apo131-sqlite3-v1.db')

def setup_environment():
    """
    Modifies the sys.path to allow these scripts to be ran directly.
    """
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, project_root)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    
def parse_int_bool(int_bool):
    """
    Takes an int and converts it to a bool in the basis of 1=True, 0=False.
    """
    if int_bool == 1:
        return True
    else:
        return False