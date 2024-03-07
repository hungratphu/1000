# -*- coding: utf-8 -*-
__title__ = 'Main Linear Dimension'
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
from Autodesk.Revit.UI.Selection import *

# pyRevit Imports
from pyrevit import forms

# .NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List

# Custom Imports
from Snippets._transaction import *
import time

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
start_time = time.time()

all_dimension_types = FilteredElementCollector(doc).OfClass(DimensionType).ToElements()
all_dimension       = FilteredElementCollector(doc).OfClass(Dimension).ToElements()
all_constraints     = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Constraints).WhereElementIsNotElementType().ToElements()

all_linear_dimension_type = [dim for dim in all_dimension_types if dim.StyleType == DimensionStyleType.Linear]
all_linear_dimension      = [dim for dim in all_dimension if dim.DimensionShape == DimensionShape.Linear]

# 1️⃣ Select the main dimension type

main_linear_dimension = forms.SelectFromList.show(all_linear_dimension_type,
                                                   title="Selection Main Dimension",
                                                   button_name="Select the main dimension",
                                                   multiselect=False,
                                                   name_attr="Name")


other_than_main_linear_dimension_and_constraint = [dim for dim in all_linear_dimension
                                                   if dim.DimensionType != main_linear_dimension
                                                   and dim.Category.BuiltInCategory != BuiltInCategory.OST_Constraints]

print("Find: {} constraints".format(len(all_constraints)))
print("Find: {} dimension to action".format(len(other_than_main_linear_dimension_and_constraint)))


# ╔╦╗╦═╗╔═╗╔╗╔╔═╗╔═╗╔═╗╔╦╗╦╔═╗╔╗╔
#  ║ ╠╦╝╠═╣║║║╚═╗╠═╣║   ║ ║║ ║║║║
#  ╩ ╩╚═╩ ╩╝╚╝╚═╝╩ ╩╚═╝ ╩ ╩╚═╝╝╚╝ TRANSACTION
# --------------------------------------------------------
# for dimension in other_than_main_linear_dimension:  # type: Dimension
#     if dimension.IsValidObject:
#         if not dimension.AreReferencesAvailable and dimension.GroupId != ElementId(-1):
#             print("002: Id, GroupId, Name:", dimension.Id, dimension.GroupId)
#             if dimension.View:
#                 print(dimension.View.Name)
#
# print("|"*50)

with transaction_group(doc, "1000: Change to main dimension type", debug=True):


    if main_linear_dimension:

        selected_id_list = []

        for dimension in other_than_main_linear_dimension_and_constraint:   # type: Dimension
            if dimension.IsValidObject:
                if dimension.GroupId == ElementId(-1):
                    with transaction(doc, "Change model dimension"):

                        if dimension.AreReferencesAvailable:
                            try:
                                dimension.DimensionType = main_linear_dimension
                                # family.Set(ElementId(main_linear_dimension.Id))
                            except:
                                print("Detect_Model: ID: {}, at: {}, cat: {}, name:{}".format(dimension.Id,
                                                                                              dimension.View,
                                                                                              dimension.Category.Name,
                                                                                              dimension.Name))
                        elif not dimension.AreReferencesAvailable:
                            try:
                                dimension.DimensionType = main_linear_dimension
                                # family.Set(ElementId(main_linear_dimension.Id))
                            except:
                                print("Detect_ViewSpecific: ID: {}, at: {}, cat: {}, name:{}".format(dimension.Id,
                                                                                                     dimension.View,
                                                                                                     dimension.Category.Name,
                                                                                                     dimension.Name))

                else:
                    if dimension.Id not in selected_id_list:
                        selected_id_list.append(dimension.Id)

            with transaction(doc, "change", debug=True):
                for con in all_constraints:
                    selected_id_list.append(con)

                new_selection = List[ElementId](selected_id_list)
                selection = uidoc.Selection.SetElementIds(new_selection)

        # forms.alert("NEXT STEP:"
        #             "Purge unused dimension")

# ---------------------------------------------------------

end_time = time.time()
count_time =  end_time - start_time
# print("EXECUTION TIME: "
#       "{} seconds".format(count_time))