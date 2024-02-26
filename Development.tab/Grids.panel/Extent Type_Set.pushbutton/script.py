# -*- coding: utf-8 -*-
"""Declare coding style"""

__title__ = 'Set Extent 2D/3D'
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
import os
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

# pyRevit Imports

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


# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# ---------------------------------------------------------
t = Transaction(doc, 'Change Name')
t.Start()

all_grids = (FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_Grids).
             WhereElementIsNotElementType().ToElements())


# Change Datum Extent Type
for grid in all_grids:
    grid = grid  # type: Grid

    # Set to 3D Extent Type
    grid.SetDatumExtentType(DatumEnds.End0, active_view, DatumExtentType.Model)
    grid.SetDatumExtentType(DatumEnds.End1, active_view, DatumExtentType.Model)


    # Set to 2D Extent right after to the 3D extent of grid
    grid.SetDatumExtentType(DatumEnds.End0, active_view, DatumExtentType.ViewSpecific)
    grid.SetDatumExtentType(DatumEnds.End1, active_view, DatumExtentType.ViewSpecific)

t.Commit()

# ---------------------------------------------------------
print('-' * 50)
print('Script is finished')
print('Developed by Hung Nguyen.')
