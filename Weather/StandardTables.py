import sys
sys.path.append('../')
import trace_log as trace
import dice


class StandardTables(object):
    def __init__(self):

        self.month = "Yestarë"
        self.date = 1

        self.high_temperature_variation_by_month = (0, 3, 4, 2, 3, 4, 4, 3, 2, 1, 2, 4, 4)
        self.low_temperature_variation_by_month = (0, 5, 5, 4, 4, 3, 4, 2, 2, 2, 3, 4, 4)

        self.temperature_modification_roll_chart = (
            # An array of information about modifiers to apply to the monthly average minimum/maximum temperature
            # based on the monthly variation class.

            # Each top-level array entry is a column in the Temperature Modification Chart for variation classes
            # 1 - 5 respectively (with an empty entry for class 0).

            # Each column entry is an array of entries in the column.  The array of entries contains:
            # - Maximum resolved dice roll that matches this entry
            # - Modification (Fahrenheit) to apply to monthly average minimum/maximum (reverse sign when applying to minimum)
            # - Modification to apply to dice roll for subsequent day.

            (),
            (
                (25, -1, 0),
                (50, 0, 0),
                (75, 1, 0),
                (100, 2, 25),
                (116, 3, 25),
                (132, 4, 25),
                (148, 5, 50),
                (164, 6, 50),
                (173, 7, 50),
                (182, 8, 50),
                (199, 9, 75),
                (999, 10, 75)
            ),
            (
                (16, -3, 0),
                (32, -2, 0),
                (48, -1, 0),
                (64, 0, 0),
                (80, 1, 0),
                (96, 2, 25),
                (107, 3, 25),
                (118, 4, 25),
                (129, 5, 25),
                (140, 6, 50),
                (151, 7, 50),
                (162, 8, 50),
                (167, 9, 50),
                (172, 10, 50),
                (177, 11, 50),
                (182, 12, 75),
                (187, 13, 75),
                (999, 14, 75)
            ),
            (
                (12, -4, 0),
                (24, -3, 0),
                (36, -2, 0),
                (48, -1, 0),
                (60, 0, 0),
                (72, 1, 0),
                (84, 2, 0),
                (96, 3, 25),
                (104, 4, 25),
                (112, 5, 25),
                (120, 6, 25),
                (128, 7, 25),
                (136, 8, 50),
                (144, 9, 50),
                (152, 10, 50),
                (160, 11, 50),
                (168, 12, 50),
                (172, 13, 50),
                (176, 14, 50),
                (180, 15, 50),
                (184, 16, 75),
                (188, 17, 75),
                (192, 18, 75),
                (999, 19, 75)
            ),
            (
                (10, -4, 0),
                (20, -3, 0),
                (30, -2, 0),
                (40, -1, 0),
                (50, 0, 0),
                (60, 1, 0),
                (70, 2, 0),
                (80, 3, 0),
                (90, 4, 0),
                (100, 5, 25),
                (106, 6, 25),
                (112, 7, 25),
                (118, 8, 25),
                (124, 9, 25),
                (130, 10, 25),
                (136, 11, 50),
                (142, 12, 50),
                (148, 13, 50),
                (154, 14, 50),
                (160, 15, 50),
                (163, 16, 50),
                (166, 17, 50),
                (169, 18, 50),
                (172, 19, 50),
                (175, 20, 50),
                (178, 21, 75),
                (182, 22, 75),
                (185, 23, 75),
                (188, 24, 75),
                (999, 25, 75)
            ),
            (
                (5, -9, 0),
                (10, -8, 0),
                (15, -7, 0),
                (20, -6, 0),
                (25, -5, 0),
                (30, -4, 0),
                (35, -3, 0),
                (40, -2, 0),
                (45, -1, 0),
                (50, 0, 0),
                (55, 1, 0),
                (60, 2, 0),
                (65, 3, 0),
                (70, 4, 0),
                (75, 5, 0),
                (80, 6, 0),
                (85, 7, 0),
                (90, 8, 0),
                (95, 9, 0),
                (100, 10, 25),
                (103, 11, 25),
                (106, 12, 25),
                (109, 13, 25),
                (112, 14, 25),
                (115, 15, 25),
                (118, 16, 25),
                (121, 17, 25),
                (124, 18, 25),
                (127, 19, 25),
                (130, 20, 25),
                (133, 21, 50),
                (136, 22, 50),
                (139, 23, 50),
                (142, 24, 50),
                (145, 25, 50),
                (148, 25, 50),
                (151, 26, 50),
                (154, 27, 50),
                (157, 28, 50),
                (160, 29, 50),
                (161, 30, 50),
                (162, 31, 50),
                (163, 32, 50),
                (164, 33, 50),
                (165, 34, 50),
                (166, 35, 50),
                (167, 36, 50),
                (168, 37, 50),
                (169, 38, 50),
                (170, 39, 50),
                (171, 40, 75),
                (172, 41, 75),
                (173, 42, 75),
                (174, 43, 75),
                (175, 44, 75),
                (176, 45, 75),
                (177, 46, 75),
                (178, 47, 75),
                (179, 48, 75),
                (999, 49, 75)
            )
        )

        self.terrain = ""
        self.altitude = 0

        self.terrain_effects_chart = {
            # Dict containing modifiers to apply based on terrain.  Each entry contains an array, where the entries
            # specify:

            # - Low Temperature modification (F, positive)
            # - High Temperature modification (F, positive)
            # - Precipitation chance modification
            # - Wind speed modification (mph)

            # Note that mountains, coastal and sea have special case handling in code.
            # Mountains have a temperature modification of -3F per 1000'; a wind modification of +5mph per 1000'
            # Coastal areas have a temperature modification of -5F (cold), +5F (warm)
            # Sea areas have a temperature modification of -10F (cold), +10F (warm)
            "Rough/hills": (0, 0, 0, 5),
            "Forests": (-5, -5, 0, -5),
            "Jungle": (5, 5, 10, -10),
            "Swamp/marsh": (5, 5, 5, -5),
            "Plains": (0, 0, 0, 5),
            "Desert": (-10, 10, 0, 5),
            "Coastal": (-5, 5, 5, 5),
            "Sea": (-10, 5, 15, 10)
        }

        self.cloud_cover_chart = (
            # Array containing cloud cover change on a per-month basis.
            # Each entry contains the base % chance each month that the sky is clear, or partly cloudy
            (0, 0),

            (25, 55),
            (25, 54),
            (20, 53),

            (26, 45),
            (25, 52),
            (24, 52),

            (22, 67),
            (31, 58),
            (31, 63),

            (31, 60),
            (29, 54),
            (19, 42)
        )

        self.precipitation_type_chart = (
            # Array containing information about possible precipitation types.
            # Each row indicates, in order:
            # - Maximum roll required to obtain weather type
            # - Type of weather
            # - Minimum possible temperature (F) required for weather type
            # - Maximum possible temperature (F) required for weather type
            # - Weather duration class: (1) Short, (2) Medium, (3) Long
            # - Weather duration roll modifier
            # - Inches type: (0) None, (1) Light, (2) Heavy, (3) Prolonged
            # - Inches roll modification
            # - Wind type: (1) Light, (2) Heavy, (3) Storm
            # - Wind speed roll modification
            # - Modifier to Moving Maneuvers
            # - Modifier to Observation, Alertness, Awareness rolls
            # - Modifier to Tracking attempts
            # - Modifier to Direction Sense attempts
            (0, "None",             -999, 999, 1,   0, 0,   0, 1, -10,   0,    0,    0,   0),
            (2, "Heavy blizzard",   -999,  10, 2,  -5, 2,   5, 3,  60, -85, -100, -200, -50),
            (5, "Light blizzard",   -999,  20, 2,  10, 2,   5, 2,  30, -75,  -90,  -40, -35),
            (10, "Heavy snowstorm", -999,  25, 2,   5, 2,  -5, 2, -20, -50,  -50,  -25, -20),
            (20, "Light snowstorm", -999,  35, 2, -15, 1,  10, 2, -25  -25,  -25,  -10, -10),
            (25, "Sleetstorm",      -999,  35, 1, -15, 1, -35, 2, -20  -25,  -25,  -10,  -5),
            (27, "Hailstorm",       -999,  65, 1, -30, 1,   0, 2, -10  -25,    0,  -10, -10),
            (30, "Heavy fog",         20,  60, 1,  25, 0,   0, 1,   0  -75, -100,  -60, -50),
            (38, "Light fog",         30,  70, 2,  -5, 0,   0, 1, -25, -50,  -75,  -30, -30),
            (40, "Mist",              30, 999, 2, -20, 0,   0, 1, -25,   0,    0,   -5,   0),
            (45, "Drizzle",           25, 999, 1,  10, 1, -45, 1,   0,   0,    0,   -5,   0),
            (60, "Light rainstorm",   25, 999, 1,  45, 1, -20, 1,   0,   0,    0,  -50,   0),
            (70, "Heavy rainstorm",   25, 999, 1,  30, 1,  20, 2, -10, -25,  -25,  -50,  -5),
            (84, "Thunderstorm",      30, 999, 1, -20, 1,   0, 2, -10, -50,  -25,  -50, -10),
            (89, "Tropical storm",    40, 999, 3,   0, 3,  -5, 2,  30, -75,  -50, -200, -30),
            (94, "Monsoon",           55, 999, 3,  80, 3,  25, 3,  0,  -75,  -75, -200, -30),
            (97, "Gale",              40, 999, 3,   0, 3,  10, 3,  30, -75,  -75, -200, -20),
            (100, "Hurricane",        55, 999, 3,   5, 3,  20, 3, 100, -75,  -75, -200, -30)
        ),

        self.precipitation_duration_chart = (
            (
                (0, 0.5, 1, 0.5),
                (8, 1, 2, 1),
                (16, 2, 5, 1),
                (24, 3, 8, 1),
                (32, 4, 10, 2),
                (40, 5, 13, 2),
                (48, 6, 16, 3),
                (56, 7, 18, 3),
                (64, 8, 21, 4),
                (72, 9, 24, 4),
                (80, 10, 26, 5),
                (88, 11, 29, 5),
                (96, 12, 32, 6),
                (112, 14, 37, 8),
                (128, 16, 42, 9),
                (144, 18, 48, 10),
                (160, 20, 53, 11),
                (176, 22, 58, 12),
                (192, 24, 64, 14),
                (216, 27, 72, 16),
                (240, 30, 80, 18),
                (264, 33, 88, 20),
                (999, 36, 96, 25)
            )
        )

        self.precipitation_inches_chart = (
            # Array containing rainfall amount for a rainfall event.  Each entry contains the following:
            # - Maximum roll required to obtain rainfall amount
            # - Inches of rain, rainfall type Light
            # - Inches of rain, rainfall type Heavy
            # - Inches of rain per day, rainfall type Prolonged
            ( 0, 0.25,  1,  1),
            ( 5,  0.5,  1,  1),
            ( 10,   1,  3,  1),
            ( 15, 1.5,  5,  2),
            ( 20,   2,  6,  2),
            ( 25, 2.5,  8,  3),
            ( 30,   3, 10,  3),
            ( 40,   4, 13,  4),
            ( 50,   5, 16,  5),
            ( 60,   6, 20,  6),
            ( 70,   7, 23,  7),
            ( 80,   8, 26,  8),
            ( 90,   9, 30,  9),
            (100,  10, 33, 10),
            (120,  12, 40, 12),
            (140,  14, 46, 14),
            (160,  16, 53, 16),
            (180,  18, 60, 18),
            (200,  20, 66, 20),
            (230,  23, 76, 23),
            (260,  26, 86, 26),
            (999,  29, 96, 29)
        ),

        self.wind_speed_chart = (
            # Array containing daily wind speed.  Each entry contains the following:
            # - Maximum roll required to obtain wind speed
            # - Wind speed, wind type Light
            # - Wind speed, wind type Heavy
            # - Wind speed, wind type Storm
            (  0,  0,   1,   1),
            (  5,  1,   2,   2),
            ( 10,  2,   5,   4),
            ( 15,  3,   8,   6),
            ( 20,  4,  11,   8),
            ( 25,  5,  14,  11),
            ( 30,  6,  17,  14),
            ( 35,  7,  20,  17),
            ( 40,  8,  23,  20),
            ( 45,  9,  26,  24),
            ( 50, 10,  29,  28),
            ( 55, 11,  32,  32),
            ( 60, 12,  35,  36),
            ( 65, 13,  38,  39),
            ( 70, 14,  41,  42),
            ( 75, 15,  44,  45),
            ( 80, 16,  47,  48),
            ( 85, 17,  50,  50),
            ( 90, 18,  53,  52),
            ( 95, 19,  56,  54),
            (100, 20,  59,  56),
            (110, 21,  63,  60),
            (120, 22,  67,  65),
            (130, 23,  71,  70),
            (140, 24,  75,  80),
            (150, 25,  79,  90),
            (160, 26,  83, 100),
            (170, 27,  87, 115),
            (180, 28,  91, 130),
            (190, 29,  95, 145),
            (200, 30, 100, 165),
            (220, 31, 105, 185),
            (240, 32, 110, 205),
            (260, 33, 115, 230),
            (280, 34, 120, 255),
            (999, 35, 125, 300)
        )

        self.beaufort_scale_chart = (
            # Beaufort scale chart.  Each entry contains
            # - Beaufort number
            # - Maximum wind speed, mph
            # - Description
            # - Land conditions
            (0, 1, "Calm", "Smoke rises vertically"),
            (1, 3, "Light air", "Direction shown by smoke drift but not wind vanes"),
            (2, 7, "Light breeze", "Wind felt on face; leaves rustle; wind vane moved by wind"),
            (3, 12, "Gentle breeze", "Leaves and small twigs in constant motion; light flags extended"),
            (4, 18, "Moderate breeze", "Raises dust and loose paper; small branches moved"),
            (5, 24, "Fresh breeze", "Small trees in leaf begin to sway; crested wavelets form on inland waters"),
            (6, 31, "Strong breeze", "Large branches in motion"),
            (7, 38, "High wind, moderate gale, near gale", "Whole trees in motion; inconvenience felt when walking against the wind"),
            (8, 46, "Gale, fresh gale", "Twigs break off trees; generally impedes progress"),
            (9, 54, "Strong/severe gale", "Slight structural damage (chimney pots and slates removed)"),
            (10, 63, "Storm, whole gale", "Seldom experienced inland; trees uprooted; considerable structural damage"),
            (11, 72, "Violent storm", "Very rarely experienced; accompanied by widespread damage"),
            (12, 300, "Hurricane", "Devastation")
        )

    def celsius_from_fahrenheit(self, fahrenheit):
        """
        Returns a temperature in Celsius obtained from a specified temperature in Fahrenheit.
        :param fahrenheit: The temperature in degrees Fahrenheit.
        :return: The temperature in degrees Celsius.
        """
        celsius = ((fahrenheit - 32) * 5 / 9)
        return celsius

    def temperature_modification(self, high_temp, roll):
        """
        Determines the modification to apply to the average monthly temperature.
        :param high_temp: Whether to look for the high temperature modification (or the low temperature modification)
        :param roll: The modified temperature roll.
        :return: Tuple of the modifier to apply to temperature, and a modifier to ongoing temperature rolls.
        """

        if (high_temp):
            modification_class = self.__high_temperature_modification_class(self.month)
        else:
            modification_class = self.__low_temperature_modification_class(self.month)

        assert (modification_class >= 1)
        assert (modification_class <= 5)
        modification_table = self.temperature_modification_roll_chart[modification_class]
        table_index = 0
        modification_table_entry = modification_table[table_index]

        if (roll > 999):
            roll = 999

        while (modification_table_entry[0] > roll):
            table_index += 1
            modification_table_entry = modification_table[table_index]

        trace.detail("Temperature modification %d, roll modification %d" %
                     (modification_table_entry[1], modification_table_entry[2]))
        return (modification_table_entry[1], modification_table_entry[2])


    def __high_temperature_modification_class(self, month):
        """
        Returns the variation class for maximum temperature based on a specified month.
        :param month: The month name.
        :return: The variation class.
        """
        month_index = self.get_month_index(month)
        return self.high_temperature_variation_by_month[month_index]

    def __low_temperature_modification_class(self, month):
        """
        Returns the variation class for minimum temperatures based on a specified month.
        :param month: The month name.
        :return: The variation class.
        """
        month_index = self.get_month_index(month)
        return self.low_temperature_variation_by_month[month_index]

    def set_terrain(self, terrain):
        """
        Updates the current terrain, used to modify temperature, precipitation chance
        and wind speed.
        :param terrain: The current terrain.
        """
        self.terrain = terrain

    def terrain_min_temperature_modification(self):
        """
        Determines the modification to minimum temperature based on terrain.
        :return: The modification (positive) in degrees Fahrenheit.
        """
        terrain_info = self.terrain_effects_chart[self.terrain]
        return terrain_info[0]

    def terrain_max_temperature_modification(self):
        """
        Determines the modification to maximum temperature based on terrain.
        :return: The modification (positive) in degrees Fahrenheit.
        """
        terrain_info = self.terrain_effects_chart[self.terrain]
        return terrain_info[1]

    def set_altitude(self, altitude):
        """
        Updates the current altitude, used to modify temperature and wind speed.
        :param altitude: The current altitude.
        """
        self.altitude = altitude

    def mountain_temperature_modification(self):
        """
        Determines the modification to temperatures based on altitude.
        :return: The modification (negative) in degrees Fahrenheit.
        """
        return round((3 * self.altitude) / 1000)

    def mountain_wind_modification(self):
        """
        Determines the modification to wind speed based on altitude.
        :return: The modification (positive) in mph.
        """
        return round((5 * self.altitude) / 1000)

    def terrain_rain_chance_modification(self):
        """
        Determines the modification to the percentage chance of rain based on
        the current terrain.
        :return: The modification (positive) in percentage points.
        """
        terrain_info = self.terrain_effects_chart[self.terrain]
        return terrain_info[2]

    def terrain_wind_speed_modification(self):
        """
        Determines the modification to wind speed based on terrain.
        :return: The modification (positive) in mph.
        """
        terrain_info = self.terrain_effects_chart[self.terrain]
        return terrain_info[3]

    def cloud_cover(self, month, is_raining):
        """
        Determines the cloud cover for the current day.
        :param month: The current month.
        :param is_raining: Whether there is any precipitation for today.
        :return: The level of cloud cover.
        """
        cloud_roll = dice.d100high()
        if (is_raining):
            cloud_roll += 30

        month_index = self.get_month_index(month)
        cloud_cover_info = self.cloud_cover_chart[month_index]
        if (cloud_roll < cloud_cover_info[0]):
            cloud_cover = "Clear"
        elif (cloud_roll < cloud_cover_info[1]):
            cloud_cover = "Partly cloudy"
        else:
            cloud_cover = "Cloudy"
        return cloud_cover

    def precipitation_type(self, min_temp, max_temp):
        """
        Determines the type of precipitation that occurs in the current day.
        The precipitation selected must be suitable for the day's temperature.

        :param min_temp: The minimum temperature for this day.
        :param max_temp: The maximum temperature for this day.
        :return: Tuple of the index to the precipitation type array, and the precipitation type.
        """
        found_precipitation = False
        trace.detail("Daily minimum %d, maximum %d (F)" % (min_temp, max_temp))
        precipitation_index = -1
        precipitation = self.precipitation_type_chart[precipitation_index]
        precipitation_max_roll = 0

        while (not found_precipitation):
            chance_roll = dice.d100()
            trace.detail("Dice roll %d" % chance_roll)

            while precipitation_max_roll < chance_roll:
                trace.detail(
                    "Skip precipitation type, max roll %d" % precipitation_max_roll)
                precipitation_index += 1
                precipitation = self.precipitation_type_chart[precipitation_index]
                precipitation_max_roll = precipitation[0]

            precipitation_min_temp = precipitation[2]
            precipitation_max_temp = precipitation[3]
            trace.detail("Precipitation has max temp %d, min temp %d" %
                         (precipitation_min_temp, precipitation_max_temp))
            if ((max_temp > precipitation_min_temp) or
                    (min_temp < precipitation_max_temp)):
                trace.flow("Found precipitation type %r, index %d" %
                           (precipitation[1], precipitation_index))
                found_precipitation = True
        return (precipitation_index, precipitation[1])

    def precipitation_start_time(self):
        """
        Determines the time at which a precipitation event starts in the current day.
        :return: The time that precipitation starts, to the nearest hour.
        """
        chance_roll = dice.dcustom(24)
        trace.detail("Start time %d" % chance_roll)
        return chance_roll

    def precipitation_duration(self, precipitation_index):
        """
        Determines the duration of a precipitation event starting in the current day.
        :param precipitation_index: The index to self.precipitation_type_chart for the precipitation event.
        :return: The duration in hours of the precipitation event.
        """
        trace.flow("Get precipitation duration, index %d" % precipitation_index)
        precipitation_info = self.precipitation_type_chart[precipitation_index]
        duration_class = precipitation_info[4]
        duration_modifier = precipitation_info[5]
        trace.detail("Duration class %d, modifier %d" % (duration_class, duration_modifier))
        assert((duration_class >= 1) and (duration_class <= 3))
        duration_roll = dice.d100high() + duration_modifier
        trace.detail("Modified roll %d" % duration_roll)
        duration_max_roll = 0
        duration_index = 0
        duration_info = self.precipitation_duration_chart[duration_index]

        while (duration_max_roll < duration_roll):
            trace.flow("Skip duration info, max roll %d" % duration_max_roll)
            duration_info = self.precipitation_duration_chart[duration_index]
            duration_max_roll = duration_info[0]
            duration_index += 1

        # This relies on duration_class taking values 1 - 3 and the 0th index being taken by the dice roll.
        duration = duration_info[duration_class]
        if duration_class == 2:
            duration *= 24
        trace.detail("Duration %d hours" % duration)
        return duration

    def is_precipitation_prolonged(self, precipitation_index):
        """
        Determines whether a precipitation type is a prolonged event.
        :param precipitation_index: The index to self.precipitation_type_chart for the precipitation event.
        :return: True if the precipitation event is prolonged, False otherwise.
        """
        duration_class = self.precipitation_type_chart[precipitation_index][4]
        trace.detail("Duration class %d" % duration_class)
        return (duration_class == 2)

    def precipitation_amount(self, precipitation_index):
        """
        Determines the amount of precipitation that falls in an event starting in the current day.
        :param precipitation_index: The index to self.precipitation_type_chart for the precipitation event.
        :return: The number of inches that fall (inches per day for a prolonged event)
        """
        trace.flow("Get precipitation_amount, precipitation index %d" % precipitation_index)
        precipitation_info = self.precipitation_type_chart[precipitation_index]
        amount_class = precipitation_info[6]
        amount_modifier = precipitation_info[7]
        assert(amount_class <= 3)
        if (amount_class == 0):
            trace.flow("No precipitation")
            return 0

        amount_roll = dice.d100high() + amount_modifier
        trace.detail("Modified roll %d" % amount_roll)
        amount_max_roll = 0
        amount_index = 0
        amount_info = self.precipitation_inches_chart[amount_index]
        while (amount_max_roll < amount_roll):
            trace.flow("Skip amount info, max roll %d" % amount_max_roll)
            amount_info = self.precipitation_inches_chart[amount_index]
            amount_max_roll = amount_info[0]
            amount_index += 1

        amount = amount_info[amount_class]
        trace.detail ("Amount %d inches" % amount)
        return amount

    def wind_speed(self, precipitation_index):
        """
        Determines the wind speed that occurs based on a specified precipitation event.
        :param precipitation_index: The index to self.precipitation_type_chart for the precipitation event.
        :return: The wind speed in miles per hour.
        """
        trace.flow("Get wind speed, precipitation index %d" % precipitation_index)
        precipitation_info = self.precipitation_type_chart[precipitation_index]
        wind_type = precipitation_info[8]
        wind_modifier = precipitation_info[9]
        assert (wind_type <= 3)

        wind_roll = dice.d100high() + wind_modifier
        trace.detail("Modified roll %d % wind_roll")
        wind_max_roll = 0
        wind_index = 0
        wind_info = self.wind_speed_chart[wind_index]
        while (wind_max_roll < wind_roll):
            trace.flow("Skip wind info, max roll %d" % wind_max_roll)
            wind_info = self.wind_speed_chart[wind_index]
            wind_max_roll = wind_info[0]
            wind_index += 1

        speed = wind_info[wind_type]
        trace.detail ("Wind speed %d mph" % speed)
        return speed

    def beaufort_info(self, wind_speed):
        """
        Returns information from the Beaufort scale for a given wind speed.
        :param wind_speed: The wind speed in miles per hour.
        :return: Tuple of the Beaufort force number, the Beaufort description, and land conditions.
        """
        trace.flow("Get Beaufort scale information, wind speed %d" % wind_speed)
        wind_max_speed = 0
        wind_force_index = 0
        beaufort_info = self.beaufort_scale_chart[wind_force_index]
        while (wind_max_speed < wind_speed):
            trace.flow("Skip wind force, max speed %d" % wind_max_speed)
            beaufort_info = self.beaufort_scale_chart[wind_force_index]
            wind_max_speed = beaufort_info[1]
            wind_force_index += 1

        trace.detail("Wind force %d, description %r, land conditions %r" %
                     (beaufort_info[0], beaufort_info[2], beaufort_info[3]))
        return (beaufort_info[0], beaufort_info[2], beaufort_info[3])

    def __movement_modifier(self, precipitation_index):
        """
        Returns the modifier to movement based on a specified precipitation event.
        :param precipitation_index: The index to self.precipitation_type_chart for the precipitation event.
        :return: The modifier (positive) to movement.
        """
        precipitation_info = self.precipitation_type_chart[precipitation_index]
        trace.detail("Movement modifier for precipitation index %d is %d" % (
            precipitation_index, precipitation_info[10]
        ))
        return precipitation_info[10]

    def __awareness_modifier(self, precipitation_index):
        """
        Returns the modifier to awareness based on a specified precipitation event.
        :param precipitation_index: The index to self.precipitation_type_chart for the precipitation event.
        :return: The modifier (positive) to awareness.
        """
        precipitation_info = self.precipitation_type_chart[precipitation_index]
        trace.detail("Awareness modifier for precipitation index %d is %d" % (
            precipitation_index, precipitation_info[11]
        ))
        return precipitation_info[11]

    def __tracking_modifier(self, precipitation_index):
        """
        Returns the modifier to tracking based on a specified precipitation event.
        :param precipitation_index: The index to self.precipitation_type_chart for the precipitation event.
        :return: The modifier (positive) to tracking.
        """
        precipitation_info = self.precipitation_type_chart[precipitation_index]
        trace.detail("Tracking modifier for precipitation index %d is %d" % (
            precipitation_index, precipitation_info[12]
        ))
        return precipitation_info[12]

    def __direction_modifier(self, precipitation_index):
        """
        Returns the modifier to direction sense based on a specified precipitation event.
        :param precipitation_index: The index to self.precipitation_type_chart for the precipitation event.
        :return: The modifier (positive) to direction sense.
        """
        precipitation_info = self.precipitation_type_chart[precipitation_index]
        trace.detail("Direction sense modifier for precipitation index %d is %d" % (
            precipitation_index, precipitation_info[13]
        ))
        return precipitation_info[13]

    def get_month_index(self):
        """
        Returns the month index of the current month.
        """
        return self.month_dict[self.month][0]

    def set_date(self, month_name, date):
        """
        Sets the month and date.  Only legal values are allowed.
        :param month_name: The name of the month.
        :param date: The date within the month.
        """
        assert month_name in self.month_dict
        month_details = self.month_dict[month_name]
        assert date <= month_details[1]

        self.month = month_name
        self.date = date
        trace.detail("Set month name to %r, date to %d" % (self.month, self.date))

    def get_days_past_spring_equinox(self):
        """
        Returns the number of days after the spring equinox.
        """
        day_in_year = self.__get_day_in_year(self.month, self.date)
        day_of_spring_equinox = self.__get_day_in_year("Gwaeron", 30)

        trace.detail("Days past spring equinox %d" % (day_in_year - day_of_spring_equinox))
        return (day_in_year - day_of_spring_equinox)

    def __get_day_in_year(self, month, date):
        """
        Returns the value of the specified date in terms of days from the start of the year.
        :param month: The month to check.
        :param date: The date in the month to check.
        """
        trace.detail("Get info for month %r, date %d" % (month, date))
        day_total = 0
        for check_month in self.month_dict:
            if check_month[0] == month:
                break
            day_total += check_month[2]

        trace.detail("Days to current month start %d" % day_total)
        day_total += date

        trace.detail("Days to current date %d" % day_total)
        return day_total

    def increment_date(self):
        """
        Increments the date, including wrapping months if needed.
        """
        trace.detail("Month name was %r, date %d" % (self.month, self.date))
        self.date += 1
        if (self.date > self.month_dict[self.month][1]):
            self.month = self.month_dict[self.month][2]
            self.date = 1
        trace.detail("Month name now %r, date %d" % (self.month, self.date))


        """
        This dict is keyed by month name.  The tuple contains the month index (used for weather calculation); 
        the number of days in the month, and name of the next month.
        """
        self.month_dict = {

            "Yestarë": (1, 1, "Narwain"),
            "Narwain": (1, 30, "Ninui"),
            "Ninui": (2, 30, "Gwaeron"),
            "Gwaeron": (3, 30, "Gwirith"),
            "Gwirith": (4, 30, "Lothron"),
            "Lothron": (5, 30, "Nórui"),
            "Nórui": (6, 31, "Loëndë"),
            "Loëndë": (6, 1, "Cerveth"),
            "Cerveth": (7, 31, "Urui"),
            "Urui": (8, 30, "Ivanneth"),
            "Ivanneth": (9, 30, "Narbeleth"),
            "Narbeleth": (10, 30, "Hithui"),
            "Hithui": (11, 30, "Girithron"),
            "Girithron": (12, 30, "Mettarë"),
            "Mettarë": (12, 1, "Yestarë")
        }