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
from Snippets._parameters import get_parameter_actual_value

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

# ╦╔═╔╗╔╔═╗╦ ╦╦  ╔═╗╔╦╗╔═╗╔═╗
# ╠╩╗║║║║ ║║║║║  ║╣  ║║║ ╦║╣
# ╩ ╩╝╚╝╚═╝╚╩╝╩═╝╚═╝═╩╝╚═╝╚═╝ KNOWLEDGE
# ---------------------------------------------------------
# https://help.autodesk.com/view/RVT/2024/PTB/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Parameters_Shared_Parameters_html

# Shared Parameters are 'parameter definitions' stored in an external file.
# The definitions are identified by a 'unique identifier' generated when the definition is created and can be used in multiple projects.
# The main objects associated with shared parameters are:
# 1. DefinitionFile         = represents a shared parameters file on disk
#                           = Shared Parameters -> Shared parameter file -> Browse/Create
# 2. DefinitionGroup        = group of shared parameters which are organized into meaningful sets
#                           = Shared Parameters -> Parameter group -> New/Rename -> Delete
# 3. ExternalDefinition     = represents a shared parameters definition, belongs to a Definition Group
#                           = Shared Parameters -> Parameters -> New/Properties/Move/Delete
# 4. ExternalDefinitions    = supports the creation of new shared parameters definitions
# 5. Binding                = binds a parameter definition to one or more categories
#                           = Project Parameters -> Edit Param -> Categories
# 6. Binding Map            = contains all the parameter bindings that exist in the Autodesk Revit project
# 7. ParameterElement       = stores information about a particular user-defined parameter in the document
# 8. SharedParameterElement = derived from ParameterElement, stores the definition of a shared parameter.


# ╔╦╗╔═╗╔═╗╦╔╗╔╦╔╦╗╦╔═╗╔╗╔  ╔═╗╦╦  ╔═╗
#  ║║║╣ ╠╣ ║║║║║ ║ ║║ ║║║║  ╠╣ ║║  ║╣
# ═╩╝╚═╝╚  ╩╝╚╝╩ ╩ ╩╚═╝╝╚╝  ╚  ╩╩═╝╚═╝ DEFINITION FILE
# ---------------------------------------------------------
# FORMAT
# The shared parameter definition file is a text file (.txt) with three blocks: META, GROUP, PARAM
# The GROUP and PARAM blocks are relevant to the shared parameter functionality in the revitapi.
# DO NOT EDIT THE DEFINITION FILE DIRECTLY, EDIT USING THE UI OR THE API INSTEAD

# The text file uses tabs to separate fields and can be difficult to read in a text editor

# The GROUP block contains group entries that associate every parameter definition with a group:
# 1. ID     - uniquely identifies the group and associates the parameter definition with a group
# 2. Name   - the group name displayed in the UI

# The PARAM block contains parameter definitions:
# 1. GUID   - Identifies the parameter definition
# 2. NAME   - parameter definition name
# 3. DATATYPE   - Parameter type. This field can be a common type (TEXT, INTEGER), structural type (FORCE, MOMENT)
#                 or common family type (Area Tags)
#                 Common type and structural type parameters are specified in the text file directly
#                 If the value is FAMILYTYPE, an extra number is added, for example FAMILYTYPE -2005020
#                 represents Family Type: Area Tags
# 4. DATACATEGORY   - An optional filed for parameters whose DATATYPE is FAMILYTYPE
# 5. GROUP          - A group ID
# 6. VISIBLE        - 1 = visible, 0 = invisible
# 7. DESCRIPTION
# 8. USERMODIFIABLE - whether user can edit the parameter, 0 = no, 1 = yes


# ╦ ╦╔═╗╦═╗╦╔═  ╦ ╦╦╔╦╗╦ ╦  ╔╦╗╔═╗╔═╗╦╔╗╔╦╔╦╗╦╔═╗╔╗╔  ╔═╗╦╦  ╔═╗
# ║║║║ ║╠╦╝╠╩╗  ║║║║ ║ ╠═╣   ║║║╣ ╠╣ ║║║║║ ║ ║║ ║║║║  ╠╣ ║║  ║╣
# ╚╩╝╚═╝╩╚═╩ ╩  ╚╩╝╩ ╩ ╩ ╩  ═╩╝╚═╝╚  ╩╝╚╝╩ ╩ ╩╚═╝╝╚╝  ╚  ╩╩═╝╚═╝ WORK WITH DEFINITION FILE
# ---------------------------------------------------------

# ACCESSING PARAMETERS IN THE DEFINITION FILE
# 1. Specify the Application.SharedParametersFileName property
# 2. Open the shared parameters file, using Application.OpenSharedParameterFile() method
# 3. Open an existing group or create a new group using the DefinitionFile.Group property
# 4. Open an existing external parameter definition or create a new definition using the DefinitionGroup.Definitions

# DefinitionFile Class
#   - Retrieved using Application.OpenSharedParameterFile() method
#   - Represents one shared parameter files
#   - Contains a number of Group objects
#   - Shared parameters are grouped for easy management and contain shared parameter definitions
#   - New definition can be added as needed

# ExternalDefinition Class
#   - ExternalDefinition object is created by a DefinitionGroup object from a shared parameter file
#   - External parameter definitions must belong to a group which is a collection of shared parameter definitions

# Application.SharedParametersFilename Property
#   - Get and set the shared parameter file path using this property
#   - By default, Revit does not have a shared parameter file.
#   - Initialize this property before using. If not, exception is thrown

# ACCESS AN EXISTING SHARED PARAMETER FILE
# Revit can have many shared parameter file, it's necessary to specifically identify the file and external params you
# want to access. The following procedures illustrate how to access an existing shared parameter file.

# Get Definition file from an external parameter file
# Set the shared parameter file path, then invoke the Application.OpenSharedParameter() method
# - If Application.SharedParameterFilename is set to an invalid path, an exception is thrown only when
#   using OpenSharedParameterFile() is called.

# ╔╗ ╦╔╗╔╔╦╗╦╔╗╔╔═╗
# ╠╩╗║║║║ ║║║║║║║ ╦
# ╚═╝╩╝╚╝═╩╝╩╝╚╝╚═╝ BINDING
# ---------------------------------------------------------
# Binding is what ties shared parameters to elements in certain categories in the model
# There are two types of binding available, Instance binding and Type binding

# To bind a parameters:
# 1. Use an InstanceBinding or a TypeBinding object to create a new Binding object that includes the categories
# 2. Add the binding and definition to the document using the Binding Map object available from the
#    Document.ParameterBindings property

# The following class and method in Autodesk.Revit.DB namespace:
# BindingMap Class
# - Retrieved from the Document.ParameterBindings property
# - Parameter binding connects a parameter definition to elements within one or more categories
# - The map is used to interrogate existing bindings as well as generate new parameter bindings using the Insert method

# BindingMap.Insert() Method
# - The binding object type dictates whether the parameter is bound to all instances or just types
# - A parameter definition cannot be bound to both instances and types
# - If the parameter binding exists , the method return False

















t = Transaction(doc, 'Change Name')
t.Start()

from Snippets._parameters import *


ReadEditExternalParam()

t.Commit()

