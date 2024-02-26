# -*- coding: utf-8 -*-
"""Declare coding style"""

__title__ = 'Change Leader Z'
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
t = Transaction(doc, '1000: Change Leader')
t.Start()

all_grids = (FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_Grids).
             WhereElementIsNotElementType().ToElements())

for grid in all_grids:
    grid = grid  # type: Grid

    leader_0, leader_1 = get_grid_leaders(grid, active_view)

    #
    def create_new_leader(new_leader, from_leader):
        # type: (Leader, Leader) -> Leader

        from_elbow = from_leader.Elbow
        from_end = from_leader.End

        new_leader.End = XYZ(from_end.X, from_end.Y, new_leader.End.Z)
        new_leader.Elbow = XYZ(from_elbow.X, from_elbow.Y, new_leader.End.Z)

        return new_leader

    # new_leader_0 = create_new_leader(leader_0, leader_0)
    # new_leader_1 = create_new_leader(leader_1, leader_1)
    # get_grid_leader_xyz(new_leader_1, True)
    # get_grid_leader_xyz(new_leader_1,True)


    # print("Is Leader Valid: ", grid.IsLeaderValid(DatumEnds.End0, active_view, new_leader_0))
    # print("Is Leader Valid: ", grid.IsLeaderValid(DatumEnds.End1, active_view, new_leader_1))


    def add_leader_elbow(leader, add_elbow=True):
        # type: (Leader, bool) -> Leader

        end     = leader.End
        elbow   = None
        anchor  = leader.Anchor

        if add_elbow:
            elbow = XYZ(end.X + (anchor.X - end.X) / 2,
                        anchor.Y,
                        anchor.Z)
        else:
            elbow = XYZ(anchor.X, anchor.Y, anchor.Z)

        leader.Elbow = elbow
        return leader

    new_center_leader = add_leader_elbow(leader_1, True)
    get_grid_leader_xyz(new_center_leader, True)
    print("Is Leader Valid: ", grid.IsLeaderValid(DatumEnds.End1, active_view, new_center_leader))


    if grid.IsLeaderValid(DatumEnds.End1, active_view, new_center_leader):
        grid.SetLeader(DatumEnds.End1, active_view, new_center_leader)

t.Commit()

# ---------------------------------------------------------
print('-' * 50)
print('Script is finished')
print('Developed by Hung Nguyen.')
