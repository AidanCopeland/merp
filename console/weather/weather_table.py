"""
Creates the WeatherTable which stores weather parameters for a give region.

Classes:
    WeatherTable
"""
from builtins import range
import sys
import read_data
import trace_log as trace
sys.path.append('../../')


class WeatherTable:
    """
    Weather table containing weather parameters for a given region.

    Methods:
        __init__(self, filename, full_open, standard_tables)
        get_module(self)
        get_regions_list(self)
        get_average_min_temperature(self, region_name, month_name)
        get_average_max_temperature(self, region_name, month_name)
        get_rain_chance(self, region_name, month_name)
    """
    def __init__(self, filename, full_open, standard_tables):
        """
        Initializes a weather table.
        :param filename: File containing the weather table to open.
        :param full_open: Whether to load all information from the weather table,
        or just the module.
        :param standard_tables: Standard weather tables.
        """
        trace.entry()
        with open(filename) as weather_file:

            self.__load_module_name(weather_file)

            self.monthly_min_temps_list_by_region = list()
            self.monthly_max_temps_list_by_region = list()
            self.monthly_rain_chance_list_by_region = list()
            self.weather_extras = dict()

            if full_open:
                self.__load_regions(weather_file)
                self.__load_weather_parameters(weather_file)
                self.__load_weather_extras(weather_file)

                self.standard_tables = standard_tables

        trace.exit()

    def __load_module_name(self, weather_file):
        """
        Load the name of the module from the specified weather file and store.
        :param weather_file: Weather file to read.
        """
        trace.entry()
        read_data.move_past_keyword(weather_file, "Module")
        self.module = read_data.read_tabbed_line(weather_file)[0]
        trace.detail("Module %r" % self.module)
        trace.exit()

    def __load_regions(self, weather_file):
        """
        Load information about the regions contained in this module and store.
        :param weather_file: Weather file to read.
        """
        trace.entry()
        read_data.move_past_keyword(weather_file, "Regions")
        self.regions_list = read_data.read_tabbed_line(weather_file)
        self.regions_count = len(self.regions_list)
        trace.detail("Regions %r" % self.regions_list)
        trace.exit()

    def __load_weather_parameters(self, weather_file):
        """
        Load weather parameters stored in a per-region, per-area format.
        :param weather_file: Weather file to read.
        """
        trace.entry()
        read_data.move_past_keyword(weather_file, "Weather")
        self.__init_weather_lists()
        line = read_data.read_tabbed_line(weather_file)
        while line is not None:
            trace.flow("Read weather line")
            self.__read_month(line)
            self.__load_month_region_values(line)
            line = read_data.read_tabbed_line(weather_file)
        trace.exit()

    def __load_weather_extras(self, weather_file):
        """
        Load additional information used to determine weather for this module.
        :param weather_file: weather file to read.
        """
        trace.entry()
        read_data.move_past_keyword(weather_file, "Extras")
        self.__init_weather_extras()

        line = read_data.read_tabbed_line(weather_file)
        while line is not None:
            self.__load_weather_extras_entry(line)
            line = read_data.read_tabbed_line(weather_file)
        trace.detail("Weather extras %r" % self.weather_extras)
        trace.exit()

    def __init_weather_lists(self):
        """
        Initialize the lists used to store weather information.
        A list is defined to store monthly minimum and maximum temperatures, and
        daily rain chance.
        Each list contains one entry for each region in the module.  Each entry is
        a list of the values for that region on a per month basis.
        """
        trace.entry()
        self.monthly_min_temps_list_by_region = list()
        self.monthly_max_temps_list_by_region = list()
        self.monthly_rain_chance_list_by_region = list()
        for _ in self.regions_list:
            trace.flow("Initialize per-region weather params list")
            self.monthly_min_temps_list_by_region.append(list())
            self.monthly_max_temps_list_by_region.append(list())
            self.monthly_rain_chance_list_by_region.append(list())
        trace.exit()

    def __init_weather_extras(self):
        """
        Initializes additional weather information for this region.
        """
        trace.entry()
        self.weather_extras = dict()
        trace.exit()

    @staticmethod
    def __read_month(text_line):
        """
        Obtains the month value from a line in the weather module file.
        :param text_line: Line to read.
        :return: Month value from 1 (Narwain) to 12 (Girithron)
        """
        trace.entry()
        month = text_line.pop(0)
        assert 1 <= month <= 12
        trace.detail("Month %d" % month)
        trace.exit()
        return month

    def __load_month_region_values(self, text_line):
        """
        Loads the weather parameters for a given month into the per-region lists.
        :param text_line: Line to read.
        """
        trace.entry()
        for region_index in range(0, self.regions_count):
            trace.flow("Load region %d entries" % region_index)
            weather_info = text_line.pop(0)
            per_region_values = read_data.read_semicolon_text(weather_info)
            trace.detail("Per region values %r" % per_region_values)
            region_min_temp_list = self.monthly_min_temps_list_by_region[region_index]
            region_min_temp_list.append(int(per_region_values[0]))

            region_max_temp_list = self.monthly_max_temps_list_by_region[region_index]
            region_max_temp_list.append(int(per_region_values[1]))

            region_rain_chance_list = self.monthly_rain_chance_list_by_region[region_index]
            region_rain_chance_list.append(int(per_region_values[2]))
        trace.exit()

    def __load_weather_extras_entry(self, text_line):
        """
        Loads a single entry in the extras category.
        :param text_line: Line to read.
        """
        # pylint: disable=unused-argument
        # pylint: disable=no-self-use
        return

    def get_module(self):
        """
        Returns the name of the current module.
        """
        trace.entry()
        trace.detail("Module %r" % self.module)
        trace.exit()
        return self.module

    def get_regions_list(self):
        """
        Returns the list of the regions in the current module.
        """
        trace.entry()
        trace.detail("Regions list %r" % self.regions_list)
        trace.exit()
        return self.regions_list

    def get_average_min_temperature(self, region_name, month_name):
        """
        Returns the average minimum temperature for the specified region and month.
        :param region_name: The name of the region to check.
        :param month_name: The month to check.
        :return: The monthly minimum temperature.
        """
        trace.entry()
        trace.detail("Region %r, month %r" % (region_name, month_name))

        # Convert the region name and month into the index values.  The month index is
        # decremented by 1 to handle the fact that the 0th index contains information
        # for the first month.
        region_index = self.regions_list.index[region_name]
        month_index = (self.standard_tables.get_month_index(month_name)) - 1
        trace.detail("Region index %d, month index %d" % (region_index, month_index))

        region_min_temp_list = self.monthly_min_temps_list_by_region[region_index]
        min_temp = region_min_temp_list[month_index]
        trace.detail("Min temp %r" % min_temp)
        trace.exit()
        return min_temp

    def get_average_max_temperature(self, region_name, month_name):
        """
        Returns the average maximum temperature for the specified region
        and month.
        :param region_name: The name of the region to check.
        :param month_name: The month to check.
        :return: The monthly maximum temperature.
        """
        trace.entry()
        trace.detail("Region %r, month %r" % (region_name, month_name))

        # Convert the region name and month into the index values.  The month index is
        # decremented by 1 to handle the fact that the 0th index contains information
        # for the first month.
        region_index = self.regions_list.index[region_name]
        month_index = (self.standard_tables.get_month_index(month_name)) - 1
        trace.detail("Region index %d, month index %d" % (region_index, month_index))

        region_max_temp_list = self.monthly_max_temps_list_by_region[region_index]
        max_temp = region_max_temp_list[month_index]
        trace.detail("Max temp %r" % max_temp)
        trace.exit()
        return max_temp

    def get_rain_chance(self, region_name, month_name):
        """
        Returns the daily rain chance for the specified region and month.
        :param region_name: The name of the region to check.
        :param month_name: The month to check.
        :return: The daily rain chance.
        """
        trace.entry()
        trace.detail("Region %r, month %r" % (region_name, month_name))

        # Convert the region name and month into the index values.  The month index is
        # decremented by 1 to handle the fact that the 0th index contains information
        # for the first month.
        region_index = self.regions_list.index[region_name]
        month_index = (self.standard_tables.get_month_index(month_name)) - 1
        trace.detail("Region index %d, month index %d" % (region_index, month_index))

        region_rain_chance_list = self.monthly_rain_chance_list_by_region[region_index]
        rain_chance = region_rain_chance_list[month_index]
        trace.detail("Rain chance %r" % rain_chance)
        trace.exit()
        return rain_chance
