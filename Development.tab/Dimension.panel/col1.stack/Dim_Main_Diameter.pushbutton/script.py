# -*- coding: utf-8 -*-
__title__ = 'Main Diameter Dimension'
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
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

# pyRevit Imports
from pyrevit import forms

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

doc             = __revit__.ActiveUIDocument.Document   # type: Document
uidoc           = __revit__.ActiveUIDocument            # type: UIDocument
app             = __revit__.Application                 # type: UIApplication.Application


# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
all_dimension_types = FilteredElementCollector(doc).OfClass(DimensionType).ToElements()
all_dimension       = FilteredElementCollector(doc).OfClass(Dimension).ToElements()

all_linear_dimension_type = [dim for dim in all_dimension_types if dim.StyleType == DimensionStyleType.Linear]
all_linear_dimension      = [dim for dim in all_dimension if dim.DimensionShape == DimensionShape.Linear]

# 1️⃣ Select the main dimension type

main_linear_dimension = forms.SelectFromList.show(all_linear_dimension_type,
                                                   title="Selection Main Dimension",
                                                   button_name="Select the main dimension",
                                                   multiselect=False,
                                                   name_attr="Name")
if main_linear_dimension:
    print("You select main dimension as: ", main_linear_dimension.Name)

# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# --------------------------------------------------------
with transaction(doc, "1000: Change to main dimension type", debug=True):
    if main_linear_dimension:
        for dimension in all_linear_dimension:
            # type: Dimension
            dimension.DimensionType = main_linear_dimension

forms.alert("You are now able to purge unused dimension"
            "All dimension are change to main dimension")

# ---------------------------------------------------------
