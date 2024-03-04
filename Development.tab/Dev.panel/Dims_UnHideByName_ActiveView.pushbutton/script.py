# -*- coding: utf-8 -*-
__title__ = "UnHide Dimension"
__author__ = "Hung Nguyen"
__doc__ = """
Date    = 2023.Nov.27
---------------------------------------------------------
Author: Hung Nguyen """


# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
import os, sys, datetime, time
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB.Architecture import *

# pyRevit Imports
from pyrevit import forms, revit, script

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
doc     = __revit__.ActiveUIDocument.Document   #type: Document
uidoc   = __revit__.ActiveUIDocument            #type: UIDocument
app     = __revit__.Application                 # Application class

active_view     = doc.ActiveView
active_level    = active_view.GenLevel
rvt_year        = int(app.VersionNumber)
PATH_SCRIPT     = os.path.dirname(__file__)

all_dimensions = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Dimensions).WhereElementIsNotElementType().ToElements()
filter_dimensions = [dims.Id for dims in all_dimensions if dims.Name == "MS Metric Dimension 2.5mm"]
list_dims_ids     = List[ElementId](filter_dimensions)
print("There are total {} Dimensions elements.".format(len(all_dimensions)))
print("There are total {} Dimensions elements as 'MS Metric Dimension 2.5mm'.".format(len(filter_dimensions)))

# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------

with transaction(doc, "1000: Unhide Dims", True):
    active_view.UnhideElements(list_dims_ids)

# ---------------------------------------------------------
print('-'*50)
print('Script is finished')
