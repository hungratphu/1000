# -*- coding: utf-8 -*-
"""Declare coding style"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.ApplicationServices import Application

import os.path


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

def get_parameter_actual_value(param):
    """Get a value from a Parameter based on its StorageType"""
    value = None
    if param.StorageType == StorageType.Double:
        value = param.AsDouble()
    elif param.StorageType == StorageType.ElementId:
        value = param.AsElementId()
    elif param.StorageType == StorageType.Integer:
        value = param.AsInteger()
    elif param.StorageType == StorageType.String:
        value = param.AsString()
    return value

# ╔╦╗╔═╗╔═╗╦╔╗╔╦╔╦╗╦╔═╗╔╗╔  ╔═╗╦╦  ╔═╗
#  ║║║╣ ╠╣ ║║║║║ ║ ║║ ║║║║  ╠╣ ║║  ║╣
# ═╩╝╚═╝╚  ╩╝╚╝╩ ╩ ╩╚═╝╝╚╝  ╚  ╩╩═╝╚═╝ DEFINITION FILE
# ---------------------------------------------------------

def assign_and_access_shared_parameter_file(path):
    # type: (str) -> DefinitionFile
    """Assign a new shared parameter file to Revit and access the file """

    # Check if path is not existing, create a new shared file based on path
    if not os.path.exists(path):
        with open(path, 'w') as file:
            pass

    app.SharedParametersFilename = path
    return app.OpenSharedParameterFile()

# ---------------------------------------------------------

def access_shared_parameter_file():
    """Access the shared parameter file"""
    app.OpenSharedParameterFile()

# ---------------------------------------------------------

def read_shared_parameter_file():
    """Read property of shared parameter file"""

    definition_file = app.OpenSharedParameterFile()

    shared_filed_info = []

    # get the file name
    shared_filed_info.append("File Name: {}".format(definition_file.Filename))

    for parameter_group in definition_file.Groups: # type: DefinitionGroup
        # get the group name:
        shared_filed_info.append("Group Name: {}".format(parameter_group.Name))

        # iterate the definitions
        for definition in parameter_group.Definitions:  # type: Definition
            shared_filed_info.append("Definition Name: {}".format(definition.Name))

    # Convert list to a string
    shared_filed_info_str = '\n'.join(shared_filed_info)

    # Print the string
    print(shared_filed_info_str)

# ---------------------------------------------------------

def open_shared_parameter_file_txt():
    definition_file = app.OpenSharedParameterFile()

    os.startfile(definition_file.Filename)


# ╔═╗╔═╗╦═╗╔═╗╔╦╗╔═╗╔╦╗╔═╗╦═╗╔═╗
# ╠═╝╠═╣╠╦╝╠═╣║║║║╣  ║ ║╣ ╠╦╝╚═╗
# ╩  ╩ ╩╩╚═╩ ╩╩ ╩╚═╝ ╩ ╚═╝╩╚═╚═╝ PARAMETERS aka DEFINITIONS (EXTERNAL)
# ---------------------------------------------------------

def change_parameter_owner_group(old_group, which_parameter, new_group):
    # type: (str, str, str) -> None
    """Change the location of one parameter from the current group to another group"""
    definition_file = app.OpenSharedParameterFile()

    # get ExternalDefinition from shared parameter file
    definition_groups = definition_file.Groups
    selected_group = definition_groups.get_Item(old_group)

    if selected_group is not None:
        selected_parameter = selected_group.Definitions.get_Item(which_parameter)

        if selected_parameter is not None:
            new_group = definition_groups.get_Item(new_group)

            if new_group is not None:
                # change the OwnerGroup of the ExternalDefinition
                selected_parameter.OwnerGroup = new_group
