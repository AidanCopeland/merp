# -*- coding: utf-8 -*-
"""
Stalk/Hide static maneuver utility functions.

Functions:
    setup_contested_frame(table)
    setup_searcher_bonus_frame(table)
"""
import sys

import frame_utils
import trace_log as trace

sys.path.append('../')

CONTESTED_TEXT = "Roll against searcher's Perception bonus?"

SEARCHER_BONUS_TEXT = "Searcher's Perception bonus"


def setup_contested_frame(table, parent_frame):
    """
    Create a frame with a Checkbox indicating whether the searcher's Perception
    bonus should be used against the Hide skill.
    :param table: The calling Stalk/Hide maneuver table.
    :param parent_frame: The owning frame.
    """
    trace.entry()
    frame_utils.setup_checkbox_frame(
        parent_frame, CONTESTED_TEXT, table.contested
    )
    table.contested.trace("w", table.skill_frames_update_callback)

    trace.exit()


def setup_searcher_bonus_frame(table, parent_frame):
    """
    Create a frame with an Entry for a searcher's Perception bonus.
    :param table: The calling Stalk/Hide maneuver table.
    :param parent_frame: The owning frame.
    """
    trace.entry()
    frame_utils.setup_entry_frame(
        parent_frame, SEARCHER_BONUS_TEXT, table.searcher_bonus
    )
    trace.exit()
