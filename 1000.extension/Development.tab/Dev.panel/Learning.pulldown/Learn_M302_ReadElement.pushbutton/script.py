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
import sys
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
from Snippets._convert import convert_units

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

# 👉 PickObject
ref_obj         = selection.PickObject(ObjectType.Element)    #type: Reference
elem            = doc.GetElement(ref_obj)                     #type: Element
elem_spatial    = elem                                        #type: SpatialElement
elem_room       = elem                                        #type: Room
elem_id         = elem.Id

# 🔎 Check element
if type(elem) != Room:
    print("This is a Room. Try again")
    sys.exit()

print(elem)
print("ElementId: {}".format(elem_id))
print("CreatedPhasedId: {}".format(elem.CreatedPhaseId))
print("DemolishedPhasedId: {}".format(elem.DemolishedPhaseId))

if elem.GroupId == ElementId(-1):
    print("GroupId: None ---> This is not part of a group!!!")
else:
    print("GroupId: {}".format(elem.GroupId))

level_id = elem.LevelId
level = doc.GetElement(level_id)
print("Level Name: {}".format(level.Name))
print("Name: {}".format(Element.Name.GetValue(elem))) # Use this to get the room name
print("CanBeHidden: {}".format(elem.CanBeHidden(active_view)))
print("CanBeLocked: {}".format(elem.CanBeLocked()))
print("GetMaterialArea: {}".format(elem.GetMaterialArea(elem.Id, False)))
print("GetMaterialIds: {}".format(elem.GetMaterialIds(True)))
print("IsHidden: {}".format(elem.IsHidden(active_view)))
print("RoomNumber: {}".format(elem_room.Number))
print("Area: {} ft2".format(elem_room.Area))
print("Perimeter: {} ft".format(elem_room.Perimeter))

area_mm = convert_units(elem_room.Area, "mm2", True)
perimeter_mm = convert_units(elem_room.Perimeter, "mm", True)
area_m = convert_units(elem_room.Area, "m2", True)
perimeter_m = convert_units(elem_room.Perimeter, "m", True)

print("Area: {} mm2".format(area_mm))
print("Perimeter: {} mm".format(perimeter_mm))
print("Area: {} m2".format(area_m))
print("Perimeter: {} m".format(perimeter_m))


boundary_segments = elem_spatial.GetBoundarySegments(SpatialElementBoundaryOptions())
print("BoundarySegment: {}".format(boundary_segments))


# We don't change anything so no need for Transaction
# t = Transaction(doc, 'Change Name')
# t.Start()
#
# t.Commit()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print('-'*50)
print('Script is finished')
print('Developed by Hung Nguyen.')
