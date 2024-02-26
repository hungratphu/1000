# -*- coding: utf-8 -*-
"""Declare coding style"""

__title__ = 'Match Leader'
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
from Snippets._datumplane import *


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc         = __revit__.ActiveUIDocument.Document   # type: Document
uidoc       = __revit__.ActiveUIDocument            # type: UIDocument
app         = __revit__.Application                 # Application class
selection   = uidoc.Selection                     # type: Selection

active_view     = doc.ActiveView
active_level    = active_view.GenLevel
rvt_year        = int(app.VersionNumber)
PATH_SCRIPT     = os.path.dirname(__file__)


# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# ---------------------------------------------------------
tg = TransactionGroup(doc, '1000: Match Leader')
tg.Start()

all_grids = (FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_Grids).
             WhereElementIsNotElementType().ToElements())

from_view = doc.GetElement(ElementId(312)) #type: View
to_view = active_view


for grid in all_grids:
    grid = grid  # type: Grid

    t1 = Transaction(doc, "Add Leader")
    t1.Start()
    add_grid_leaders(grid, to_view)
    t1.Commit()
    # -----------------------------------------

    t2 = Transaction(doc, "Straighten Leader")
    t2.Start()
    # straighten_grid_leaders(grid, to_view)
    t2.Commit()
    # -----------------------------------------

    t3 = Transaction(doc, "Match Leader XYZ")
    t3.Start()
    from_leader_0,  from_leader_1   = get_grid_leaders(grid, from_view)
    to_leader_0,    to_leader_1     = get_grid_leaders(grid, to_view)

    new_leader_0 = match_leaders_xyz(from_leader_0, to_leader_0)
    new_leader_1 = match_leaders_xyz(from_leader_1, to_leader_1)

    t3.Commit()
    # -----------------------------------------

    t4 = Transaction(doc, "Set Leader")
    t4.Start()
    set_leaders(grid, to_view, new_leader_0, new_leader_1)
    t4.Commit()
    # -----------------------------------------

    t5 = Transaction(doc, "Straight leader if from_leader is None or Straight")
    t5.Start()
    leader_0, leader_1 = get_grid_leaders(grid, active_view)

    if (from_leader_0 is None) or \
       (from_leader_0 and from_leader_0.LeaderShape == LeaderShape.Straight):
        straight_grid_leader_0(grid, active_view, leader_0)

    if (from_leader_1 is None) or \
       (from_leader_1 and from_leader_1.LeaderShape == LeaderShape.Straight):
        straight_grid_leader_1(grid, active_view, leader_1)

    print("|"*50)
    t5.Commit()
    # -----------------------------------------

    t6 = Transaction(doc, "Match grid bubble")
    t6.Start()
    from_bubble_is_visible_0, from_bubble_visible_1 = is_grid_bubble_visible(grid, from_view)

    if from_bubble_is_visible_0:
        grid.ShowBubbleInView(DatumEnds.End0, to_view)
    else:
        grid.HideBubbleInView(DatumEnds.End0, to_view)

    if from_bubble_visible_1:
        grid.ShowBubbleInView(DatumEnds.End1, to_view)
    else:
        grid.HideBubbleInView(DatumEnds.End1, to_view)

    t6.Commit()

tg.Assimilate()

# ---------------------------------------------------------
print('-' * 50)
print('Script is finished')
print('Developed by Hung Nguyen.')