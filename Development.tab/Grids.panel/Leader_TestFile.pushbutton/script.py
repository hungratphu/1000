# -*- coding: utf-8 -*-
"""Declare coding style"""

__title__ = 'Change Leader Z'
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
from Autodesk.Revit.UI.Selection import *

# pyRevit Imports

# .NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List

# Custom Imports
from Snippets._datumplane import *


# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc         = __revit__.ActiveUIDocument.Document   # type: Document
uidoc       = __revit__.ActiveUIDocument            # type: UIDocument
app         = __revit__.Application                 # Application class
selection   = uidoc.Selection                     # type: Selection

active_view     = doc.ActiveView
active_level    = active_view.GenLevel
rvt_year        = int(app.VersionNumber)
PATH_SCRIPT     = os.path.dirname(__file__)


# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# ---------------------------------------------------------
# t = Transaction(doc, '1000: Change Leader')
# t.Start()

all_grids = (FilteredElementCollector(doc, active_view.Id).OfCategory(BuiltInCategory.OST_Grids).
             WhereElementIsNotElementType().ToElements())

from pyrevit import forms

view_base = forms.select_views(
    title='Select View Base',
    button_name='Select View',
    multiple=False,
    filterfunc=lambda x: x.ViewType == ViewType.FloorPlan or x.ViewType == ViewType.CeilingPlan)

views_set = forms.select_views(
    title='Select View To Match Grid Leader',
    button_name='Select Views',
    multiple=True,
    filterfunc=lambda x: (x.ViewType == ViewType.FloorPlan or x.ViewType == ViewType.CeilingPlan) and x.Id != view_base.Id
    )


from_view = doc.GetElement(ElementId(312))  # type: View
to_view = active_view

print(active_view)
print(views_set)
print(view_base.Id)

# for grid in all_grids:
#     grid = grid  # type: Grid


# t.Commit()

# ---------------------------------------------------------
print('-' * 50)
print('Script is finished')
print('Developed by Hung Nguyen.')
