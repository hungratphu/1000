# -*- coding: utf-8 -*-
"""Declare coding style"""

__title__ = 'Set Extent Type'
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

# get_curves_in_view = datum.GetCurvesInView(DatumExtentType.Model, active_view)
# line = get_curves_in_view[0]
# print(line)
# print(type(line))
# print('-'*50)


# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# ---------------------------------------------------------
t = Transaction(doc, 'Change Name')
t.Start()

# UnCrop Active View


# Change Datum Extent Type
for grid in all_grids:
    grid = grid  # type: Grid

    # Set to 3D Extent Type
    grid.SetDatumExtentType(DatumEnds.End0, active_view, DatumExtentType.Model)
    grid.SetDatumExtentType(DatumEnds.End1, active_view, DatumExtentType.Model)

    # TEST
    # grid.SetCurveInView(DatumExtentType.Model, active_view, get_curves_in_view[0])

    # Set to 2D Extent Right after
    grid.SetDatumExtentType(DatumEnds.End0, active_view, DatumExtentType.ViewSpecific)
    grid.SetDatumExtentType(DatumEnds.End1, active_view, DatumExtentType.ViewSpecific)

t.Commit()

# ---------------------------------------------------------
print('-' * 50)
print('Script is finished')
print('Developed by Hung Nguyen.')
