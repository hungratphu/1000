# -*- coding: utf-8 -*-
__title__ = 'Get Extent Type'
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
from Autodesk.Revit.UI.Selection import *
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
doc = __revit__.ActiveUIDocument.Document  # type: Document
uidoc = __revit__.ActiveUIDocument  # type: UIDocument
app = __revit__.Application  # Application class
selection = uidoc.Selection  # type: Selection

active_view = doc.ActiveView
active_level = active_view.GenLevel
rvt_year = int(app.VersionNumber)
PATH_SCRIPT = os.path.dirname(__file__)

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ---------------------------------------------------------


# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
# Filter all grids in view:
all_grids = (FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_Grids).
             WhereElementIsNotElementType().ToElements())

for grid in all_grids:
    grid = grid  # type: Grid

    # Get 3D Extent Type
    datum_extend_type_end_0 = grid.GetDatumExtentTypeInView(DatumEnds.End0, active_view)
    datum_extend_type_end_1 = grid.GetDatumExtentTypeInView(DatumEnds.End1, active_view)

    print("GRID: ", grid.Name, ":", datum_extend_type_end_0, "|", datum_extend_type_end_1)


# ---------------------------------------------------------
print('-' * 50)
print('Script is finished')
print('Developed by Hung Nguyen.')
