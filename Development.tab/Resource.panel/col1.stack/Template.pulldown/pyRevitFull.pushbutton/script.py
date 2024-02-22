# -*- coding: utf-8 -*-


__title__ = ''  # Name of the button displayed in Revit UI
__doc__ = """
Date    = 2023.Nov.11
---------------------------------------------------------
Description:
This is a template file for pyRevit Scripts
---------------------------------------------------------
How-to: (Example)
-> Click on the button
-> Change Settings (optional)
-> Make a change
---------------------------------------------------------
Last update:
- [2023.Nov.11] - 1.1 UPDATE - New Feature
---------------------------------------------------------
To-Do:
- Add ... Feature
---------------------------------------------------------
Author: Hung Nguyen """  # Description of the button displayed in Revit UI
__author__ = "Hung Nguyen"
__helpurl__ = "https://apidocs.co/apps/revit/2024/d4648875-d41a-783b-d5f4-638df39ee413.htm"
__hightlight__ = 'new'  # 'new' or 'updated'
# __min_revit_ver = 2024
# __max_revit_ver = 2024
# __context__ = ["selection"]

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
import os, sys, datetime, time                                          # Regular Imports

from Autodesk.Revit.DB import *                                         # Import everything from DB (good for beginners)
from Autodesk.Revit.DB import Transaction, FilteredElementCollector     # or Import only classes that are used.
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB.Architecture import *

# pyRevit Imports
from pyrevit import forms, revit, script                                # Import pyRevit modules. (Lots of useful features)

# .NET Imports
import clr                                                              # Common Language Runtime. Makes .NET libraries accessible
clr.AddReference('System')                                              # Reference System.dll for import
from System.Collections.Generic import List                             # List<ElementType>() <- it's special type of list from .NET framework that Revit API requires
# List_example = List[ElementID]()                                      # Use .Add() instead of append or put python list of ElementIds in parenthesis

# Custom Imports
# from Snippets._selection import get_selected_elements                 # Import from aaa
# from Snippets._selection import convert_internal_to_m                 # Import from aaa

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc     = __revit__.ActiveUIDocument.Document   #type: Document         # Document class from RevitAPI that represents project. Use to Create, Delete, Modify and Query elements from the project
uidoc   = __revit__.ActiveUIDocument            #type: UIDocument       # UIDocument class from RevitAPI that represents Revit project opened in the Revit UI
app     = __revit__.Application                 # Application class     # Represents the Autodesk Revit Application, providing access to documents, options and other application wide data and settings
                                                                        # __revit__ == Autodesk.Revit.UI.UIApplication

active_view     = doc.ActiveView                                        # Get current open view
active_level    = active_view.GenLevel                                  # Only ViewPlan view
rvt_year        = int(app.VersionNumber)
PATH_SCRIPT     = os.path.dirname(__file__)                             # Absolute path to the folder where script is placed

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ---------------------------------------------------------

# ╔═╗╦  ╔═╗╔═╗╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗║╣ ╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝╚═╝╚═╝ CLASSES
# ---------------------------------------------------------

# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
if __name__ == '__main__':
    # ⌨ START CODE HERE
    # 🔓 Use Transaction to Modify Document
    # (Avoid placing inside of loops)
    t = Transaction(doc, 'Change Name')

    t.Start()           #🔓 Start Transaction
    # Change Here....
    t.Commit()          #🔒 Commit Transaction

# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# ---------------------------------------------------------





# ---------------------------------------------------------
print('-'*50)
print('Script is finished')
print('Template has been developed by Hung Nguyen.')
