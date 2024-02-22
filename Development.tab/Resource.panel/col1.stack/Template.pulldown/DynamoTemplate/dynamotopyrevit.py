from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

import clr
clr.AddReference('System')
from System.Collections.Generic import List # List[ElementId]()

# Variables
uidoc = __revit__.ActiveUIDocument
doc   = __revit__.ActiveUIDocument.Document

# Alternative Method with pyrevit module
# from pyrevit import revit
# doc = revit.doc
# uidoc = revit.uidoc
# app = revit.app

# Regular Style
t = Transaction(doc, "Change")

t.Start()
# change in here
t.Commit()

# Context Manager Style
with Transaction(doc, 'Change') as t:
    t.Start()
    # Changes Here
    t.Commit()