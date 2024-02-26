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
PATH_SCRIPT     = os.path.dirname(__file__)

# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
# class Custom_Filter(ISelectionFilter):
#
#     def AllowElement(self, element):            #type: (Element)
#         if element.Category.BuiltInCategory == BuiltInCategory.OST_Rooms:
#             return True


# def GetRoomsByRectangle():
#
#     selFilter = Custom_Filter()
#     eList = selection.PickElementsByRectangle(selFilter, "Select multiple rooms")
#     return eList

#
# custom_filter = Custom_Filter()
# selected_elements = selection.PickElementsByRectangle(custom_filter, "Select rooms")
# for e in selected_elements:
#     print(e)
# ---------------------------------------------------------

from Autodesk.Revit.UI.Selection import ISelectionFilter
#
# class ISelectionFilter_Classes(ISelectionFilter):
#     def __init__(self, allowed_classes):
#         self.allowed_classes = allowed_classes
#
#     def AllowElement(self, elem):
#         if type(elem) in self.allowed_classes:
#             return True
#
#
# class ISelectionFilter_Categories(ISelectionFilter):
#     def __init__(self, allowed_categories):
#         self.allowed_categories = allowed_categories
#
#     def AllowElement(self, element):
#         if element.Category.BuiltInCategory in self.allowed_categories:
#             return True

from Snippets._selection import ISelectionFilter_Classes, ISelectionFilter_Categories

filter_cats       = ISelectionFilter_Categories([BuiltInCategory.OST_Walls, BuiltInCategory.OST_Dimensions])
selected_elements = selection.PickElementsByRectangle(filter_cats)
for e in selected_elements:
    print (e)

# ---------------------------------------------------------
print('-'*50)
print('Script is finished')
print('Developed by Hung Nguyen.')
