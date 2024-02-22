
# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
import os, datetime, re, pathlib
from pyrevit import forms


# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝ FUNCTIONS
# ---------------------------------------------------------
def get_subfolder_path(folder_path, folder_index):
    sub_folders     = list(folder_path.glob('*/'))
    return            sub_folders[folder_index]


def ask_for_folder_path(option_1, option_2):
    selected_option = forms.CommandSwitchWindow.show(
            [option_1, option_2],
            message='Select parent folder:')
    return selected_option


def ask_for_folder_description():
    description_input = forms.ask_for_string(default="folder description",
                                             prompt='Enter folder description',
                                             title='Create New Folder')
    if re.search(r'[\\/:*?"<>|]', description_input):
        forms.alert('A file name cannot contain any of the following characters: \\/:*?\"<>|', exitscript=True)
    else:
        return description_input


def create_folder(base_path, folder_name):
    new_folder_path = base_path / folder_name
    new_folder_path.mkdir()
    os.startfile(str(new_folder_path))
