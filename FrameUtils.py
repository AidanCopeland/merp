#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')#

import trace_log as trace

from Tkinter import LEFT, RIGHT, BOTH, RAISED, StringVar
from ttk import Frame, Label, Entry, Checkbutton, OptionMenu


def destroy_frame_objects(parent_frame):
    """
    Destroy any objects in a previous instance of a frame.
    """
    trace.entry()

    for widget in parent_frame.winfo_children():
        widget.destroy()

    """Add a 1x1 pixel frame to force the parent to collapse if there is nothing else in it"""
    tmp = Frame(parent_frame, width=1, height=1, borderwidth=0)
    tmp.pack()

    trace.exit()

def setup_checkbox_frame(parent_frame, checkbox_text, checkbox_variable):
    """
    Sets up a frame containing a Checkbox
    :param parent_frame: The parent frame.
    :param checkbox_text: The text to apply to the checkbox.
    :param checkbox_variable: The variable that tracks the checkbox.
    """
    trace.entry()

    checkbox_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
    checkbox_frame.pack(fill=BOTH, expand=True)

    checkbox_prompt = Label(checkbox_frame, text=checkbox_text)
    checkbox_prompt.pack(side=LEFT)

    checkbox_input = Checkbutton(
        checkbox_frame,
        variable=checkbox_variable
    )
    checkbox_input.pack(side=RIGHT)

    trace.exit()


def setup_entry_frame(parent_frame, entry_text, entry_variable):
    """
    Sets up a frame containing an Entry.
    :param parent_frame: The parent frame.
    :param entry_text: The text to apply to the entry.
    :param entry_variable: The variable that tracks the entry.
    """
    trace.entry()

    entry_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
    entry_frame.pack(fill=BOTH, expand=True)

    entry_prompt = Label(entry_frame, text=entry_text)
    entry_prompt.pack(side=LEFT)

    entry_input = Entry(
        entry_frame,
        textvariable=entry_variable
    )
    entry_input.pack(side=RIGHT)

    trace.exit()


def setup_optionmenu_frame(parent_frame, prompt_text, default, variable, *options):
    """
    Sets up a frame containing an OptionMenu.
    :param parent_frame: The parent frame.
    :param prompt_text: The prompt text to associate with the OptionMenu.
    :param options: The options to apply to the OptionMenu
    :param variable: The variable that tracks the OptionMenu
    """
    trace.entry()

    option_menu_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
    option_menu_frame.pack(fill=BOTH, expand=True)

    option_menu_prompt = Label(option_menu_frame, text=prompt_text)
    option_menu_prompt.pack(side=LEFT)

    option_menu_selector = \
        OptionMenu(
            option_menu_frame,
            variable,
            default,
            *options)
    option_menu_selector.pack(side=RIGHT)

    trace.exit()
    pass