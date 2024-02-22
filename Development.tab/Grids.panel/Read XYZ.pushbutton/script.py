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

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ---------------------------------------------------------
def GetInfo_Grid(grid):
    message = "Grid : "

    # Show IsCurved property
    message += "\nIf grid is Arc : " + str(grid.IsCurved)

    # Show Curve information
    curve = grid.Curve
    if grid.IsCurved:
        # if the curve is an arc, give center and radius information
        arc = curve.AsCurve()
        message += "\nArc's radius: " + str(arc.Radius)
        message += "\nArc's center:  (" + XYZString(arc.Center)
    else:
        # if the curve is a line, give length information
        line = curve.AsCurve()
        message += "\nLine's Length: " + str(line.Length)
    # Get curve start point
    message += "\nStart point: " + XYZString(curve.GetEndPoint(0))
    # Get curve end point
    message += "; End point: " + XYZString(curve.GetEndPoint(1))

    TaskDialog.Show("Revit", message)

# output the point's three coordinates
def XYZString(point):
    return "(" + str(point.X) + ", " + str(point.Y) + ", " + str(point.Z) + ")"


# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
grids_in_view = FilteredElementCollector(doc, active_view).OfCategory(BuiltInCategory.OST_Grids).WhereElementIsNotElementType().ToElements()





# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# ---------------------------------------------------------
# t = Transaction(doc, 'Change Name')
# t.Start()
#
# t.Commit()

# ---------------------------------------------------------
print('-'*50)
print('Script is finished')
print('Developed by Hung Nguyen.')
