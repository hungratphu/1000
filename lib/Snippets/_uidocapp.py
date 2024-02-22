# -*- coding: utf-8 -*-

# Variables
uidoc   = __revit__.ActiveUIDocument                # type: UIDocument
doc     = __revit__.ActiveUIDocument.Document       # type: Document
app     = __revit__.Application                     # Application Class

active_view     = doc.ActiveView
active_level    = active_view.GenLevel
rvt_year        = int(app.VersionNumber)

from pyrevit import _HostApplication as hostapp
doc = hostapp.doc
ui = hostapp.uidoc
app = hostapp.app

from pyrevit import revit

