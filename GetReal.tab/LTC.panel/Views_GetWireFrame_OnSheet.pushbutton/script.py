# -*- coding: utf-8 -*-
__title__ = 'Get Wire Frame Views'
__doc__ = """
Date    = 2023.Dec.03
---------------------------------------------------------
Description:
---------------------------------------------------------
Author: Hung Nguyen """

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
import os, sys, datetime, time
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI. Selection import *
from Autodesk.Revit.DB.Architecture import *

# pyRevit Imports
from pyrevit import forms, revit, script

# .NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List

# Custom Imports

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc             = __revit__.ActiveUIDocument.Document   #type: Document
uidoc           = __revit__.ActiveUIDocument            #type: UIDocument
app             = __revit__.Application                 # Application class
selection       = uidoc.Selection                       #type: Selection

active_view     = doc.ActiveView
active_level    = active_view.GenLevel
rvt_year        = int(app.VersionNumber)
PATH_SCRIPT     = os.path.dirname(__file__)

# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
# ✌️Get and filter views on sheets
collector = FilteredElementCollector(doc).OfClass(View).WhereElementIsNotElementType().ToElements()

filter_view = [view for view in collector if
               view.GetPlacementOnSheetStatus() == ViewPlacementOnSheetStatus.CompletelyPlaced
               and view.DisplayStyle == DisplayStyle.Wireframe]


from pyrevit import script

output = script.get_output()

for view in filter_view:
    print(output.linkify(view.Id, view.Name))

# ---------------------------------------------------------
print('-'*50)
print('Script is finished')
print('Developed by Hung Nguyen.')
