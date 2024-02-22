# -*- coding: utf-8 -*-
"""Declare coding style"""

__title__ = 'Open Folder Central'
__doc__ = """
Date    = 2023.Dec.25
---------------------------------------------------------
Description:
---------------------------------------------------------
Author: Hung Nguyen """

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
import os, datetime, pathlib, re
from Autodesk.Revit.DB import *
from Snippets._path import get_subfolder_path

# pyRevit Imports
from pyrevit import forms

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc                         = __revit__.ActiveUIDocument.Document           #type: Document

# 👉SEE IF DOCUMENT IS WORK-SHARED
if doc.IsWorkshared:
    central_file            = doc.GetWorksharingCentralModelPath()
    file_location           = ModelPathUtils.ConvertModelPathToUserVisiblePath(central_file)
else:
    file_location           = doc.PathName

# 👉GET FOLDERS PATH
project_parent_path = pathlib.Path(file_location).parents[3]
admin_folder                = get_subfolder_path    (project_parent_path, 0)
client_files_folder         = get_subfolder_path    (project_parent_path, 1)
deliverable_folder          = get_subfolder_path    (project_parent_path, 2)
working_folder              = get_subfolder_path    (project_parent_path, 3)
pictures_folder             = get_subfolder_path    (project_parent_path, 4)
construction_admin_folder   = get_subfolder_path    (project_parent_path, 5)

working_dwg_folder    = get_subfolder_path    (working_folder,      3)
current_drawings      = get_subfolder_path    (working_dwg_folder,  0)
incoming              = get_subfolder_path    (working_dwg_folder,  2)
misc_folder           = get_subfolder_path    (working_dwg_folder,  4)
product_info_cutsheet = get_subfolder_path    (working_dwg_folder,  5)

project_revit_links     = get_subfolder_path    (current_drawings,  1)
project_revit_families  = get_subfolder_path    (current_drawings,  2)

# 👉CREATE A DICTIONARY FROM FOLDERS PATH ABOVE:
folder_options = {
    admin_folder.name               : admin_folder,
    client_files_folder.name        : client_files_folder,
    deliverable_folder.name         : deliverable_folder,
    working_folder.name             : working_dwg_folder,
    construction_admin_folder.name  : construction_admin_folder,
    current_drawings.name           : current_drawings,
    incoming.name                   : incoming,
    misc_folder.name                : misc_folder,
    product_info_cutsheet.name      : product_info_cutsheet,
    project_revit_links.name        : project_revit_links,
    project_revit_families.name     : project_revit_families}

# 👉PRINT TEST
# print(file_location)
# print(project_parent_path)
# print(deliverable_folder)
# print(working_folder)
# print(working_dwg_folder)
# print(misc_folder)
# print(deliverable_folder.name)
# print(working_dwg_folder.name)
# print(misc_folder.name)
# print(project_parent_path.name)

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝ FUNCTIONS
# ---------------------------------------------------------
def ask_for_folder_path_user_choice(dict_of_folder):
    option_keys = list(dict_of_folder.keys())                   # CREATE A LIST FROM DICT. KEY
    selected_option = forms.CommandSwitchWindow.show(           # USE PYREVIT SEARCH GUID
            option_keys,
            message='Select parent folder:')

    selected_folder = folder_options.get(selected_option)       # GET DICT. VALUE FROM SELECTED DICT. KEY

    if selected_folder:                                         # OPEN THE FOLDER IN EXPLORER
        return os.startfile(str(selected_folder))
    else:
        return forms.check_selection(exitscript=True)           # ALERT USER IF NOTHING SELECTED


# ╔╦╗  ╔═╗  ╦  ╔╗╔
# ║║║  ╠═╣  ║  ║║║
# ╩ ╩  ╩ ╩  ╩  ╝╚╝  MAIN
# ---------------------------------------------------------
ask_for_folder_path_user_choice(folder_options)