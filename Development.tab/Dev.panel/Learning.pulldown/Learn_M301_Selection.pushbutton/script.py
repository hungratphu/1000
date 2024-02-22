# -*- coding: utf-8 -*-
"""Declare coding style"""

__title__ = ''
__doc__ = """
Date    = 2023.Dec.03
---------------------------------------------------------
Description:
Learning Selection Class under Autodesk.Revit.UI.Selection
---------------------------------------------------------
Author: Hung Nguyen """

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
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
doc     = __revit__.ActiveUIDocument.Document   #type: Document
uidoc   = __revit__.ActiveUIDocument            #type: UIDocument
app     = __revit__.Application                 # Application class
selection = uidoc.Selection                     #type: Selection

active_view     = doc.ActiveView
active_level    = active_view.GenLevel
rvt_year        = int(app.VersionNumber)

# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ✅ 1. GetElement & GetElementIds
# ---------------------------------------------------------
# selected_element_ids = selection.GetElementIds()
#
# for e_id in selected_element_ids:
#     e = doc.GetElement(e_id)
#     print (e, e_id)
#
#     if type(e) == Room:
#         print("This is a Room")
#     if type(e) == Wall:
#         print("This is a Wall")
#     if type(e) == RoomTag:
#         print("This is a RoomTag")

# ✅ 2. PickObject
# ---------------------------------------------------------
# ref_pick_object = selection.PickObject(ObjectType.Element)
# pick_object = doc.GetElement(ref_pick_object)
# print(pick_object, pick_object.Id)


# ✅ 3. PickObjects (Pick Multiple Objects)
# ---------------------------------------------------------
# ref_pick_objects = selection.PickObjects(ObjectType.Element)
# for ref_obj in ref_pick_objects:
#     pick_objects = doc.GetElement(ref_obj)
#     print (pick_objects, pick_objects.Id.Value)

# ✅4. PickElementsByRectangle
# ---------------------------------------------------------
# selected_elements_by_rec = selection.PickElementsByRectangle()
# print(selected_elements_by_rec)

# ✅ 5. Pick Box
# ---------------------------------------------------------
# picked_box = selection.PickBox(PickBoxStyle.Directional)
# min_box = picked_box.Min
# max_box = picked_box.Max
# print("Min:", min_box.X, min_box.Y, min_box.Z)
# print("Max:", max_box.X, max_box.Y, max_box.Z)

# ✅ 6. Set Selection in Revit UI
# ---------------------------------------------------------
# new_ids_list = List[ElementId]()
# new_ids_list.Add(ElementId(313430))
# new_ids_list.Add(ElementId(313468))
# new_ids_list.Add(ElementId(313599))
# new_ids_list.Add(ElementId(313628))
#
# selection.SetElementIds(new_ids_list)

# ✅ 7. Pick Point
# ---------------------------------------------------------
# pick_point = selection.PickPoint()
# print(pick_point)

# We don't change anything so no need for Transaction
# t = Transaction(doc, 'Change Name')
# t.Start()
#
# t.Commit()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print('-'*50)
print('Script is finished')
print('Developed by Hung Nguyen.')
