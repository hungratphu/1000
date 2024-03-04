# -*- coding: utf-8 -*-
__title__ = 'Hide Dimension'
__author__ = "Hung Nguyen"
__doc__ = """
Date    = 2023.Nov.27
---------------------------------------------------------
Author: Hung Nguyen """



# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
import os
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

# .NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List

# Custom Imports
from Snippets._transaction import *

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc     = __revit__.ActiveUIDocument.Document
uidoc   = __revit__.ActiveUIDocument
app     = __revit__.Application

active_view     = doc.ActiveView
active_level    = active_view.GenLevel

# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
all_dimensions      = (FilteredElementCollector(doc).
                       OfCategory(BuiltInCategory.OST_Dimensions).
                       WhereElementIsNotElementType().
                       ToElements())

filter_dimensions   = [dims.Id for dims in all_dimensions if dims.Name == "MS Metric Dimension 2.5mm"]

list_dims_ids       = List[ElementId](filter_dimensions)

print("There are total {} Dimensions elements.".format(len(all_dimensions)))
print("There are total {} Dimensions elements as 'MS Metric Dimension 2.5mm'.".format(len(filter_dimensions)))


with transaction(doc, "1000: Hide Dims", True):
    active_view.HideElements(list_dims_ids)

# ---------------------------------------------------------
print('-'*50)
print('Script is finished')
