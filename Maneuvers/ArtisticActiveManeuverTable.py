# -*- coding: utf-8 -*-
import sys

from StaticManeuverTable import *

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

sys.path.append('../')

PRACTISED_TEXT = "Add IG bonus if piece practised: "
IMPROVISATION_TEXT = "Is this improvised?"
PARTNER_TEXT = "Is this with a partner?"
LORE_TEXT = "At least 7 ranks in related Lore?"

PRACTISED_BONUS = 5
IMPROVISATION_PENALTY = 20
PARTNER_PENALTY = 10
LORE_BONUS = 10

class ArtisticActiveManeuverTable(StaticManeuverTable):
    MANEUVER_ACTING = "Acting"
    MANEUVER_DANCING = "Dancing"
    MANEUVER_MIMERY = "Mimery"
    MANEUVER_MIMICRY = "Mimicry"
    MANEUVER_PLAY_INSTRUMENT = "Play instrument"
    MANEUVER_POETIC_IMPROVISATION = "Poetic Improvisation"
    MANEUVER_SINGING = "Singing"
    MANEUVER_TALE_TELLING = "Tale Telling"
    MANEUVER_VENTRILOQUISM = "Ventriloquism"

    maneuver_type_options = (
        MANEUVER_ACTING, MANEUVER_DANCING, MANEUVER_MIMERY, MANEUVER_MIMICRY, MANEUVER_PLAY_INSTRUMENT,
        MANEUVER_POETIC_IMPROVISATION, MANEUVER_SINGING, MANEUVER_TALE_TELLING, MANEUVER_VENTRILOQUISM
    )

    maneuver_result_text = {
        BLUNDER: "Horror!  Your mind has gone blank, and the rest of your performance went with it! "
                 "You are so rattled that you attempt to improvise and fail miserably, offending your patrons in what "
                 "is most certainly the worst performance of your career.  "
                 "Your reputation suffers commensurately, and you operate at a -20 modification (non-cumulative) to "
                 "future attempts at this skill until you achieve a result of Absolute Success in a future attempt.",
        ABSOLUTE_FAILURE: "Your mind is out of sync with your body, and you somehow manage to fall all over yourself "
                          "during a critical moment.  Your audience laughs derisively and turns its attention "
                          "elsewhere.  "
                          "Maybe you should join the circus.  You abort the rest of your performance.",
        FAILURE: "Yeech.  A lacklustre performance leaves your audience yawning.  "
                 "The snores drown out the feeble applause.",
        PARTIAL_SUCCESS: "Not bad.  Not good, but not bad.  You hold the attention of the audience, but a few key "
                         "blunders spoil an otherwise satisfactory performance.",
        NEAR_SUCCESS: "You near the completion of the act.  Fine tuning is all that you lack. "
                      "Roll again with a +10 modification to bring it home.",
        SUCCESS: "Bravo!  Your performance is a success, and the enthusiastic response of your audience warms your "
                 "old performer's heart.",
        ABSOLUTE_SUCCESS: "You have surpassed yourself, and your audience mobs you for autographs, bits of string "
                          "from your outfit, and kisses.  What will you do for an encore?"
    }

    maneuver_result_stats = {
        BLUNDER: (-50, 1.3, -20),
        ABSOLUTE_FAILURE: (0, 0.6, -10),
        FAILURE: (10, 1, 0),
        PARTIAL_SUCCESS: (80, 1, 5),
        NEAR_SUCCESS: (80, 80, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 1, 30)
    }

    @staticmethod
    def select_artistic_active_table(maneuver_type):
        """
        Set the current artistic/active maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        from Maneuvers.ArtisticActive.ActingManeuverTable import ActingManeuverTable
        from Maneuvers.ArtisticActive.MimeryManeuverTable import MimeryManeuverTable
        from Maneuvers.ArtisticActive.MimicryManeuverTable import MimicryManeuverTable
        from Maneuvers.ArtisticActive.PoeticImprovisationManeuverTable import PoeticImprovisationManeuverTable
        from Maneuvers.ArtisticActive.SingingManeuverTable import SingingManeuverTable
        from Maneuvers.ArtisticActive.TaleTellingManeuverTable import TaleTellingManeuverTable
        from Maneuvers.ArtisticActive.VentriloquismManeuverTable import VentriloquismManeuverTable

        if maneuver_type == ArtisticActiveManeuverTable.MANEUVER_ACTING:
            trace.flow("Acting maneuver")
            trace.exit()
            return ActingManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_DANCING:
            trace.flow("Dancing maneuver")
            trace.exit()
            return ArtisticActiveManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_MIMERY:
            trace.flow("Acting maneuver")
            trace.exit()
            return MimeryManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_MIMICRY:
            trace.flow("Acting maneuver")
            trace.exit()
            return MimicryManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_PLAY_INSTRUMENT:
            trace.flow("Acting maneuver")
            trace.exit()
            return ArtisticActiveManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_POETIC_IMPROVISATION:
            trace.flow("Acting maneuver")
            trace.exit()
            return PoeticImprovisationManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_SINGING:
            trace.flow("Acting maneuver")
            trace.exit()
            return SingingManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_TALE_TELLING:
            trace.flow("Acting maneuver")
            trace.exit()
            return TaleTellingManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_VENTRILOQUISM:
            trace.flow("Acting maneuver")
            trace.exit()
            return VentriloquismManeuverTable()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_practised_frame():
            """
            Create a frame with a Checkbox indicating whether the piece is practised.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, PRACTISED_TEXT, self.practised_bonus)
            trace.exit()

        def setup_improvised_frame():
            """
            Create a frame with a Checkbox indicating whether the piece is improvised.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, IMPROVISATION_TEXT, self.is_improvised)
            trace.exit()

        def setup_partner_frame():
            """
            Create a frame with a Checkbox indicating whether the performance is with a partner.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, PARTNER_TEXT, self.with_partner)
            trace.exit()

        def setup_lore_frame():
            """
            Create a frame with a Checkbox indicating whether the performance is with a partner.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, LORE_TEXT, self.lore_skill)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.practised_bonus = IntVar()
        self.practised_bonus.set(0)
        self.is_improvised = IntVar()
        self.with_partner = IntVar()
        self.lore_skill = IntVar()
        setup_practised_frame()
        setup_improvised_frame()
        setup_partner_frame()
        setup_lore_frame()

        trace.exit()

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        trace.detail("Practised bonus: %d" % self.practised_bonus.get())
        bonus += self.practised_bonus.get()
        if self.is_improvised.get() == 1:
            trace.flow("Improvised: -20")
            bonus -= IMPROVISATION_PENALTY

        if self.with_partner.get() == 1:
            trace.flow("With partner: -10")
            bonus -= PARTNER_PENALTY

        if self.lore_skill.get() == 1:
            trace.flow("Lore skill: +10")
            bonus += LORE_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
