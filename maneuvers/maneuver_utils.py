#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The base maneuver utility functions.

Functions:
    setup_maneuver_difficulty_frame(table, parent_frame)
    setup_maneuver_table_frames_for_equipment(table, parent_frame)
    setup_equipment_frame(table, parent_frame)
    table_bonus_from_equipment(table)
"""
from __future__ import absolute_import
from tkinter import LEFT, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Label, OptionMenu

import trace_log as trace
import frame_utils

MANEUVER_DIFFICULTY_LABEL_TEXT = "Maneuver difficulty: "

ROUTINE = "Routine"
EASY = "Easy"
LIGHT = "Light"
MEDIUM = "Medium"
HARD = "Hard"
VERY_HARD = "Very Hard"
EXTREMELY_HARD = "Extremely Hard"
SHEER_FOLLY = "Sheer Folly"
ABSURD = "Absurd"

maneuver_difficulty_options = (
    ROUTINE, EASY, LIGHT, MEDIUM, HARD, VERY_HARD, EXTREMELY_HARD, SHEER_FOLLY, ABSURD)

EQUIPMENT_TEXT = "Set bonus of -10 to -50 if without proper equipment"


def setup_maneuver_difficulty_frame(table, parent_frame):
    """
    Creates a frame to allow selection of the maneuver difficulty using an OptionMenu widget.
    :param table: The maneuver table.
    :param parent_frame: The owning frame.
    """
    trace.entry()

    frame_utils.destroy_frame_objects(parent_frame)

    maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
    maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

    maneuver_difficulty_prompt = Label(maneuver_difficulty_frame,
                                       text=MANEUVER_DIFFICULTY_LABEL_TEXT)
    maneuver_difficulty_prompt.pack(side=LEFT)

    table.maneuver_difficulty_options = maneuver_difficulty_options

    table.maneuver_difficulty_selector = \
        OptionMenu(
            maneuver_difficulty_frame,
            table.maneuver_difficulty,
            MEDIUM,
            *table.maneuver_difficulty_options)
    table.maneuver_difficulty_selector.pack(side=RIGHT)

    trace.exit()


def setup_maneuver_table_frames_for_equipment(table, parent_frame):
    """
    Set up the frames specific to the maneuver table, with a single Entry indicating
    whether proper equipment is missing.
    :param table: The maneuver table.
    :param parent_frame: The owning frame.
    """
    trace.entry()

    frame_utils.destroy_frame_objects(parent_frame)
    table.equipment_bonus.set(0)
    setup_equipment_frame(table, parent_frame)

    trace.exit()


def setup_equipment_frame(table, parent_frame):
    """
    Create a frame with an Entry indicating whether proper equipment is missing.
    :param table: The maneuver table.
    :param parent_frame: The owning frame.
    """
    trace.entry()
    frame_utils.setup_entry_frame(parent_frame, EQUIPMENT_TEXT, table.equipment_bonus)
    trace.exit()


def table_bonus_from_equipment(table):
    """
    Determine any additional bonuses to apply to a maneuver based on an equipment penalty
    to this maneuver type
    :param table: The maneuver table.
    :return: The additional maneuver bonus
    """
    trace.entry()

    bonus = 0
    trace.detail("Equipment bonus: %d" % table.equipment_bonus.get())
    bonus += table.equipment_bonus.get()

    trace.exit()
    return bonus
