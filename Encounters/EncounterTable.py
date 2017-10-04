import sys
sys.path.append('../')
import readData
import trace_log as trace


class EncounterTable(object):
    def __init__(self, filename, full_open):
        trace.entry()
        txt = open(filename)

        self.__read_module(txt)

        if full_open:
            self.__read_areas(txt)
            self.__read_chance(txt)
            self.__read_distance(txt)
            self.__read_time(txt)

            self.__read_encounters(txt)

        txt.close()
        trace.exit()

    def __read_module(self, txt):
        assert (readData.get_next_keyword(txt) == "Module")
        self.module = readData.read_tabbed_line(txt)[0]

    def __read_areas(self, txt):
        assert (readData.get_next_keyword(txt) == "Areas")
        self.areas = readData.read_tabbed_line(txt)
        self.area_count = len(self.areas)

    def __read_chance(self, txt):
        assert (readData.get_next_keyword(txt) == "Chance")
        self.chance = readData.read_tabbed_line(txt)
        self.chance = map(int, self.chance)
        assert (len(self.chance) == self.area_count)

    def __read_distance(self, txt):
        assert (readData.get_next_keyword(txt) == "Distance")
        self.distance = readData.read_tabbed_line(txt)
        self.distance = map(float, self.distance)
        assert (len(self.distance) == self.area_count)

    def __read_time(self, txt):
        assert (readData.get_next_keyword(txt) == "Time")
        self.time = readData.read_tabbed_line(txt)
        self.time = map(float, self.time)
        assert (len(self.time) == self.area_count)

    def __read_encounters(self, txt):
        self.__init_encounter_lists()

        assert (readData.get_next_keyword(txt) == "Encounters")
        line = readData.read_tabbed_line(txt)
        while line is not None:
            self.__read_encounter_type(line)
            self.__read_encounter_area_values(line)
            line = readData.read_tabbed_line(txt)

    def __init_encounter_lists(self):
        self.encounters = list()
        self.encounter_values = list()
        for area in self.areas:
            self.encounter_values.append(list())

    def __read_encounter_type(self, line):
        encounter_type = line.pop(0)
        self.encounters.append(encounter_type)
        assert (len(line) == self.area_count)

    def __read_encounter_area_values(self, line):
        for index in range(0, self.area_count):
            encounter_value = line.pop(0)
            encounter_value_list = self.encounter_values[index]
            encounter_value_list.append(int(encounter_value))

    def get_module(self):
        trace.detail("Module %r" % self.module)
        return self.module

    def get_areas_list(self):
        trace.detail("Areas list %r" % self.areas)
        return self.areas

    def encounter_happened(self, area_name, roll):
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
        trace.entry()
        trace.detail("Get encounter distance, area %s" % area_name)
        area_index = self.areas.index(area_name)
        trace.detail("Distance is %d" % self.distance[area_index])
        trace.exit()
        return self.distance[area_index]

    def encounter_time(self, area_name):
        trace.entry()
        trace.detail("Get encounter time, area %s" % area_name)
        area_index = self.areas.index(area_name)
        trace.detail("Time is %d" % self.time[area_index])
        trace.exit()
        return self.time[area_index]

    def encounter_type(self, area_name, roll):
        trace.entry()
        trace.detail("Get encounter type, area %s, roll %d" % (area_name, roll))
        area_index = self.areas.index(area_name)
        encounter_list = self.encounter_values[area_index]
        index = 0
        for index in range(0, len(encounter_list)):
            encounter_value = encounter_list[index]
            if encounter_value >= roll:
                trace.flow("Found encounter type, value %d" % encounter_value)
                break

        trace.detail("Encounter is %s" % self.encounters[index])
        trace.exit()
        return self.encounters[index]

