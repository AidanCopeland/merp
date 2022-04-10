#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Tkinter frame utility functions.

Functions:
    destroy_frame_objects(parent_frame)
    setup_checkbox_frame(parent_frame, checkbox_text, checkbox_variable)
    setup_entry_frame(parent_frame, entry_text, entry_variable)
    setup_optionmenu_frame(parent_frame, prompt_text, default, variable, *options)
"""
import sys
from tkinter import LEFT, RIGHT, BOTH, RAISED, TOP
from tkinter.ttk import Frame, Label, Entry, Checkbutton, OptionMenu, Button
from future import standard_library
import trace_log as trace

standard_library.install_aliases()

sys.path.append('../')


def destroy_frame_objects(parent_frame):
    """
    Destroy any objects in a previous instance of a frame.
    """
    trace.entry()

    for widget in parent_frame.winfo_children():
        widget.destroy()

    # Add a 1x1 pixel frame to force the parent to collapse if there is nothing else in it
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
    :param default: The default value to report.
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


def init_ui_go_button(parent, text, command):
    trace.entry()

    selection_frame = Frame(parent, relief=RAISED, borderwidth=1)
    selection_frame.pack(fill=BOTH, expand=True)
    selection_button = Button(selection_frame, text=text, command=command)
    selection_button.pack()

    trace.exit()


def init_ui_go_buttons(parent, button_list):
    trace.entry()

    selection_frame = Frame(parent, relief=RAISED, borderwidth=1)
    selection_frame.pack(fill=BOTH, expand=True)

    num_columns = len(button_list)
    for column in range(num_columns):
        selection_frame.columnconfigure(column, weight=1)

    column = 0
    for (text, command) in button_list:
        trace.flow("Process next button")
        selection_button = Button(selection_frame, text=text, command=command)
        selection_button.grid(row=1, column=column, padx=20)
        column += 1
