#!/usr/bin/python
# -*- coding: utf-8 -*-
from future import standard_library
import sys

import trace_log as trace

from tkinter import Tk, LEFT, RIGHT, BOTH, RAISED, StringVar, OptionMenu, Toplevel
from tkinter.ttk import Frame, Style, Label, Button
from tk_helper import clear_option_menu, refresh_option_menu
from Character.CharacterManager import CharacterManager
from CharacterDatabase.CharacterDatabase import CharacterDatabase
from DiceRoller.DiceRoller import DiceRoller
from Encounters.EncounterGenerator import EncounterGenerator
from Maneuvers.ManeuverTable import ManeuverTable
from NameDatabase.NameSelector import NameSelector

standard_library.install_aliases()

sys.path.append('../')  #
sys.path.append('Character')  #
sys.path.append('CharacterDatabase')  #
sys.path.append('DiceRoller')  #
sys.path.append('Encounters/')  #
sys.path.append('Encounters/Modules')  #
sys.path.append('../Maneuvers')  #
sys.path.append('NameDatabase')  #

MANEUVERS = "Maneuvers"
CHARACTER_MANAGER = "Character manager"
DICE_ROLLER = "Dice roller"
ENCOUNTER_GENERATOR = "Encounter generator"
NAME_SELECTOR = "Name selector"


class Console(Frame):
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
        trace.entry()

        def initialize_variables():
            trace.entry()
            self.master.title("Console")
            self.style = Style()
            self.style.theme_use("default")

            self.options = (CHARACTER_MANAGER, MANEUVERS, DICE_ROLLER, ENCOUNTER_GENERATOR, NAME_SELECTOR)
            self.current_option = DICE_ROLLER
            trace.exit()

        def initialize_ui_variables():
            trace.entry()
            self.selector_widget = StringVar()
            self.selector_widget.set(self.options[0])
            self.selector_widget.trace("w", lambda *args: self.option_change_callback())
            trace.exit()

        def init_ui_title():
            title_frame = Frame(self, relief=RAISED, borderwidth=1)
            title_frame.pack(fill=BOTH, expand=True)
            title_label = Label(title_frame, text="Console")
            title_label.pack()

        def init_ui_selector():
            self.selector_frame = Frame(self, relief=RAISED, borderwidth=1)
            self.selector_frame.pack(fill=BOTH, expand=True)
            selector_prompt_label = Label(self.selector_frame, text="Option to select: ")
            selector_prompt_label.pack(side=LEFT)
            self.option_selector = OptionMenu(self.selector_frame, self.selector_widget, *self.options)
            self.option_selector.pack(side=RIGHT)

        def init_ui_go_button():
            selection_frame = Frame(self, relief=RAISED, borderwidth=1)
            selection_frame.pack(fill=BOTH, expand=True)
            selection_button = Button(selection_frame, text='Go!', command=self.launch_option)
            selection_button.pack()

        def add_entries_to_option_selector():
            trace.entry()
            clear_option_menu(self.option_selector)
            refresh_option_menu(self.option_selector, self.selector_widget, self.options)
            self.set_current_option(self.selector_widget.get())
            trace.exit()

        initialize_variables()
        initialize_ui_variables()

        init_ui_title()
        init_ui_selector()
        init_ui_go_button()

        add_entries_to_option_selector()

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def set_current_option(self, option):
        trace.entry()
        self.current_option = option
        trace.exit()

    def option_change_callback(self):
        trace.entry()
        trace.detail("Option selected is %r" % self.selector_widget.get())
        self.set_current_option(self.selector_widget.get())
        trace.exit()

    def launch_option(self):
        trace.entry()
        trace.detail("Trigger option %s" % self.current_option)
        if self.current_option == CHARACTER_MANAGER:
            trace.flow("Start character manager")
            if self.character_manager_window is None:
                trace.flow("Open character manager")
                self.character_manager_window = Toplevel(self)
                self.character_manager_window.wm_title(CHARACTER_MANAGER)
                self.character_manager_window.protocol("WM_DELETE_WINDOW", self.character_manager_closed)
                self.character_manager = CharacterManager(self.character_manager_window,
                                                          self,
                                                          self.character_database)
            else:
                trace.flow("Shift focus to character manager")
                self.character_manager_window.focus_set()

        elif self.current_option == MANEUVERS:
            trace.flow("Start maneuver table")
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

        elif self.current_option == DICE_ROLLER:
            trace.flow("Start dice roller")
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

        elif self.current_option == ENCOUNTER_GENERATOR:
            trace.flow("Start encounter generator")
            if self.encounter_generator is None:
                trace.flow("Open encounter generator")
                self.encounter_generator = Toplevel(self)
                self.encounter_generator.wm_title(ENCOUNTER_GENERATOR)
                self.encounter_generator.protocol("WM_DELETE_WINDOW", self.encounter_generator_closed)
                EncounterGenerator(self.encounter_generator, self, "./Encounters")
            elif self.encounter_generator.state() == 'normal':
                trace.flow("Switch focus to encounter generator")
                self.encounter_generator.focus_set()
            else:
                trace.flow("Deiconify window")
                self.encounter_generator.deiconify()

        else:
            trace.flow("Start name selector")
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

        trace.exit()

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

    @staticmethod
    def characters_updated(self):
        """
        Tell any other objects using the characters that the characters have been updated.
        """
        trace.entry()
        if self.maneuver_table is not None:
            self.maneuver_table.characters_updated()
        trace.exit()


def main():
    root = Tk()
    trace.init("")
    Console()
    root.mainloop()


if __name__ == '__main__':
    main()
