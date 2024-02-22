# coding=utf-8

# How to use .NET List?
# This list is different to python list because it's Typed List.
# It means that we need to specify Type of elements inside of that list,
# and no other types can be added.
# You will see it's required inside many methods in Revit API.
# You will also see ICollection<T> as argument too, and we can use List<T> instead.
# Here is an example:

# Imports
import clr
from System import List # List[ElementId]()

#1️⃣ Create Empty List and Add Items
empty_list = List[ElementId]()
empty_list.Add(element_A.Id)
empty_list.Add(element_B.Id)

#2️⃣ Convert python list in .NET List
python_list_ids = [element_A.Id, element_B.Id]
List_el_ids     = List[ElementId](python_list_ids)
