# -*- coding: utf-8 -*-
"""Declare coding style"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
# ---------------------------------------------------------
import os.path

from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI.Selection import *

# .NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
# ---------------------------------------------------------
doc         = __revit__.ActiveUIDocument.Document   #type: Document
uidoc       = __revit__.ActiveUIDocument            #type: UIDocument
app         = __revit__.Application                 # Application class

selection       = uidoc.Selection                   #type: Selection
active_level    = doc.ActiveView
active_level    = active_level.GenLevel
rvt_year        = int(app.VersionNumber)
PATH_SCRIPT     = os.path.dirname(__file__)

# ╔═╗╦ ╦╔╗╔╔═╗╔╦╗╦╔═╗╔╗╔╔═╗
# ╠╣ ║ ║║║║║   ║ ║║ ║║║║╚═╗
# ╚  ╚═╝╝╚╝╚═╝ ╩ ╩╚═╝╝╚╝╚═╝ FUNCTIONS
# ---------------------------------------------------------

#


# ╦  ╔═╗╔═╗╔╦╗╔═╗╦═╗
# ║  ║╣ ╠═╣ ║║║╣ ╠╦╝
# ╩═╝╚═╝╩ ╩═╩╝╚═╝╩╚═ LEADER
# ---------------------------------------------------------

def get_grid_leaders(grid, view, read_leader_shape=False):
    # type: (Grid, View, bool) -> []
    # Leaders are view specific objects, that's why we specify view

    leader_end_0 = grid.GetLeader(DatumEnds.End0, view)
    leader_end_1 = grid.GetLeader(DatumEnds.End1, view)

    if read_leader_shape:
        print("GRID NAME: ", grid.Name)
        print("VIEW NAME: ", view.Name)

        if leader_end_0:
            print("LEADER 0 SHAPE: ", leader_end_0.LeaderShape)
        else:
            print("LEADER 0: NONE")

        if leader_end_1:
            print("LEADER 1 SHAPE: ", leader_end_1.LeaderShape)
        else:
            print("LEADER 1: NONE")

        print("."*20)

    return [leader_end_0, leader_end_1]

# ---------------------------------------------------------

def get_grid_leader_xyz(leader, read_leader_xyz=False):
    if leader:
        leader_anchor = leader.Anchor  # Anchor is point that connects to Grid Head
        leader_elbow = leader.Elbow  # Elbow is point that is between Anchor and End
        leader_end = leader.End  # End is point that connects grid line and leader

        leader_anchor_point = (round(leader_anchor.X), round(leader_anchor.Y), round(leader_anchor.Z))
        leader_elbow_point = (round(leader_elbow.X), round(leader_elbow.Y), round(leader_elbow.Z))
        leader_end_point = (round(leader_end.X), round(leader_end.Y), round(leader_end.Z))

        if read_leader_xyz:
            print("Leader XYZ: ")
            print("Leader Anchor Point: {}".format(leader_anchor_point))
            print("Leader Elbow Point: {}".format(leader_elbow_point))
            print("Leader End Point: {}".format(leader_end_point))
            print("-"*50)

        return leader_anchor, leader_elbow, leader_end

# ---------------------------------------------------------

def add_grid_leaders(grid, view):
    """The leader can add where bubbles is shown and leader is none"""
    # type: (Grid, View)
    leader_end_0 = grid.GetLeader(DatumEnds.End0, view)
    leader_end_1 = grid.GetLeader(DatumEnds.End1, view)
    is_grid_bubble_visible_0 = grid.IsBubbleVisibleInView(DatumEnds.End0, view)
    is_grid_bubble_visible_1 = grid.IsBubbleVisibleInView(DatumEnds.End1, view)

    new_leader_0 = None
    if is_grid_bubble_visible_0 and leader_end_0 is None:
        new_leader_0 = grid.AddLeader(DatumEnds.End0, view)

    new_leader_1 = None
    if is_grid_bubble_visible_1 and leader_end_1 is None:
        new_leader_1 = grid.AddLeader(DatumEnds.End1, view)

    return new_leader_0, new_leader_1

# ---------------------------------------------------------

def straighten_grid_leaders(grid, view):
    """Straighten grid leaders"""
    # type: (Grid, View)
    leader_0 = grid.GetLeader(DatumEnds.End0, view)
    leader_1 = grid.GetLeader(DatumEnds.End1, view)

    if leader_0:
        leader_0.Elbow = XYZ(leader_0.Anchor.X,
                             leader_0.Anchor.Y,
                             leader_0.Anchor.Z)

        is_valid_0 = grid.IsLeaderValid(DatumEnds.End0, view, leader_0)
        is_bubble_visibility_0 = grid.IsBubbleVisibleInView(DatumEnds.End0, view)

        if is_valid_0 and is_bubble_visibility_0:
            grid.SetLeader(DatumEnds.End0, view, leader_0)

    if leader_1:
        leader_1.Elbow = XYZ(leader_1.Anchor.X,
                             leader_1.Anchor.Y,
                             leader_1.Anchor.Z)

        is_valid_1 = grid.IsLeaderValid(DatumEnds.End1, view, leader_1)
        is_bubble_visibility_1 = grid.IsBubbleVisibleInView(DatumEnds.End1, view)

        if is_valid_1 and is_bubble_visibility_1:
            grid.SetLeader(DatumEnds.End1, view, leader_1)

    return leader_0, leader_1

# ---------------------------------------------------------

def straight_grid_leader_0(grid, view, leader_0):
    # Next task: Combine this with straight_grid_leader() function
    if leader_0:
        leader_0.Elbow = XYZ(leader_0.Anchor.X,
                             leader_0.Anchor.Y,
                             leader_0.Anchor.Z)

        is_valid_0 = grid.IsLeaderValid(DatumEnds.End0, view, leader_0)
        is_bubble_visibility_0 = grid.IsBubbleVisibleInView(DatumEnds.End0, view)

        if is_valid_0 and is_bubble_visibility_0:
            grid.SetLeader(DatumEnds.End0, view, leader_0)
        else:
            print("Leader 0: Fail to set leader straight @ grid {}".format(grid.Name))

# ---------------------------------------------------------

def straight_grid_leader_1(grid, view, leader_1):
    # Next task: Combine this with straight_grid_leader() function
    if leader_1:
        leader_1.Elbow = XYZ(leader_1.Anchor.X,
                             leader_1.Anchor.Y,
                             leader_1.Anchor.Z)

        is_valid_1 = grid.IsLeaderValid(DatumEnds.End1, view, leader_1)
        is_bubble_visibility_1 = grid.IsBubbleVisibleInView(DatumEnds.End1, view)

        if is_valid_1 and is_bubble_visibility_1:
            grid.SetLeader(DatumEnds.End1, view, leader_1)
        else:
            print("Leader 1: Fail to set leader straight @ grid {}".format(grid.Name))

# ---------------------------------------------------------

def match_leaders_xyz(from_leader, new_leader):
    """Match new leader End XYZ and Elbow XYZ with selected leader"""
    # type: (Leader, Leader)
    if from_leader and new_leader:

        from_end   = from_leader.End
        from_elbow = from_leader.Elbow

        new_leader.End = XYZ(from_end.X, from_end.Y, new_leader.End.Z)
        new_leader.Elbow = XYZ(from_elbow.X, from_elbow.Y, new_leader.Elbow.Z)

        return new_leader


# ---------------------------------------------------------

def set_leaders(grid, view, leader_0, leader_1):
    """The leader can be applied only to ends where bubble is shown"""
    if leader_0:
        is_valid_0 = grid.IsLeaderValid(DatumEnds.End0, view, leader_0)
        is_grid_bubble_visible_0 = grid.IsBubbleVisibleInView(DatumEnds.End0, view)

        if is_valid_0 and is_grid_bubble_visible_0:
            grid.SetLeader(DatumEnds.End0, view, leader_0)
        else:
            print("Leader 0: Fail to set leader @ grid {}".format(grid.Name))

    if leader_1:
        is_valid_1 = grid.IsLeaderValid(DatumEnds.End1, view, leader_1)
        is_grid_bubble_visible_1 = grid.IsBubbleVisibleInView(DatumEnds.End1, view)

        if is_valid_1 and is_grid_bubble_visible_1:
            grid.SetLeader(DatumEnds.End1, view, leader_1)
        else:
            print("Leader 1: Fail to set leader @ grid {}".format(grid.Name))

# ---------------------------------------------------------




# ---------------------------------------------------------

def has_datum_bubble(grid, view):
    """Grid and Elevations always has bubbles. Ref doesn't have bubbles"""
    # type: (Grid, View)
    has_bubble_0 = grid.HasBubbleInView(DatumEnds.End0, view)
    has_bubble_1 = grid.HasBubbleInView(DatumEnds.End1, view)

    return has_bubble_0, has_bubble_1

# ---------------------------------------------------------

def is_grid_bubble_visible(grid, view):
    """Use this to evaluate if bubble visible"""
    # type: (Grid, View)
    is_bubble_visibility_0 = grid.IsBubbleVisibleInView(DatumEnds.End0, view)
    is_bubble_visibility_1 = grid.IsBubbleVisibleInView(DatumEnds.End1, view)

    return is_bubble_visibility_0, is_bubble_visibility_1

# ---------------------------------------------------------

















