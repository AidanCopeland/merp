#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module provides the console from which all Merp functions can be accessed.

Classes: console
"""
import sys
from tkinter import Tk, LEFT, RIGHT, BOTH, RAISED, StringVar, OptionMenu, Toplevel
from tkinter.ttk import Frame, Style, Label

from future import standard_library

import frame_utils
from console.character_database.character_database import CharacterDatabase
from console.dice_roller.dice_roller import DiceRoller
from console.name_database.name_selector import NameSelector
from console.character.character_manager import CharacterManager
from console.encounters.encounter_generator import EncounterGenerator
from maneuvers.maneuver_table import ManeuverTable
import trace_log as trace
from tk_helper import clear_option_menu, refresh_option_menu

standard_library.install_aliases()

sys.path.append('../')  #
sys.path.append('character')  #
sys.path.append('character_database')  #
sys.path.append('dice_roller')  #
sys.path.append('encounters/')  #
sys.path.append('encounters/modules')  #
sys.path.append('../maneuvers')  #
sys.path.append('name_database')  #

MANEUVERS = "Maneuvers"
CHARACTER_MANAGER = "Character manager"
DICE_ROLLER = "Dice roller"
ENCOUNTER_GENERATOR = "Encounter generator"
NAME_SELECTOR = "Name selector"


class Console(Frame):
    """The top level console used to access all other functionality.

    Methods:
        __init__(self)
        init_ui(self)
        set_current_option(self, option)
        option_change_callback(self)
        launch_option(self)
        character_manager_closed(self)
        maneuver_window_closed(self)
        dice_roller_closed(self)
        encouter_generator_closed(self)
        characters_updated(self)
        """
    def __init__(self):
        trace.entry()
        trace.detail("Path is %r" % sys.path)
        Frame.__init__(self)

        self.style = None
        self.options = None
        self.selector_widget = None
        self.selector_frame = None
        self.option_selector = None
        self.character_manager_window = None
        self.maneuver_window = None
        self.dice_roller_window = None
        self.encounter_generator = None
        self.name_selector_window = None

        self.character_manager = None
        self.maneuver_table = None
        self.dice_roller = None
        self.name_selector = None

        self.character_database = CharacterDatabase()
        self.current_option = ""
        self.init_ui()

        trace.exit()

    def init_ui(self):
        """
        Initializes the components of the Console window.
        """
        trace.entry()

        self._initialize_variables()
        self._initialize_ui_variables()

        self._init_ui_title()
        self._init_ui_selector()
        frame_utils.init_ui_go_button(self, 'Go!', self.launch_option)

        self._add_entries_to_option_selector()

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def _initialize_variables(self):
        trace.entry()
        self.master.title("Console")
        self.style = Style()
        self.style.theme_use("default")

        self.options = \
            (CHARACTER_MANAGER, MANEUVERS, DICE_ROLLER, ENCOUNTER_GENERATOR, NAME_SELECTOR)
        self.current_option = DICE_ROLLER
        trace.exit()

    def _initialize_ui_variables(self):
        trace.entry()
        self.selector_widget = StringVar()
        self.selector_widget.set(self.options[0])
        self.selector_widget.trace("w", lambda *args: self.option_change_callback())
        trace.exit()

    def _init_ui_title(self):
        title_frame = Frame(self, relief=RAISED, borderwidth=1)
        title_frame.pack(fill=BOTH, expand=True)
        title_label = Label(title_frame, text="Console")
        title_label.pack()

    def _init_ui_selector(self):
        self.selector_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.selector_frame.pack(fill=BOTH, expand=True)
        selector_prompt_label = Label(self.selector_frame, text="Option to select: ")
        selector_prompt_label.pack(side=LEFT)
        self.option_selector = \
            OptionMenu(self.selector_frame, self.selector_widget, *self.options)
        self.option_selector.pack(side=RIGHT)

    def _add_entries_to_option_selector(self):
        trace.entry()
        clear_option_menu(self.option_selector)
        refresh_option_menu(self.option_selector, self.selector_widget, self.options)
        self.set_current_option(self.selector_widget.get())
        trace.exit()

    def set_current_option(self, option):
        """
        Sets the current option to the option specified.
        :param option: The option to set.  Specifies which child console is desired.
        """
        trace.entry()
        self.current_option = option
        trace.exit()

    def option_change_callback(self):
        """Handles the callback when an option is selected by storing the selected option."""
        trace.entry()
        trace.detail("Option selected is %r" % self.selector_widget.get())
        self.set_current_option(self.selector_widget.get())
        trace.exit()

    def launch_option(self):
        """Launches or switches focus to the specified option."""
        trace.entry()
        trace.detail("Trigger option %s" % self.current_option)
        if self.current_option == CHARACTER_MANAGER:
            trace.flow("Start character manager")
            self._start_character_manager()

        elif self.current_option == MANEUVERS:
            trace.flow("Start maneuver table")
            self._start_maneuver_table()

        elif self.current_option == DICE_ROLLER:
            trace.flow("Start dice roller")
            self._start_dice_roller()

        elif self.current_option == ENCOUNTER_GENERATOR:
            trace.flow("Start encounter generator")
            self._start_encounter_generator()

        else:
            trace.flow("Start name selector")
            self._start_name_selector()

        trace.exit()

    def _start_character_manager(self):
        """
        Launches or switches focus to the character manager
        """
        if self.character_manager_window is None:
            trace.flow("Open character manager")
            self.character_manager_window = Toplevel(self)
            self.character_manager_window.wm_title(CHARACTER_MANAGER)
            self.character_manager_window.protocol("WM_DELETE_WINDOW",
                                                   self.character_manager_closed)
            self.character_manager = CharacterManager(self.character_manager_window,
                                                      self,
                                                      self,
                                                      self.character_database)
        elif self.character_manager_window.state() == 'normal':
            trace.flow("Shift focus to character manager")
            self.character_manager_window.focus_set()
        else:
            trace.flow("Deiconify character manager")
            self.character_manager_window.deiconify()

    def _start_maneuver_table(self):
        """
        Launches or switches focus to the maneuver table
        """
        if self.maneuver_window is None:
            trace.flow("Open maneuver table")
            self.maneuver_window = Toplevel(self)
            self.maneuver_window.wm_title(MANEUVERS)
            self.maneuver_window.protocol("WM_DELETE_WINDOW", self.maneuver_window_closed)
            self.maneuver_table = ManeuverTable(self.maneuver_window, self)
        elif self.maneuver_window.state() == 'normal':
            trace.flow("Switch focus to maneuver table")
            self.maneuver_window.focus_set()
        else:
            trace.flow("Deiconify maneuver table")
            self.maneuver_window.deiconify()

    def _start_dice_roller(self):
        """
        Launches or switches focus to the dice roller
        """
        if self.dice_roller_window is None:
            trace.flow("Open dice roller")
            self.dice_roller_window = Toplevel(self)
            self.dice_roller_window.wm_title(DICE_ROLLER)
            self.dice_roller_window.protocol("WM_DELETE_WINDOW", self.dice_roller_closed)
            self.dice_roller = DiceRoller(self.dice_roller_window, self)
        elif self.dice_roller_window.state() == 'normal':
            trace.flow("Switch focus to dice roller")
            self.dice_roller_window.focus_set()
        else:
            trace.flow("Deiconify window")
            self.dice_roller_window.deiconify()

    def _start_encounter_generator(self):
        """
        Launches or switches focus to the encounter generator
        """
        if self.encounter_generator is None:
            trace.flow("Open encounter generator")
            self.encounter_generator = Toplevel(self)
            self.encounter_generator.wm_title(ENCOUNTER_GENERATOR)
            self.encounter_generator.protocol("WM_DELETE_WINDOW",
                                              self.encounter_generator_closed)
            EncounterGenerator(self.encounter_generator, self, "./encounters")
        elif self.encounter_generator.state() == 'normal':
            trace.flow("Switch focus to encounter generator")
            self.encounter_generator.focus_set()
        else:
            trace.flow("Deiconify window")
            self.encounter_generator.deiconify()

    def _start_name_selector(self):
        """
        Launches or switches focus to the name selector
        """
        if self.name_selector_window is None:
            trace.flow("Open name selector")
            self.name_selector_window = Toplevel(self)
            self.name_selector_window.wm_title(NAME_SELECTOR)
            self.name_selector_window.protocol("WM_DELETE_WINDOW", self.name_selector_closed)
            self.name_selector = NameSelector(self.name_selector_window, self)
        elif self.name_selector_window.state() == 'normal':
            trace.flow("Switch focus to name selector")
        else:
            trace.flow("Deiconify window")
            self.name_selector_window.deiconify()

    def character_manager_closed(self):
        """
        Callback when a request is received to close the character manager
        """
        trace.entry()
        self.character_manager_window.destroy()
        self.character_manager_window = None
        self.character_manager = None

        trace.exit()

    def maneuver_window_closed(self):
        """
        Callback when a request is received to close the maneuver window
        """
        trace.entry()
        self.maneuver_window.destroy()
        self.maneuver_window = None
        self.maneuver_table = None

        trace.exit()

    def dice_roller_closed(self):
        """
        Callback when a request is received to close the dice roller
        """
        trace.entry()
        self.dice_roller_window.destroy()
        self.dice_roller_window = None
        self.dice_roller = None

        trace.exit()

    def encounter_generator_closed(self):
        """
        Callback when a request is received to close the encounter generator
        """
        trace.entry()
        self.encounter_generator.destroy()
        self.encounter_generator = None

        trace.exit()

    def name_selector_closed(self):
        """
        Callback when a request is received to close the name selector
        """
        trace.entry()
        self.name_selector_window.destroy()
        self.name_selector_window = None
        self.name_selector = None

        trace.exit()

    def characters_updated(self):
        """
        Tell any other objects using the characters that the characters have been updated.
        """
        trace.entry()
        if self.maneuver_table is not None:
            self.maneuver_table.characters_updated()
        if self.character_manager is not None:
            self.character_manager.characters_updated()
        trace.exit()


def main():
    """
    Start an instance of the MERP console.
    """
    root = Tk()
    trace.init("console")
    Console()
    root.mainloop()


if __name__ == '__main__':
    main()
