import sys
sys.path.append('../')
import readData

class EncounterData(object):
    def __init__(self, filename):

        txt = open(filename)

        self.__read_areas(txt)
        self.__read_chance(txt)
        self.__read_distance(txt)
        self.__read_time(txt)

        self.__read_encounters(txt)

        txt.close()

    def __read_areas(self, txt):
        assert (readData.get_next_keyword(txt) == "Areas")
        self.areas = readData.read_tabbed_line(txt)
        self.area_count = len(self.areas)
        print "There are %d areas" % self.area_count

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


    def __init_category_lists(self):
        self.categories = list()
        self.category_values = list()
        for area in self.areas:
            self.category_values.append(list())


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

    def encounter_happened(self, area_index, roll):
        chance = self.chance[area_index]
        if roll <= chance:
            return True
        else:
            return False

    def encounter_distance(self, area_index):
        return self.distance[area_index]

    def encounter_time(self, area_index):
        return self.time[area_index]

    def encounter_type(self, area_index, roll):
        encounter_list = self.encounter_values[area_index]
        index = 0
        for index in range(0, len(encounter_list)):
            encounter_value = encounter_list[index]
            if encounter_value >= roll:
                break

        return self.encounters[index]

test = EncounterData("Shire.txt")
encounter_happened = test.encounter_happened(0, 10)
encounter_distance = test.encounter_distance(0)
encounter_time = test.encounter_distance(0)
encounter_type = test.encounter_type(0, 42)

print "Encounter happened? %r. Distance was %d miles, time was %d hours, encounter was with %s" % (encounter_happened, encounter_distance, encounter_time, encounter_type)
