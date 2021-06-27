from __future__ import print_function
from builtins import input
from builtins import range
from builtins import object
from .EncounterTable import EncounterTable
import sys
import dice
import trace_log as trace
import os

sys.path.append('../../')


class EncounterCalculator(object):
    def __init__(self, base_directory):
        trace.entry()
        dice.randomize()
        self.base_directory = base_directory
        self.regions = {
            'Arnor and the North': 'Arnor',
            'Gondor and dependent territories': 'Gondor',
            'Harad and the South': 'Harad',
            'Wilderland': 'Wilderland'}
        self.modules = {}
        self.current_region = None
        self.current_module = None
        self.current_area = None
        self.region_dir = ""
        self.set_region("Arnor and the North")
        self.encounter_table = None
        self.num_encounters = 0
        trace.exit()

    def get_regions(self):
        return sorted(self.regions.keys())

    def set_region(self, region):
        trace.detail("Set region to %r" % region)
        self.current_region = region
        trace.detail("Region %s" % self.regions[region])
        self.region_dir = "%s/Modules/%s/" % (self.base_directory, self.regions[region])
        trace.detail("Region directory %s" % self.region_dir)
        self.modules = {}

    def read_modules(self):
        for module_file in os.listdir("%s" % self.region_dir):
            trace.flow("Load module %r" % module_file)
            module = EncounterTable(self.region_dir + module_file, False)
            module_name = module.get_module()
            self.modules[module_name] = module_file

    def get_modules(self):
        trace.detail("Returning %r" % self.modules.keys)
        return sorted(self.modules.keys())

    def set_module(self, module):
        trace.detail("Set module to %r" % module)
        self.current_module = module
        module_file = self.modules[module]
        self.encounter_table = EncounterTable(self.region_dir + module_file, True)

    def current_module(self):
        trace.detail("Current module %r" % self.current_module)
        return self.current_module

    def current_areas(self):
        trace.detail("Areas list %r" % self.encounter_table.get_areas_list())
        return self.encounter_table.get_areas_list()

    def set_area(self, area):
        trace.entry()
        trace.detail("Current area %r" % area)
        self.current_area = area
        self.__get_encounter_stats()
        trace.exit()

    def calculate_encounter(self):
        trace.entry()
        self.__determine_area()
        self.__get_encounter_stats()
        self.__print_encounter_stats()
        self.__determine_num_encounters()
        self.__get_encounters()
        self.__print_encounters()
        print()
        print()
        trace.exit()

    def __determine_area(self):
        trace.entry()
        areas_list = self.encounter_table.get_areas_list()
        print("Areas available")
        trace.detail("Areas %r" % areas_list)
        for area in areas_list:
            print(area)
        if self.current_area is not None:
            trace.flow("Area currently selected %s" % self.current_area)
            selected_area = input("Select area, or Enter to leave unchanged ")
            while selected_area != "" and selected_area not in areas_list:
                trace.flow("Bad area %s selected" % selected_area)
                selected_area = input("Try again ")
        else:
            trace.flow("No area currently selected")
            selected_area = input("Select area ")
            while selected_area not in areas_list:
                trace.flow("Bad area %s selected" % selected_area)
                selected_area = input("Try again ")
        if selected_area != "":
            self.current_area = selected_area
        trace.detail("Selected area now %s" % self.current_area)
        trace.exit()

    def __determine_num_encounters(self):
        trace.entry()
        num_encounters = input("Number of encounters to generate? ")
        while num_encounters.isdigit() is False:
            num_encounters = input("Try again ")
        self.num_encounters = int(num_encounters)
        trace.detail("Number of encounters %d" % self.num_encounters)
        trace.exit()

    def __get_encounter_stats(self):
        trace.entry()
        self.encounter_distance = self.encounter_table.encounter_distance(self.current_area)
        self.encounter_time = self.encounter_table.encounter_time(self.current_area)
        trace.exit()

    def __get_encounters(self):
        trace.entry()
        self.encounters = list()
        for i in range(0, self.num_encounters, 1):
            trace.flow("Check encounter index %d" % i)
            chance_roll = dice.d100()
            encounter_happened = self.encounter_table.encounter_happened(self.current_area, chance_roll)
            if self.current_module == "Lake Town (rural)":
                category_roll = 0
                encounter_roll = dice.d1000()
            else:
                category_roll = 0
                if self.encounter_table.categories_present:
                    category_roll = dice.d100()
                encounter_roll = dice.d100()
            if encounter_happened:
                trace.flow("Encounter happened")
                extras_roll = dice.d100()
                encounter_type = self.encounter_table.encounter_type(self.current_area, category_roll, encounter_roll)
                encounter_extras = \
                    self.encounter_table.get_encounter_extras(
                        encounter_type,
                        self.current_area,
                        extras_roll)
                self.encounters.append(encounter_type + encounter_extras)
            else:
                trace.flow("No encounter")
                self.encounters.append(None)
        trace.exit()

    def read_encounters(self, num_encounters):
        self.num_encounters = num_encounters
        self.__get_encounters()
        return self.encounters

    def __print_encounter_stats(self):
        trace.entry()
        print("Maximum distance per encounter chance was %r miles, maximum time %r hours"
              % (self.encounter_distance, self.encounter_time))
        trace.exit()

    def __print_encounters(self):
        trace.entry()
        print("Encounter results")
        for encounter in self.encounters:
            if encounter is not None:
                trace.flow("Encounter happened")
                print("Encounter was with %s" % encounter)
            else:
                trace.flow("No encounter")
                print("No encounter occurred")
        trace.exit()
