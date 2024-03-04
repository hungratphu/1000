# -*- coding: utf-8 -*-

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
from Autodesk.Revit.DB import Transaction, TransactionGroup
import contextlib, traceback

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ---------------------------------------------------------
@contextlib.contextmanager
def transaction(doc, title, debug=False):
    """Context Manager that will initiate Transaction .Start() and .Commit() methods.
    In case of an error - it will .RollBack() transaction and display error message if debug = True
    @param doc:     Document where Transaction should be created
    @param title:   Name of Transaction
    @param debug:   True - Display error messages / False - No error messages
    """

    t = Transaction(doc, title)
    t.Start()
    try:
        yield
        t.Commit()
    except:
        t.RollBack()
        if debug:
            print(traceback.format_exc())

# ---------------------------------------------------------

@ contextlib.contextmanager
def try_except(debug=False):
    try:
        yield
    except:
        if debug:
            print(traceback.format_exc())

# ---------------------------------------------------------

@contextlib.contextmanager
def transaction_group(doc, title, debug=False):
    """Context Manager that will initiate TransactionGroup .Start() and .Assimilate() methods.
    In case of an error - it will .RollBack() transaction and display error message if debug = True
    @param doc:     Document where Transaction should be created
    @param title:   Name of Transaction
    @param debug:   True - Display error messages / False - No error messages
    """

    t = TransactionGroup(doc, title)
    t.Start()
    try:
        yield
        t.Assimilate()
    except:
        t.RollBack()
        if debug:
            print(traceback.format_exc())