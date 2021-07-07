#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the EncounterGenerator used for generating random encounters.

Classes:
    EncounterGenerator
"""
from builtins import str
import sys
from tkinter import \
    Tk, LEFT, RIGHT, END, BOTH, TOP, RAISED, W, Y, StringVar, OptionMenu, Text, _setit
from tkinter.ttk import Frame, Style, Label, Entry, Scrollbar
from future import standard_library

import frame_utils
import trace_log as trace

from .encounter_calculator import EncounterCalculator

standard_library.install_aliases()

sys.path.append('../../')


class EncounterGenerator(Frame):
    """
    Class handling user-triggered random encounter generation.

    Methods:
        __init__(self, master, parent_console, base_directory)
        set_current_region(self, region)
        set_current_module(self, module)
        set_current_area(self, area)
        calculate_encounters(self)
        check_encounter_numbers(self)
        region_change_callback(self)
        module_change_callback(self)
        area_change_callback(self)
    """
    def __init__(self, master, parent_console, base_directory):
        trace.entry()
        Frame.__init__(self, master)

        self.parent_console = parent_console
        self.modules = ['']
        self.module_areas = ['']
        self.region_selector = None
        self.encounter_calculator = None
        self.current_module = StringVar()
        self.current_area = StringVar()
        self.module_selector = None
        self.current_region = StringVar()
        self.regions = ['']
        self.encounter_interval = StringVar()
        self.encounter_distance = StringVar()
        self.num_encounters = StringVar()
        self.area_selector = None
        self.encounter_text = Text()
        self.style = Style()
        self.region_frame = Frame()
        self.module_frame = Frame()
        self.area_frame = Frame()
        self.init_ui(base_directory)

        trace.exit()

    def init_ui(self, base_directory):
        """
        Initialize the user interface components of the EncounterGenerator.
        :param base_directory: The root directory in which EncounterGenerator is running.
        """
        trace.entry()

        self._initialize_variables(base_directory)

        self._init_ui_title()
        self._init_ui_region()
        self._init_ui_module()
        self._init_ui_module_area()
        self._init_ui_interval()
        self._init_ui_encounter_number()
        frame_utils.init_ui_go_button(self, 'Calculate encounters', self.calculate_encounters)
        self._init_ui_encounter_details()

        self._initialize_regions()
        self._initialize_modules_areas()

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def _initialize_variables(self, base_directory):
        trace.entry()
        self.master.title("Encounter Generator")
        self.style.theme_use("default")
        self.encounter_calculator = EncounterCalculator(base_directory)
        self.modules = ['']
        self.module_areas = ['']
        self.current_module = StringVar()
        self.num_encounters.set("1")

        self.regions = self.encounter_calculator.get_regions()
        self.current_region.set(self.regions[0])
        self.current_region.trace("w", lambda *args: self.region_change_callback())
        self.current_module.trace("w", lambda *args: self.module_change_callback())
        self.current_area.trace("w", lambda *args: self.area_change_callback())
        trace.exit()

    def _init_ui_title(self):
        title_frame = Frame(self, relief=RAISED, borderwidth=1)
        title_frame.pack(fill=BOTH, expand=True)
        title_label = Label(title_frame, text="Encounter Generator")
        title_label.pack()

    def _init_ui_region(self):
        self.region_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.region_frame.pack(fill=BOTH, expand=True)
        region_prompt_label = Label(self.region_frame, text="Current Region: ")
        region_prompt_label.pack(side=LEFT)
        self.region_selector = OptionMenu(self.region_frame,
                                          self.current_region,
                                          tuple(self.regions))
        self.region_selector.pack(side=RIGHT)

    def _init_ui_module(self):
        self.module_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.module_frame.pack(fill=BOTH, expand=True)
        module_prompt_label = Label(self.module_frame, text="Current Module: ")
        module_prompt_label.pack(side=LEFT)
        self.module_selector = OptionMenu(self.module_frame,
                                          self.current_module,
                                          tuple(self.modules))
        self.module_selector.pack(side=RIGHT)

    def _init_ui_module_area(self):
        self.area_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.area_frame.pack(fill=BOTH, expand=True)
        area_prompt_label = Label(self.area_frame, text="Area within Module: ")
        area_prompt_label.pack(side=LEFT)
        self.area_selector = OptionMenu(self.area_frame,
                                        self.current_area,
                                        tuple(self.module_areas))
        self.area_selector.pack(side=RIGHT)

    def _init_ui_interval(self):
        interval_frame = Frame(self, relief=RAISED, borderwidth=1)
        interval_frame.pack(fill=BOTH, expand=True)
        interval_label = Label(interval_frame, textvariable=self.encounter_interval)
        interval_label.pack(side=TOP, anchor=W)
        distance_label = Label(interval_frame, textvariable=self.encounter_distance)
        distance_label.pack(side=TOP, anchor=W)

    def _init_ui_encounter_number(self):
        encounter_number_frame = Frame(self, relief=RAISED, borderwidth=1)
        encounter_number_frame.pack(fill=BOTH, expand=True)
        encounter_prompt = Label(encounter_number_frame,
                                 text="Number of encounters to calculate: ")
        encounter_prompt.pack(side=LEFT)
        encounter_numbers = Entry(encounter_number_frame, textvariable=self.num_encounters)
        self.num_encounters.trace("w", lambda *args: self.check_encounter_numbers())
        encounter_numbers.pack(side=RIGHT)

    def _init_ui_encounter_details(self):
        encounter_details_frame = Frame(self, relief=RAISED, borderwidth=1)
        encounter_scrollbar = Scrollbar(encounter_details_frame)
        encounter_scrollbar.pack(side=RIGHT, fill=Y)
        self.encounter_text = Text(
            encounter_details_frame,
            yscrollcommand=encounter_scrollbar.set)
        encounter_scrollbar.config(command=self.encounter_text.yview)

        encounter_details_frame.pack(fill=BOTH, expand=True)
        self.encounter_text.pack(fill=BOTH)

    def _initialize_regions(self):
        trace.entry()
        region_selector_menu = self.region_selector['menu']
        region_selector_menu.delete(0, 'end')

        for region in self.regions:
            region_selector_menu.add_command(label=region,
                                             command=_setit(self.current_region,
                                                            region))

        self.set_current_region(self.current_region.get())
        trace.exit()

    def _initialize_modules_areas(self):
        trace.entry()
        self.modules = self.encounter_calculator.get_modules()
        self.current_module.set(self.modules[0])
        module_selector_menu = self.module_selector['menu']
        module_selector_menu.delete(0, 'end')

        for module in self.modules:
            module_selector_menu.add_command(label=module,
                                             command=_setit(self.current_module,
                                                            module))

        self.set_current_module(self.current_module.get())
        self.set_current_area(self.current_area.get())
        trace.exit()

    def set_current_region(self, region):
        """
        Updates encounter variables following a change to the region for which to generate
        encounters.
        :param region: The region for which to generate encounters.
        """
        trace.entry()
        self.encounter_calculator.set_region(region)
        self.encounter_calculator.read_modules()
        self.modules = self.encounter_calculator.get_modules()
        trace.detail("Modules %r" % self.modules)
        self.current_module.set(self.modules[0])
        self.current_module.set(self.modules[0])
        module_selector_menu = self.module_selector['menu']
        module_selector_menu.delete(0, 'end')
        for module in self.modules:
            module_selector_menu.add_command(
                label=module,
                command=_setit(self.current_module, module))
        self.set_current_module(self.current_module.get())
        trace.exit()

    def set_current_module(self, module):
        """
        Updates encounter variables following a change to the MERP module within a region.
        :param module: The MERP module for which to generate encounters.
        """
        trace.entry()
        self.encounter_calculator.set_module(module)
        self.module_areas = self.encounter_calculator.current_areas()
        self.current_area.set(self.module_areas[0])
        area_selector_menu = self.area_selector['menu']
        area_selector_menu.delete(0, 'end')
        for area in self.module_areas:
            area_selector_menu.add_command(label=area,
                                           command=_setit(self.current_area,
                                                          area))
        self.set_current_area(self.module_areas[0])
        trace.exit()

    def set_current_area(self, area):
        """
        Updates encounter variables following a change to the area within a MERP module.
        :param area: The area with the MERP module.
        """
        trace.entry()
        self.encounter_calculator.set_area(area)
        interval_text = \
            "Minimum time between encounters: " + \
            str(self.encounter_calculator.encounter_time) + \
            " hours"
        distance_text = \
            "Minimum distance between encounters: " + \
            str(self.encounter_calculator.encounter_distance) + \
            " miles"
        trace.detail("Encounter interval %r" % self.encounter_calculator.encounter_time)
        trace.detail("Encounter distance %r" % self.encounter_calculator.encounter_distance)
        self.encounter_interval.set(interval_text)
        self.encounter_distance.set(distance_text)
        self.num_encounters.set("1")
        self.encounter_text.delete(1.0, END)
        trace.exit()

    def calculate_encounters(self):
        """
        Generates the required number of encounters and adds the results to self.encounter_text.
        """
        trace.entry()
        self.encounter_text.delete(1.0, END)
        encounters = self.encounter_calculator.read_encounters(int(self.num_encounters.get()))
        encounter_output = '\n'.join([str(encounter) for encounter in encounters])
        self.encounter_text.insert(END, encounter_output)
        trace.exit()

    def check_encounter_numbers(self):
        """
        Validates that the specified number of encounters to generate is a digit, and replaces it
        with '1' otherwise.
        """
        trace.exit()
        if self.num_encounters.get().isdigit():
            trace.detail("OK")
        else:
            self.num_encounters.set(1)

    def region_change_callback(self):
        """
        Callback made when the region for calculating encounters has changed.
        """
        trace.entry()
        trace.detail("Region changed to %r" % self.current_region.get())
        self.set_current_region(self.current_region.get())
        trace.exit()

    def module_change_callback(self):
        """
        Callback made when the module within a region has changed.
        """
        trace.entry()
        trace.detail("Module changed to %r" % self.current_module.get())
        self.set_current_module(self.current_module.get())
        trace.exit()

    def area_change_callback(self):
        """
        Callback made when the area within a MERP module has changed.
        """
        trace.entry()
        trace.detail("Area changed to %r" % self.current_area.get())
        self.set_current_area(self.current_area.get())
        trace.exit()


def main(master=None, parent_console=None, base_directory="."):
    """
    Start the EncounterGenerator instance.
    :param master: The owning top-level widget.
    :param parent_console: The parent console instance.
    :param base_directory: The base directory in which this EncounterGenerator is running.
    """
    root = Tk()
    trace.init("EncounterGenerator")
    EncounterGenerator(master, parent_console, base_directory=base_directory)
    root.mainloop()


if __name__ == '__main__':
    main()
