# -*- coding: utf-8 -*-

# Imports
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

# Variables
uidoc       = __revit__.ActiveUIDocument            #type: UIDocument
doc         = __revit__.ActiveUIDocument.Document   #type: Document
selection   = uidoc.Selection                       #type: Selection

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝    FUNCTION
# ===========================================================================
def get_selected_elements():
    """Function to get selected elements in Revit UI."""
    return [doc.GetElement(e_id) for e_id in uidoc.Selection.GetElementIds()]


# ╔═╗╦  ╔═╗╔═╗╔═╗
# ║  ║  ╠═╣╚═╗╚═╗
# ╚═╝╩═╝╩ ╩╚═╝╚═╝   CLASS
# ===========================================================================
class ISelectionFilter_Classes(ISelectionFilter):
    def __init__(self, allowed_classes):
        self.allowed_classes = allowed_classes

    def AllowElement(self, elem):
        if type(elem) in self.allowed_classes:
            return True


class ISelectionFilter_Categories(ISelectionFilter):
    def __init__(self, allowed_categories):
        self.allowed_categories = allowed_categories

    def AllowElement(self, elem):
        if elem.Category.BuiltInCategory in self.allowed_categories:
            return True