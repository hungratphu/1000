# -*- coding: utf-8 -*-
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
from pyrevit import forms

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
doc         = __revit__.ActiveUIDocument.Document   # type: Document
uidoc       = __revit__.ActiveUIDocument            # type: UIDocument
app         = __revit__.Application                 # Application class
selection   = uidoc.Selection                       # type: Selection

active_view     = doc.ActiveView
active_level    = active_view.GenLevel


# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# ---------------------------------------------------------
# Get all grids in active view
all_grids = (FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_Grids).
             WhereElementIsNotElementType().ToElements())

# Select view base
view_base = forms.select_views(
    title='Select View Base',
    button_name='Select View',
    multiple=False,
    filterfunc=lambda x: x.ViewType == ViewType.FloorPlan or x.ViewType == ViewType.CeilingPlan)

# Select set of views to match
views_set = forms.select_views(
    title='Select View To Match Grid Leader',
    button_name='Select Views',
    multiple=True,
    filterfunc=lambda x: (x.ViewType == ViewType.FloorPlan or x.ViewType == ViewType.CeilingPlan) and x.Id != view_base.Id
    )

from_view = view_base  # type: View

# Start Transaction Group
tg = TransactionGroup(doc, '1000: Match Leader')
tg.Start()

# Start the iteration
for to_view in views_set:
    for grid in all_grids:  # type: Grid

        # -----------------------------------------

        with transaction(doc, "Add Leader", True):
            add_grid_leaders(grid, to_view)

        # -----------------------------------------

        with transaction(doc, "Match Leader XYZ", True):
            from_leader_0,  from_leader_1   = get_grid_leaders(grid, from_view)
            to_leader_0,    to_leader_1     = get_grid_leaders(grid, to_view)

            new_leader_0 = match_leaders_xyz(from_leader_0, to_leader_0)
            new_leader_1 = match_leaders_xyz(from_leader_1, to_leader_1)

        # -----------------------------------------

        with transaction(doc, "Set Leader", True):
            set_leaders(grid, to_view, new_leader_0, new_leader_1)

        # -----------------------------------------

        with transaction(doc, "Straight leader if from_leader is None or Straight", True):
            leader_0, leader_1 = get_grid_leaders(grid, active_view)

            if (from_leader_0 is None) or \
                    (from_leader_0 and from_leader_0.LeaderShape == LeaderShape.Straight):
                straight_grid_leader_0(grid, active_view, leader_0)

            if (from_leader_1 is None) or \
                    (from_leader_1 and from_leader_1.LeaderShape == LeaderShape.Straight):
                straight_grid_leader_1(grid, active_view, leader_1)


        # -----------------------------------------

        with transaction(doc, "Match grid bubble", True):
            from_bubble_is_visible_0, from_bubble_visible_1 = is_grid_bubble_visible(grid, from_view)

            if from_bubble_is_visible_0:
                grid.ShowBubbleInView(DatumEnds.End0, to_view)
            else:
                grid.HideBubbleInView(DatumEnds.End0, to_view)

            if from_bubble_visible_1:
                grid.ShowBubbleInView(DatumEnds.End1, to_view)
            else:
                grid.HideBubbleInView(DatumEnds.End1, to_view)

        print("Wonderful!")
        # -----------------------------------------

    print(to_view.Name, "DONE")

tg.Assimilate()

# ---------------------------------------------------------
print('-' * 50)
print('Script is finished')
print('Developed by Hung Nguyen.')
