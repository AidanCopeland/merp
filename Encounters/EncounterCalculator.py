from EncounterTable import EncounterTable
import sys
sys.path.append('../')

import dice
import trace_log as trace
import os

class EncounterCalculator(object):
    def __init__(self):
        trace.entry()
        dice.randomize()
        self.modules = {}
        self.current_module = None
        self.current_area = None
        self.read_modules()
        trace.exit()

    def read_modules(self):
        for module_file in os.listdir("Modules"):
            trace.flow("Load module %r" % module_file)
            module = EncounterTable("Modules/" + module_file, False)
            module_name = module.get_module()
            self.modules[module_name] = module_file

    def get_modules(self):
        return sorted(self.modules.keys())


    def set_module(self, module):
        trace.detail("Set module to %r" % module)
        self.current_module = module
        module_file = self.modules[module]
        self.encounter_table = EncounterTable("Modules/" + module_file, True)


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
        print
        print
        trace.exit()

    def __determine_area(self):
        trace.entry()
        areas_list = self.encounter_table.get_areas_list()
        print "Areas available"
        trace.detail("Areas %r" % areas_list)
        for area in areas_list:
            print area
        if self.current_area is not None:
            trace.flow("Area currently selected %s" % self.current_area)
            selected_area = raw_input("Select area, or Enter to leave unchanged ")
            while selected_area != "" and selected_area not in areas_list:
                trace.flow("Bad area %s selected" % selected_area)
                selected_area = raw_input("Try again ")
        else:
            trace.flow("No area currently selected")
            selected_area = raw_input("Select area ")
            while selected_area not in areas_list:
                trace.flow("Bad area %s selected" % selected_area)
                selected_area = raw_input("Try again ")
        if selected_area != "":
            self.current_area = selected_area
        trace.detail("Selected area now %s" % self.current_area)
        trace.exit()

    def __determine_num_encounters(self):
        trace.entry()
        num_encounters = raw_input("Number of encounters to generate? ")
        while num_encounters.isdigit() is False:
            num_encounters = raw_input("Try again ")
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
                encounter_roll = dice.d1000()
            else:
                encounter_roll = dice.d100()
            if encounter_happened:
                trace.flow("Encounter happened")
                encounter_type = self.encounter_table.encounter_type(self.current_area, encounter_roll)
                self.encounters.append(encounter_type)
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
        print "Maximum distance per encounter chance was %r miles, maximum time %r hours" \
              % (self.encounter_distance, self.encounter_time)
        trace.exit()

    def __print_encounters(self):
        trace.entry()
        print "Encounter results"
        for encounter in self.encounters:
            if encounter is not None:
                trace.flow("Encounter happened")
                print "Encounter was with %s" % encounter
            else:
                trace.flow("No encounter")
                print "No encounter occurred"
        trace.exit()

