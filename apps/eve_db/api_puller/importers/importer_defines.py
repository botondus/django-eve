"""
Generally static configuration/definitions for the importers to reference.
"""
import os
import sys

# The path to the folder containing settings.py.
FRAMEWORK_BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))