"""
Creates the EncounterTable used to store information about possible encounters in an area.

Classes:
    EncounterTable
"""
from builtins import map
from builtins import range
import sys
import read_data
import trace_log as trace

sys.path.append('../../')


class EncounterTable:
    """
    Class handling the parameters that determine which encounters are possible, and how likely they
    are to occur, in a given area.

    Methods:
        __init__(self, filename, full_open)
        get_module(self)
        get_areas_list(self)
        encounter_happened(self, area_name, roll)
        encounter_distance(self, area_name)
        encounter_time(self, area_name)
        encounter_type(self, area_name, category_roll, encounter_roll)
        get_category_value(self, area_index, roll)
        get_encounter_type(self, area_index, category, roll)
        get_encounter_extras(self, encounter_type, area_name, extras_roll)
    """
    def __init__(self, filename, full_open):
        trace.entry()
        with open(filename) as txt:

            self.__read_module(txt)

            self.categories = list()
            self.category_values = list()
            self.encounter_categories = list()
            self.encounters = list()
            self.encounter_values = list()
            self.encounter_extras = dict()

            if full_open:
                self.__read_areas(txt)
                self.__read_chance(txt)
                self.__read_distance(txt)
                self.__read_time(txt)

                self.__read_categories(txt)
                self.__read_encounters(txt)
                self.__read_extras(txt)

        trace.exit()

    def __read_module(self, txt):
        assert read_data.get_next_keyword(txt) == "Module"
        self.module = read_data.read_tabbed_line(txt)[0]

    def __read_areas(self, txt):
        assert read_data.get_next_keyword(txt) == "Areas"
        self.areas = read_data.read_tabbed_line(txt)
        self.area_count = len(self.areas)

    def __read_chance(self, txt):
        assert read_data.get_next_keyword(txt) == "Chance"
        self.chance = read_data.read_tabbed_line(txt)
        self.chance = list(map(int, self.chance))
        assert len(self.chance) == self.area_count

    def __read_distance(self, txt):
        assert read_data.get_next_keyword(txt) == "Distance"
        self.distance = read_data.read_tabbed_line(txt)
        self.distance = list(map(float, self.distance))
        assert len(self.distance) == self.area_count

    def __read_time(self, txt):
        assert read_data.get_next_keyword(txt) == "Time"
        self.time = read_data.read_tabbed_line(txt)
        self.time = list(map(float, self.time))
        assert len(self.time) == self.area_count

    def __read_categories(self, txt):
        keyword = read_data.opt_get_next_keyword(txt, "Categories")
        if keyword == "Categories":
            trace.flow("Category information present")
            self.__init_category_lists()
            self.categories_present = True
            line = read_data.read_tabbed_line(txt)
            while line is not None:
                self.__read_category_type(line)
                self.__read_category_area_values(line)
                line = read_data.read_tabbed_line(txt)
        else:
            trace.flow("Category information not present")
            self.categories_present = False

    def __read_encounters(self, txt):
        self.__init_encounter_lists()

        assert read_data.get_next_keyword(txt) == "Encounters"
        line = read_data.read_tabbed_line(txt)
        while line is not None:
            self.__read_encounter_type(line)
            self.__read_encounter_area_values(line)
            line = read_data.read_tabbed_line(txt)

    def __read_extras(self, txt):

        self.__init_encounter_extras()

        assert read_data.get_next_keyword(txt) == "Extras"
        line = read_data.read_tabbed_line(txt)
        while line is not None:
            self.__read_encounter_extras(line)
            line = read_data.read_tabbed_line(txt)
        trace.detail("Encounter extras %r" % self.encounter_extras)

    def __init_category_lists(self):
        self.categories = list()
        self.category_values = list()
        for _ in self.areas:
            self.category_values.append(list())

    def __init_encounter_lists(self):
        if self.categories_present:
            self.encounter_categories = list()
        self.encounters = list()
        self.encounter_values = list()
        for _ in self.areas:
            self.encounter_values.append(list())

    def __init_encounter_extras(self):
        self.encounter_extras = dict()

    def __read_category_type(self, line):
        category_type = line.pop(0)
        self.categories.append(category_type)
        assert len(line) == self.area_count

    def __read_category_area_values(self, line):
        for area_index in range(0, self.area_count):
            category_value = line.pop(0)
            category_value_list = self.category_values[area_index]
            category_value_list.append(int(category_value))

    def __read_encounter_type(self, line):
        if self.categories_present:
            encounter_category = line.pop(0)
            self.encounter_categories.append(encounter_category)
        encounter_type = line.pop(0)
        self.encounters.append(encounter_type)
        assert len(line) == self.area_count

    def __read_encounter_area_values(self, line):
        for area_index in range(0, self.area_count):
            encounter_value = line.pop(0)
            encounter_value_list = self.encounter_values[area_index]
            encounter_value_list.append(int(encounter_value))

    def __read_encounter_extras(self, line):
        encounter_type = line.pop(0)
        self.encounter_extras[encounter_type] = dict()
        extras_dict = self.encounter_extras[encounter_type]
        area_name = line.pop(0)
        if area_name == "All":
            trace.flow("All areas specified")
            extras_dict["all"] = (list(), list())
            next_area_index = -1
            area_details = extras_dict["all"]
        else:
            trace.flow("Area %r specified" % area_name)
            area = area_name
            extras_dict[area] = (list(), list())
            next_area_index = self.__next_details_area_index(line)
            area_details = extras_dict[area]

        parse_area = True
        while parse_area:
            trace.flow("Parse area")
            extras_chance_list = area_details[0]
            extras_details_list = area_details[1]
            area_list = line
            trace.detail("Area list %r" % area_list)
            if next_area_index != -1:
                area_list = line[:next_area_index]
                line = line[next_area_index:]
                area = line.pop(0)
                extras_dict[area] = (list(), list())
                next_area_index = self.__next_details_area_index(line)
                area_details = extras_dict[area]
                if next_area_index == -1:
                    trace.flow("Final area found")
            else:
                trace.flow("No more to parse")
                parse_area = False
            while len(area_list) >= 2:
                trace.flow("Get next set of into")
                chance = area_list.pop(0)
                details = area_list.pop(0)
                extras_chance_list.append(int(chance))
                extras_details_list.append(details)

    def __next_details_area_index(self, line):
        area_index = 0
        for entry in line:
            if entry in self.areas:
                return area_index
            area_index += 1
        return -1

    def get_module(self):
        """
        Returns the current MERP module.
        """
        trace.detail("Module %r" % self.module)
        return self.module

    def get_areas_list(self):
        """
        Returns the list of areas in the current module.
        """
        trace.detail("Areas list %r" % self.areas)
        return self.areas

    def encounter_happened(self, area_name, roll):
        """
        Determine whether an encounter happened.
        :param area_name: The name of the area within the current module.
        :param roll: The roll to determine whether an encounter happened.
        :return: True if an encounter happened, False otherwise.
        """
        trace.entry()
        trace.detail("Check if encounter happened, area %s, roll %d" % (area_name, roll))
        area_index = self.areas.index(area_name)
        chance = self.chance[area_index]
        trace.detail("Chance of encounter happening %d" % chance)
        if roll <= chance:
            trace.detail("Encounter happened")
            trace.exit()
            return True
        else:
            trace.detail("Encounter did not happen")
            trace.exit()
            return False

    def encounter_distance(self, area_name):
        """
        Determine the minimum distance between encounters in this area.
        :param area_name: The area in the current module.
        :return: The minimum time between encounters.
        """
        trace.entry()
        trace.detail("Get encounter distance, area %s" % area_name)
        area_index = self.areas.index(area_name)
        trace.detail("Distance is %d" % self.distance[area_index])
        trace.exit()
        return self.distance[area_index]

    def encounter_time(self, area_name):
        """
        Determine the minimum time between encounters in this area.
        :param area_name: The area in the current module.
        :return: The minimum time between encounters.
        """
        trace.entry()
        trace.detail("Get encounter time, area %s" % area_name)
        area_index = self.areas.index(area_name)
        trace.detail("Time is %d" % self.time[area_index])
        trace.exit()
        return self.time[area_index]

    def encounter_type(self, area_name, category_roll, encounter_roll):
        """
        Determine the type of encounter generated.
        :param area_name: The name of the area within the current MERP module.
        :param category_roll: Dice roll for determining the category of encounter.
        :param encounter_roll: Dice roll for determining the encounter.
        :return: Text describing the encounter.
        """
        trace.entry()
        trace.detail("Get encounter type, area %s" % area_name)
        area_index = self.areas.index(area_name)

        category_value = self.get_category_value(area_index, category_roll)
        trace.detail("Category %r" % category_value)

        encounter_type = self.get_encounter_type(area_index, category_value, encounter_roll)

        trace.exit()
        return encounter_type

    def get_category_value(self, area_index, roll):
        """
        Determine the category of encounter to generate within a given module.
        :param area_index: The area within the current MERP module.
        :param roll: Dice roll used to generate an encounter category.
        :return: The category of encounter to use, or None if the module does not use encounter
        categories.
        """
        if self.categories_present:
            trace.flow("Look for category, roll %d" % roll)
            category_list = self.category_values[area_index]
            index = 0
            for index, category_value in enumerate(category_list):
                if category_value >= roll:
                    trace.flow("Found category type, value %r" % self.categories[index])
                    break
            return self.categories[index]
        else:
            return None

    def get_encounter_type(self, area_index, category, roll):
        """
        Determines the type of encounter generated.
        :param area_index: The index of the area within the current MERP module.
        :param category: The category roll, or 0 if categories are not present in the module.
        :param roll: The encounter roll.
        :return: Text describing the type of encounter generated.
        """
        encounter_list = self.encounter_values[area_index]
        index = 0
        trace.flow("Look for encounter, category %r, roll %d" % (category, roll))
        for index, encounter_value in enumerate(encounter_list):
            encounter_category = None
            if self.categories_present:
                encounter_category = self.encounter_categories[index]
                trace.detail("Encounter category %r" % encounter_category)
            if ((self.categories_present is False) or
                    (encounter_category == category)):
                if encounter_value >= roll:
                    trace.flow("Found encounter type, value %r" % encounter_value)
                    break

        trace.detail("Encounter is %s" % self.encounters[index])
        return self.encounters[index]

    def get_encounter_extras(self, encounter_type, area_name, extras_roll):
        """
        Determines any additional text to add to an encounter description.
        :param encounter_type: The type of encounter.
        :param area_name: The area within the current module.
        :param extras_roll: Dice roll used to generate additional text.
        :return: Additional text to add, or "" if no additional text is required.
        """
        trace.entry()
        trace.detail("Look for encounter %r" % encounter_type)
        trace.detail("Encounter extras %r" % self.encounter_extras)
        # noinspection PyBroadException
        try:
            extras_dict = self.encounter_extras[encounter_type]
            extras_info = None
            trace.detail("Found additional info %r" % extras_dict)
            if "all" in extras_dict:
                trace.flow("Information for all areas")
                extras_info = extras_dict["all"]
            else:
                trace.flow("Information not for all areas")
                if area_name in extras_dict:
                    trace.flow("Information for this area")
                    extras_info = extras_dict[area_name]
            if extras_info is not None:
                trace.flow("Found matching info")
                index = 0
                for index, extra_value in enumerate(extras_info[0]):
                    if extra_value >= extras_roll:
                        trace.flow("Found extra info, value %d" % extra_value)
                        break
                extra_text = " (" + extras_info[1][index] + ")"
                trace.detail("Extra text %r" % extra_text)
                trace.exit()
                return extra_text
            else:
                trace.exit()
                return ""

        except KeyError:
            trace.detail("No additional info")
            trace.exit()
            return ""
