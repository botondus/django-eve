#!/usr/bin/env python
"""
Import race data.

Tables imported:
chrRaces
"""
import os
import sqlite3
import constants

# Setup the Django environment if this is being executed directly.
if __name__ == "_main__":
    constants.setup_environment()

def do_import():
    """
    Handle the import.
    """
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    
    for row in c.execute('select * from chrRaces'):
        print row['raceName']

    # Clean up.
    c.close()

if __name__ == "__main__":
    do_import()