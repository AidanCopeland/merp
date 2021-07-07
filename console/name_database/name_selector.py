#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the NameSelector which allows random selection of character names.

Classes:
    NameSelector
"""
from builtins import range
import sys
from tkinter import Tk, LEFT, RIGHT, END, BOTH, RAISED, StringVar, OptionMenu, Text
from tkinter.ttk import Frame, Style, Label, Entry

from future import standard_library

import dice
import frame_utils
import trace_log as trace
from console.name_database.name_database import NameDatabase
from tk_helper import clear_option_menu, refresh_option_menu
standard_library.install_aliases()


sys.path.append('../../')


class NameSelector(Frame):
    """
    Interface to the name database, allowing selection of random character names based on race and
    gender.

    Methods:
         __init__(self, master, parent_console)
         init_ui(self)
         set_current_race(self, race)
         roll_dice(self)
         check_num_names(self, use_default)
         race_change_callback(self)
         gender_change_callback(self)
    """
    def __init__(self, master, parent_console):
        trace.entry()
        Frame.__init__(self, master)

        self.parent_console = parent_console
        self.style = Style()
        self.name_database = NameDatabase()
        self.races = self.name_database.get_races()
        trace.detail("List length is %d" % len(self.races))

        self.current_race_widget = StringVar()
        self.num_names_widget = StringVar()
        self.database_size_display = StringVar()
        self.gender_widget = StringVar()
        self.gender_widget_options = ()

        self.race_frame = Frame()
        self.race_selector = None
        self.db_size_frame = Frame()
        self.gender_frame = Frame()
        self.gender_selector = None

        self.name_output_widget = None

        self.num_males = 0
        self.num_females = 0

        self.init_ui()

        trace.exit()

    def init_ui(self):
        """
        Initializes the user interface components.
        """
        trace.entry()

        self._initialize_variables()
        self._initialize_ui_variables()
        dice.randomize()

        self._init_ui_title()
        self._init_ui_race_selector()
        self._init_ui_db_size_display()
        self._init_ui_gender_selector()
        self._init_ui_num_names_input()
        frame_utils.init_ui_go_button(self, 'Pick names', self.roll_dice)
        self._init_ui_output_display()

        self._add_entries_to_race_selector()

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def _initialize_variables(self):
        trace.entry()
        self.master.title("Name Selector")
        self.style.theme_use("default")

        self.num_males = self.name_database.get_num_males()
        self.num_females = self.name_database.get_num_females()

        trace.exit()

    def _initialize_ui_variables(self):
        trace.entry()

        trace.detail("List length is %d" % len(self.races))

        self.current_race_widget.set(self.races[0])
        self.current_race_widget.trace("w", lambda *args: self.race_change_callback())

        self.num_names_widget.set("1")

        self.database_size_display.set("Number of names available: %s male, %s female" %
                                       (self.num_males, self.num_females))

        self.gender_widget_options = ("Either", "Male", "Female")
        self.gender_widget.set("Either")
        self.gender_widget.trace("w", lambda *args: self.gender_change_callback)
        trace.exit()

    def _init_ui_title(self):
        title_frame = Frame(self, relief=RAISED, borderwidth=1)
        title_frame.pack(fill=BOTH, expand=True)
        title_label = Label(title_frame, text="Name Selector")
        title_label.pack()

    def _init_ui_race_selector(self):
        self.race_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.race_frame.pack(fill=BOTH, expand=True)
        race_prompt_label = Label(self.race_frame, text="Race to select: ")
        race_prompt_label.pack(side=LEFT)
        self.race_selector = OptionMenu(self.race_frame, self.current_race_widget, *self.races)
        self.race_selector.pack(side=RIGHT)

    def _init_ui_db_size_display(self):
        self.db_size_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.db_size_frame.pack(fill=BOTH, expand=True)
        db_size_label = Label(self.db_size_frame,
                              textvariable=self.database_size_display)
        db_size_label.pack(side=LEFT)

    def _init_ui_gender_selector(self):
        self.gender_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.gender_frame.pack(fill=BOTH, expand=True)
        gender_prompt_label = Label(self.gender_frame, text="Gender to choose: ")
        gender_prompt_label.pack(side=LEFT)
        self.gender_selector = OptionMenu(self.gender_frame,
                                          self.gender_widget,
                                          "Either",
                                          *self.gender_widget_options)
        self.gender_selector.pack(side=RIGHT)

    def _init_ui_num_names_input(self):
        num_names_frame = Frame(self, relief=RAISED, borderwidth=1)
        num_names_frame.pack(fill=BOTH, expand=True)
        num_names_prompt = Label(num_names_frame, text="Number of names to select: ")
        num_names_prompt.pack(side=LEFT)
        num_names_widget = Entry(num_names_frame, textvariable=self.num_names_widget)

        self.num_names_widget.trace("w", lambda *args: self.check_num_names(False))
        num_names_widget.pack(side=RIGHT)

    def _init_ui_output_display(self):
        name_output_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.name_output_widget = Text(name_output_frame)
        name_output_frame.pack(fill=BOTH, expand=True)
        self.name_output_widget.pack(fill=BOTH)

    def _add_entries_to_race_selector(self):
        trace.entry()
        clear_option_menu(self.race_selector)
        refresh_option_menu(self.race_selector, self.current_race_widget, self.races)
        self.set_current_race(self.current_race_widget.get())
        trace.exit()

    def set_current_race(self, race):
        """
        Updates internal variables when the selected race has changed.
        :param race: The selected race.
        """
        trace.entry()
        self.name_database.set_race(race)
        self.num_males = self.name_database.get_num_males()
        self.num_females = self.name_database.get_num_females()
        self.database_size_display.set("Number of names available: %s male, %s female" %
                                       (self.num_males, self.num_females))

        clear_option_menu(self.gender_selector)

        self.gender_widget_options = ("Either", "Male", "Female")
        if self.num_females == 0:
            trace.flow("No females")
            self.gender_widget_options = ("Male",)
            self.gender_widget.set("Male")

        refresh_option_menu(self.gender_selector, self.gender_widget, self.gender_widget_options)
        trace.exit()

    def roll_dice(self):
        """
        Rolls the dice to pick random names and inserts the generated names in
        self.name_output_widget.
        """
        trace.entry()
        self.name_output_widget.delete(1.0, END)
        self.check_num_names(True)
        num_names = int(self.num_names_widget.get())
        trace.detail("Number of names %r" % num_names)
        if num_names > 1:
            trace.flow("Multiple names")
            result_text = "Names chosen were:\n"
        else:
            trace.flow("Single name")
            result_text = "Name chosen was "
        for i in range(0, num_names):
            trace.flow("Choose name %r" % i)
            if self.gender_widget.get() == "Either":
                trace.flow("Get either gender")
                result_text += self.name_database.get_either() + "\n"
            elif self.gender_widget.get() == "Male":
                trace.flow("Get male name")
                result_text += self.name_database.get_male() + "\n"
            else:
                trace.flow("Get female name")
                result_text += self.name_database.get_female() + "\n"
            trace.detail("Result string now %s" % result_text)
        self.name_output_widget.insert(END, ("%s" % result_text))
        trace.exit()

    def check_num_names(self, use_default):
        """
        Validates that the requested number of names is a digit, and replaces it with "1" if not.
        :param use_default: Whether to replace an invalid value with the default.
        """
        trace.entry()
        if self.num_names_widget.get().isdigit():
            trace.detail("OK")
        elif use_default:
            self.num_names_widget.set(1)

    def race_change_callback(self):
        """
        Callback when the requested race has changed.
        """
        trace.entry()
        trace.detail("Race changed to %r" % self.current_race_widget.get())
        self.set_current_race(self.current_race_widget.get())
        trace.exit()

    def gender_change_callback(self):
        """
        Callback when the requested gender has changed.
        """
        trace.entry()
        trace.detail("Gender changed to %r" % self.gender_widget.get())
        trace.exit()


def main(master=None, parent_console=None):
    """
    Create an instance of the NameSelector.
    :param master: The owning window.
    :param parent_console: The parent Console instance.
    """
    root = Tk()
    trace.init("NameSelector")
    NameSelector(master, parent_console)
    root.mainloop()


if __name__ == '__main__':
    main()
