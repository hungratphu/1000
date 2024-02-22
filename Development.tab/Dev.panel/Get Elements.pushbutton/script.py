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

# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
# ✌️ Get Elements by Type/Family name
def get_elements_by_type_name(type_name):
    """Function to get Elements by Type Name."""

    # CREATE RULE
    param_id = ElementId(BuiltInParameter.ALL_MODEL_TYPE_NAME)
    f_param = ParameterValueProvider(param_id)
    f_evaluator = FilterStringEquals()

    # Revit API has changes
    if rvt_year < 2023:
        f_rule = FilterStringRule(f_param, FilterStringEquals(), type_name, True)
    else:
        f_rule = FilterStringRule(f_param, FilterStringEquals(), type_name)

    # CREATE FILTER
    filter_type_name = ElementParameterFilter(f_rule)

    # GET ELEMENTS
    return FilteredElementCollector(doc).WherePasses(filter_type_name) \
        .WhereElementIsNotElementType().ToElements()


# Get Elements
elements = get_elements_by_type_name('Type Name')
print(elements)

# ---------------------------------------------------------
def get_elements_by_family_name(family_name):
    """Function to get Elements by Family Name."""

    # CREATE RULE
    param_id = ElementId(BuiltInParameter.ALL_MODEL_FAMILY_NAME)
    f_param = ParameterValueProvider(param_id)
    f_evaluator = FilterStringEquals()

    # Revit API has changes
    if rvt_year < 2023:
        f_rule = FilterStringRule(f_param, FilterStringEquals(), family_name, True)
    else:
        f_rule = FilterStringRule(f_param, FilterStringEquals(), family_name)

    # CREATE FILTER
    filter_type_name = ElementParameterFilter(f_rule)

    # GET ELEMENTS
    return FilteredElementCollector(doc).WherePasses(filter_type_name) \
        .WhereElementIsNotElementType().ToElements()


# Get Elements
elements = get_elements_by_family_name('Filled Region')
print(elements)



# ---------------------------------------------------------
# t = Transaction(doc, 'Change Name')
# t.Start()
#
# t.Commit()

# ---------------------------------------------------------
print('-'*50)
print('Script is finished')
print('Developed by Hung Nguyen.')
