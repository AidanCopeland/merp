from WeatherTable import WeatherTable
import sys
sys.path.append('../')
import trace_log as trace
import dice
import os

class WeatherCalculator(object):
    def __init__(self, standard_tables, weather_table):
        """
        Initializes the Weather Calculator object.
        :param standard_tables: Tables containing standard weather information.
        :param weather_table: Tables containing weather information for the
        current module.
        """
        trace.entry()
        dice.randomize()
        self.regions = {
            'Arnor and the North': 'Arnor',
            'Gondor and dependent territories': 'Gondor',
            'Harad and the South': 'Harad',
            'Wilderland': 'Wilderland'}
        self.module_dir = ""
        self.modules = {}
        self.current_region = None
        self.current_module = None
        self.current_area = None
        self.set_region("Arnor and the North")

        self.standard_tables = standard_tables
        self.weather_table = weather_table

        self.min_temp_f = 0
        self.max_temp_f = 0

        self.reset_variables()


    def reset_variables(self):
        """
        Resets information tracking ongoing weather patterns.
        """
        self.min_temp_roll_modifier = 0
        self.max_temp_roll_modifier = 0
        self.precipitation = "None"
        self.precipitation_type_index = 0
        self.precipitation_start = 0
        self.precipitation_duration = 0
        self.precipitation_end = 0

        self.ongoing_rainfall_type = ""
        self.ongoing_rainfall_type_index = 0
        self.ongoing_rainfall_duration_left = 0
        self.ongoing_rainfall_daily_amount = 0

        self.wind_speed = 0
        self.wind_direction = 0

    def get_regions(self):
        return sorted(self.regions.keys())

    def set_region(self, region):
        trace.detail("Set region to %r" % region)
        self.current_region = region
        trace.detail("Region %s" % self.regions[region])
        self.region_dir = "Modules/" + "%s/" % self.regions[region]
        trace.detail("Region directory %s" % self.region_dir)
        self.modules = {}

    def read_modules(self):
        for module_file in os.listdir("%s" % self.region_dir):
            trace.flow("Load module %r" % module_file)
            module = WeatherTable(self.region_dir + module_file, False, self.standard_tables)
            module_name = module.get_module()
            self.modules[module_name] = module_file

    def get_modules(self):
        trace.detail("Returing %r" % self.modules.keys)
        return sorted(self.modules.keys())

    def calculate_weather(self):
        """
        Calculates the weather for the current date.
        """

        self.__calculate_temperatures()

        ongoing_precipitation = self.__check_for_ongoing_precipitation

        if (ongoing_precipitation == False):
            (self.precipitation, self.precipitation_type_index) = self.__calculate_precipitation()
            if self.precipitation != "":
                self.__store_new_precipitation_info()

        self.__calculate_cloud_cover()

        self.__calculate_wind()

    def __calculate_temperatures(self):
        """
        Calculates the daily minimum and maximum temperatures.
        """
        (self.min_temp_f, self.min_temp_roll_modifier) = self.__calculate_min_temp()
        (self.max_temp_f, self.max_temp_roll_modifier) = self.__calculate_max_temp()

    def __calculate_min_temp(self):
        """
        Calculates the daily minimum temperature.
        :return: Tuple of the daily minimum temperature in degrees Fahrenheit, and the modifier to apply
        to subsequent minimum temperature rolls.
        """
        temperature_roll = dice.d100high() + self.min_temp_roll_modifier
        trace.detail("Modified roll %d" % temperature_roll)

        temperature_mod_values = self.standard_tables.temperature_modification(False, temperature_roll)
        trace.detail("Ongoing modifier %d" % temperature_mod_values[1])
        self.min_temp_roll_modifier = temperature_mod_values[1]

        trace.detail("Temperature modifier %d" % temperature_mod_values[0])

        average_min_temp = self.weather_table.get_average_min_temperature(self.current_area,
                                                                          self.standard_tables.month)
        trace.detail("Average minimum temperature %d" % average_min_temp)

        terrain_mod = self.weather_table.terrain_min_temperature_modification()
        altitude_mod = self.weather_table.mountain_temperature_modification()

        min_temp = average_min_temp - temperature_mod_values[0] + terrain_mod - altitude_mod

        trace.detail("Daily min temp %d" % min_temp)

        return (min_temp, temperature_mod_values[1])

    def __calculate_max_temp(self):
        """
        Calculates the daily maximum temperature.
        :return: Tuple of the daily maximum temperature in degrees Fahrenheit, and the modifier to apply
        to subsequent maximum temperature rolls.
        """
        temperature_roll = dice.d100high() + self.max_temp_roll_modifier
        trace.detail("Modified roll %d" % temperature_roll)

        temperature_mod_values = self.standard_tables.temperature_modification(True, temperature_roll)
        trace.detail("Ongoing modifier %d" % temperature_mod_values[1])

        trace.detail("Temperature modifier %d" % temperature_mod_values[0])

        average_max_temp = self.weather_table.get_average_max_temperature(self.current_area,
                                                                          self.standard_tables.month)
        trace.detail("Average maximum temperature %d" % average_max_temp)

        terrain_mod = self.weather_table.terrain_min_temperature_modification()
        altitude_mod = self.weather_table.mountain_temperature_modification()

        max_temp = average_max_temp - temperature_mod_values[0] + terrain_mod - altitude_mod
        trace.detail("Daily max temp %d" % max_temp)

        return (max_temp, temperature_mod_values[1])

    def __check_for_ongoing_precipitation(self):
        """
        Checks whether there is any precipitation to carry over from the previous day, and updates current variables
        if so.
        :return: True if there is precipitation, False otherwise.
        """
        if self.ongoing_rainfall_duration_left > 0:
            trace.flow("Prolonged rainfall event: duration %d" % self.ongoing_rainfall_duration_left)
            self.__prolonged_precipitation_next_day()
            return True

        elif (self.precipitation_start + self.precipitation_duration > 24):
            trace.flow("Rainfall event from previous day")
            self.precipitation_duration = self.precipitation_duration - (24 - self.precipitation_start)
            trace.detail("Remaining duration %d" % self.precipitation_duration)
            self.precipitation_start = 0
            return True

        else:
            return False

    def __calculate_precipitation(self):
        """
        Calculates precipitation for the current day.
        :return: Tuple of the name of the precipitation and the index to the standard weather precipitation table
        for that precipitation type.
        """
        area_rainfall_chance = self.weather_table.get_rain_chance(self.current_area, self.standard_tables.month)
        terrain_mod = self.weather_table.terrain_rain_chance_modification()
        rainfall_chance = area_rainfall_chance + terrain_mod
        trace.detail("Area chance %d, terrain mod %d, total chance %d" %
                     (area_rainfall_chance, terrain_mod, rainfall_chance))

        rainfall_roll = dice.d100()
        trace.detail("Rainfall roll %d" % rainfall_roll)

        if (rainfall_roll > rainfall_chance):
            trace.flow("No rain")
            precipitation = "None"
            precipitation_type_index = 0
        else:
            trace.flow("Rain")
            (precipitation, precipitation_type_index) = \
                self.standard_tables.precipitation_type(self.min_temp_f, self.max_temp_f)

        return (precipitation, precipitation_type_index)

    def __prolonged_precipitation_next_day(self):
        """
        Pulls information about a prolonged precipitation event into the current variables after moving to the next
        day.
        """
        self.precipitation = self.ongoing_rainfall_type
        self.precipitation_type_index = self.ongoing_rainfall_type_index
        self.precipitation_duration = self.ongoing_rainfall_duration_left
        self.ongoing_rainfall_duration_left = \
            max(0, self.ongoing_rainfall_duration_left - (24 - self.precipitation_start))
        self.precipitation_start = 0

    def __store_new_precipitation_info(self):
        """
        Stores information about a new precipitation event into the current variables.
        """
        self.precipitation_start = self.standard_tables.precipitation_start_time()
        self.precipitation_duration = self.standard_tables.precipitation_duration(self.precipitation_type_index)
        self.precipitation_amount = self.standard_tables.precipitation_amount(self.precipitation_type_index)

        prolonged = self.standard_tables.is_precipitation_prolonged(self.precipitation_type_index)
        if (prolonged):
            self.ongoing_rainfall_type = self.precipitation
            self.ongoing_rainfall_type_index = self.precipitation_type_index
            self.ongoing_rainfall_daily_amount = self.precipitation_amount
            self.ongoing_rainfall_duration_left = self.precipitation_duration

    def __calculate_cloud_cover(self):
        """
        Determines the cloud cover for the current day and stores in current variables.
        """
        is_raining = (self.precipitation != "")
        self.cloud_cover = self.standard_tables.cloud_cover(self.standard_tables.month, is_raining)

    def __calculate_wind(self):
        """
        Calculates information about the wind for today and stores in current variables.
        """

        terrain_mod = self.weather_table.terrain_wind_speed_modification()
        altitude_mod = self.weather_table.mountain_wind_modification()

        self.wind_speed = \
            self.standard_tables.wind_speed(self.precipitation_type_index) + terrain_mod + altitude_mod

        self.wind_direction = self.__update_wind_direction(self.wind_direction)

    def set_wind(self, wind_direction):
        """
        Sets the wind direction to a specified value.  Values accepted are N, NE, E, SE, S, SW, W, NW
        :param wind_direction: The desired wind direction.
        """
        trace.detail("Configured wind direction %r" % wind_direction)

        if wind_direction.lower == "n":
            self.wind_direction = 0
        elif wind_direction.lower == "ne":
            self.wind_direction = 45
        elif wind_direction.lower == "e":
            self.wind_direction = 90
        elif wind_direction.lower == "se":
            self.wind_direction = 135
        elif wind_direction.lower == "s":
            self.wind_direction = 180
        elif wind_direction.lower == "sw":
            self.wind_direction = 225
        elif wind_direction.lower == "w":
            self.wind_direction = 270
        elif wind_direction.lower == "nw":
            self.wind_direction = 315

        trace.detail("Wind direction now %d degrees" % self.wind_direction)

    def __update_wind_direction(self, wind_direction):
        """
        Update the wind direction.
        :param wind_direction: The current wind direction, in degrees.
        :return: The updated wind direction, in degrees.
        """
        trace.detail("Current wind direction %d" % wind_direction)

        """
        Determine the variation in the wind by using 4d90 to determine the alteration in degrees.  The midpoint, 182,
        is taken as meaning no change.
        """
        dice_roll = dice.dcustom(90, 4)
        dice_roll =- 182
        trace.detail("Update wind direction by %d degrees" % dice_roll)

        wind_direction += dice_roll
        if (wind_direction >= 360):
            wind_direction -= 360

        trace.detail("New wind direction %d degrees" % wind_direction)

        return(wind_direction)

    def get_wind_compass_direction(self, wind_direction):
        """
        Determine the compass point from which the wind is currently blowing.
        :param wind_direction: The current wind direction, in degrees
        :return: The compass point, from the 16-point compass rose.
        """
        trace.detail("Wind direction (degrees) %d" % wind_direction)
        if wind_direction <= 11:
            compass = "North"
        elif wind_direction <= 33:
            compass = "North-north-east"
        elif wind_direction <= 56:
            compass = "North-east"
        elif wind_direction <= 78:
            compass = "East-north-east"
        elif wind_direction <= 101:
            compass = "East"
        elif wind_direction <= 123:
            compass = "East-south-east"
        elif wind_direction <= 145:
            compass = "South-east"
        elif wind_direction <= 168:
            compass = "South-south-east"
        elif wind_direction <= 191:
            compass = "South"
        elif wind_direction <= 213:
            compass = "South-south-west"
        elif wind_direction <= 236:
            compass = "South-west"
        elif wind_direction <= 258:
            compass = "West"
        elif wind_direction <= 281:
            compass = "West-north-west"
        elif wind_direction <= 303:
            compass = "North-west"
        elif wind_direction <= 326:
            compass = "North-north-west"
        else:
            compass = "North"

        trace.detail("Compass point %r" % compass)

        return compass

    def calculate_sunrise_sunset(self):
        """
        Calculate the sunrise and sunset for the current day.
        :return: Tuple of sunrise and sunset, in hours and fractions of hours.
        """

    def calculate_sunrise(self):
        """
        Get the current day of the year, as a number of days.  Compare with spring equinox: 30 Gwaeron.  Result is x.
        Solar declination: delta = 23.5deg * sin [(x/365)*360def]
        Get latitude of observer.
        If abs(-tan (latitude)* tan (decliation)) > 1, there is no sunrise or sunset.
        Calculate local hour angle of sunrise/sunset - degrees of earth's circumference between noon and sunrise/sunset.
        cos (angle) = -tan (latitude) * tan (declination)
        angle = cos-1 (equation above)
        Number of hours = 24 * (angle / 360)
        :return:
        """
        days_past_spring_equinox = self.standard_tables.get_days_past_spring_equinox
        return 0

    def calculate_sunset(self):
        return 0
