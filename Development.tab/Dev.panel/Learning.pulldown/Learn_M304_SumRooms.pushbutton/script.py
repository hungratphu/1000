# -*- coding: utf-8 -*-
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
from Snippets._selection import ISelectionFilter_Categories

# 1️⃣a. Get Rooms from current selection within the project
current_selected_elements = [doc.GetElement(e) for e in selection.GetElementIds()]
selected_rooms = [room for room in current_selected_elements if type(room) == Room]


# 1️⃣b. Prompt to pick rooms if not selected
if not selected_rooms:
    filter_categories = ISelectionFilter_Categories([BuiltInCategory.OST_Rooms])
    pick_rooms_ref = selection.PickObjects(ObjectType.Element, filter_categories, "There are no room selected, Please pick rooms")
    selected_rooms = [doc.GetElement(ref) for ref in pick_rooms_ref]


# 1️⃣c. Prompt Alert to user
if not selected_rooms:
    from pyrevit import forms
    forms.alert("There are no Rooms selected. Please try again",
                title="Alert",
                ok= False,
                cancel = True,
                exitscript = True)

# 2️⃣ Get Room Properties & Sum Room Area
from Snippets._convert import convert_units


total = 0
for room in selected_rooms:
    room_name = room.get_Parameter(BuiltInParameter.ROOM_NAME).AsString()
    area_m2 = convert_units(room.Area, "m2")
    area_round = round(area_m2, 2)
    total += area_round

    print("{} {}: {} m2".format(room_name, room.Number, area_round))

# 3️⃣ Display result:
print("Total area = {} m2".format(total))
print("Selected from {} rooms".format(len(selected_rooms)))

# ---------------------------------------------------------
print('-'*50)
print('Script is finished')
print('Developed by Hung Nguyen.')
