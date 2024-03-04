# -*- coding: utf-8 -*-
__title__ = 'Straighten Leader'
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

# .NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List

# Custom Imports
from Snippets._datumplane import *
from Snippets._transaction import *


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc         = __revit__.ActiveUIDocument.Document       # type: Document
uidoc       = __revit__.ActiveUIDocument                # type: UIDocument
app         = __revit__.Application                     # Application class
selection   = uidoc.Selection                           # type: Selection

active_view = doc.ActiveView
active_level = active_view.GenLevel


# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# ---------------------------------------------------------
all_grids = (FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_Grids).
             WhereElementIsNotElementType().ToElements())

view = doc.GetElement(ElementId(8929216))

tg = TransactionGroup(doc, '1000: Straighten Leaders')
tg.Start()

for grid in all_grids:
    grid = grid  # type: Grid

    with transaction(doc, "Straighten Leader", True):
        leader_0, leader_1 = straighten_grid_leaders(grid, active_view)

    with transaction(doc, "Reader New Leader XYZ", True):
        print("GRID NAME: ", grid.Name)
        leader_straight_0, leader_straight_1 = get_grid_leaders(grid, active_view)
        get_grid_leader_xyz(leader_straight_0, True)
        get_grid_leader_xyz(leader_straight_1, True)

tg.Assimilate()

# ---------------------------------------------------------
print('-' * 50)
print('Script is finished')
print('Developed by Hung Nguyen.')
