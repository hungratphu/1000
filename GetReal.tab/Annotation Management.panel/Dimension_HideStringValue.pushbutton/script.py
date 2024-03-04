# -*- coding: utf-8 -*-
__title__ = 'Hide Dimension String Value'
__doc__ = """
Date    = 2023.Dec.06
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
from Autodesk.Revit.DB import Dimension, DimensionSegmentArray
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI. Selection import *


# .NET Imports
import clr
clr.AddReference('System')

# Custom Imports
from Snippets._transaction import *

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc             = __revit__.ActiveUIDocument.Document   #type: Document
uidoc           = __revit__.ActiveUIDocument            #type: UIDocument
app             = __revit__.Application                 # Application class
selection       = uidoc.Selection                       #type: Selection
active_view     = doc.ActiveView

# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
# ✌️1️⃣ Get dimension in active view
all_dims = FilteredElementCollector(doc, active_view.Id).OfClass(Dimension).WhereElementIsNotElementType().ToElements()


# ✌️2️⃣ Filter dimensions and get segments in a single step
dim_segments = [seg for dim in all_dims if dim.NumberOfSegments > 1 for seg in dim.Segments]


# ✌️3️⃣ Filter segments with ValueString
dim_seg_list = [seg for seg in dim_segments if seg.ValueString == '130']
print("Hide {} dimensions".format(len(dim_seg_list)))


# ✌️4️⃣ Transaction to override values
with transaction(doc, "Override Dimension Value", True):
    for dim_seg in dim_seg_list:
        dim_seg.ValueOverride = "‌"
        dim_seg.ResetTextPosition()