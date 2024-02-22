# -*- coding: utf-8 -*-
"""Declare coding style"""

__title__ = ''
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
from Autodesk.Revit.UI. Selection import *
from Autodesk.Revit.DB.Architecture import *

# pyRevit Imports
from pyrevit import forms, revit, script

# .NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List

# Custom Imports
from Snippets._convert import convert_mm_to_internal

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

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ---------------------------------------------------------


# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
# 2️⃣ Filter levels
all_levels = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Levels).WhereElementIsNotElementType().ToElements()

for level in all_levels:
    if level.Name == 'T/O SECOND FL SLAB':
        level_filter = ElementLevelFilter(level.Id)
        # rule = ElementParameterFilter(filterable_value_provider, filter_string_rule_evaluator, )
        walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WherePasses(level_filter).WhereElementIsNotElementType().ToElements() #type: Wall

        filter_wall_list = [wall.Id for wall in walls if wall.WallType.Function == WallFunction.Interior]
        # new_ids_list = List[ElementId]()
        wall_ids_list = List[ElementId](filter_wall_list)
        #
        # for wall_id in filter_wall_list:
        #     new_ids_list.Add(wall_id)

        # set_current_elements = selection.SetElementIds(new_ids_list)
        set_current_elements = selection.SetElementIds([wall_ids_list])



t = Transaction(doc, 'Change Name')
t.Start()

t.Commit()

# ---------------------------------------------------------
print('-'*50)
print('Script is finished')
print('Developed by Hung Nguyen.')
