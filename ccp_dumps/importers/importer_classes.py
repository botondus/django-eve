"""
This module holds all importer related classes.
"""

class SQLImporter(object):
    """
    Serves as the encapsulating class for importers.
    """
    # A list of other table names that this class depends on (strings).
    dependencies = []
    
    def run_importer(self):
        """
        This needs to be over-ridden on all sub-classes!
        """
        pass