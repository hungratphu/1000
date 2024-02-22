API_Development_Requirements = """
When developing with Autodesk Revit API, ensure to references two DLLs: RevitAPI.dll and RevitAPIUI.dll in Autodesk Revit Program directory"""

API_Application_and_Document = """
The top level objects in Revit Platform API are //Application// and //Document//. These are represented by the classes:
- Application, 
- UIApplication, 
- Document, 
- UIDocument.

()These application object refers to an individual Revit session, providing access to documents, options and other application-wide data and settings:
- Autodesk.Revit.UI.UIApplication - provides access to UI-level interfaces for the application, 
including the ability to add RibbonPanels to the user interface, and 
the ability to obtain the active document in the user interface

- Autodesk.Revit.ApplicationServices.Application - provides access to all other application level properties.

()The document object is a single Revit project file representing a building model. Revit can have multiple projects open and multiple views for one project.
- Autodesk.Revit.UI.UIDocument - provides access to UI-level interfaces for the document, such as
the contents of the selection, and
the ability to prompt the user to make selections and pick points.

- Autodesk.Revit.DB.Document - provides access to all other document and level properties
"""

API_Application_Functions = """
https://help.autodesk.com/view/RVT/2024/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Introduction_Application_and_Document_Application_Functions_html
"""

API_Doccument_Functions = """
Document stores the Revit Elements, manages the data, and updates multiple data views. 
The Document class mainly provides the following functions.

//Document//
The document class represents an open Autodesk Revit project.

### Settings Property
The Settings property returns an object that provides access to general components within Revit projects

### Place and Locations
Each project has only one site location that identifies the physical project location on Earth. 
There can be several project locations for one project.
Each location is an offset, or rotation, of the site location

### View Management
A project document can have multiple views. The ActiveView property returns a View object representing the active view.
You can filter the elements in the project to retrieve other views.

### File Management
Each Document object represents a revit project file. Document provides these functions:
. Retrieve file information such as file path name and project title
. Provides Close() and Save() methods to close and save the document.

### Element Management
Revit maintains all Element objects in a project. To create new lement, use the Create property which returns an Object
Factory used to create new project element instances in the Revit Platform API, such as FamilyINstance or Group.

The Document class can also be used to delete elements. use the Delete() method to delete an element in the project.
Deleted elements and any dependent elements are not displayed and are removed from the Document.

### Events
Events are raised on certain actions, such as when you save a project using Save or Save As. To capture the events and
respond in the application, you must register the event handlers

### Document Status
Several properties provide information on the status of the document:
. IsModificable - whether the document may currently be modifed
. IsModified
. IsReadOnly
. IsReadOnlyFile
. IsFamilyDocument
. IsWorkshared

### Others
Document also provides these functions"
. ParameterBindings Property - Mapping between parameter definitions and categories.
. ReactionsAreUpToDate Property - Reports wheter the reactionary loads changed.
. Default Types - Access to the default types for family and non-family elements.

//UIDocument//
The UIDocument class represents an Autodesk Revit project opened in the REvit user interface.

### Element Retrieval in UIDocument
Retrieve selected elements using the Selection property in UIDocument. This property returns an object representing the
active selection containing the selected project elements. It also provides sUI interaction methods to pick objects in the Revit model.

### Element Display
The ShowElements() method uses zoom to fit to focus in one or more elements.

### View Management in UIDocument
The UIDocument class can be used to refresh the active view in the active document by calling the RefreshActiveView() method.
The ActiveView property can be used to retrieve or set the active view for the document. Changing the active view has some
restriction. It can only be used in an active document, which must not be in read-only state and must not be inside a transaction.
Additionally, the active view may not be changed during the ViewActivating or ViewAcitiviated event, or during any pre-action event,
such as DocumentSaving, DocumentClosing, or other similar events

The UIDocument.ActiveGraphicalView property retrieves the active graphical view for the document. Unlike UIDocument.ActiveView,
this property will new return auxiliary views like the Project Browser or System Browser if the user has happened to make a selection in one of those views.

The UIDocument can also be used to get a list of all open view windows in the Revit user interface. The GetOpenUIViews method returns
a list of UIViews which contain data about the view windows in the Revit user interface.





"""







