# -*- coding: utf-8 -*-

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
from Autodesk.Revit.DB import Document
from Autodesk.Revit.UI import UIDocument

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc         = __revit__.ActiveUIDocument.Document   #type: Document
uidoc       = __revit__.ActiveUIDocument            #type: UIDocument
app         = __revit__.Application                 # Application class
rvt_year    = int(app.VersionNumber)


# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ---------------------------------------------------------

def convert_units(length, unit = "mm", convert_from_internal_unit=True):
    #type: (float, str, bool) -> float
    """ Function to convert internal units to mm or vice versa
    :param length:                      Value to convert
    :param string:                      Choose from mm / mm2 ; m / m2
    :param convert_from_internal_unit:  True to get Millimeters, False to get internal units
    :return:                            Length in Millimeters or internal units """

    from Autodesk.Revit.DB import UnitTypeId, UnitUtils
    if   unit == "mm" : units = UnitTypeId.Millimeters
    elif unit == "mm2": units = UnitTypeId.SquareMillimeters
    elif unit == "m"  : units = UnitTypeId.Meters
    elif unit == "m2" : units = UnitTypeId.SquareMeters

    if convert_from_internal_unit:
        return UnitUtils.ConvertFromInternalUnits(length, units)
    else:
        return UnitUtils.ConvertToInternalUnits(length, units)

def convert_mm_to_internal(length):
    from Autodesk.Revit.DB import UnitTypeId, UnitUtils
    return UnitUtils.ConvertFromInternalUnits(length, UnitTypeId.Millimeters)
