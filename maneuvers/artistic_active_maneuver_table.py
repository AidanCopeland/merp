# -*- coding: utf-8 -*-
"""
The Artistic/Active static maneuver table.

Classes:
    ArtisticActiveManeuverTable
"""
from __future__ import absolute_import
import sys
from tkinter import IntVar

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from console.character.secondary_skills import SKILL_ACTING, SKILL_DANCING, SKILL_MIMERY, \
    SKILL_MIMICRY, SKILL_PLAY_INSTRUMENT, SKILL_POETIC_IMPROVISATION, SKILL_SINGING, \
    SKILL_TALE_TELLING, SKILL_VENTRILOQUISM

import frame_utils
import trace_log as trace

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
    """
    Static maneuver table for Artistic/Active maneuvers.

    Methods:
        select_artistic_active_table(maneuver_type)
        setup_maneuver_table_frames(self, parent_frame)
        table_bonus(self)
    """
    MANEUVER_ACTING = "Acting"
    MANEUVER_DANCING = "Dancing"
    MANEUVER_MIMERY = "Mimery"
    MANEUVER_MIMICRY = "Mimicry"
    MANEUVER_PLAY_INSTRUMENT = "Play instrument"
    MANEUVER_POETIC_IMPROVISATION = "Poetic Improvisation"
    MANEUVER_SINGING = "Singing"
    MANEUVER_TALE_TELLING = "Story/Tale Telling"
    MANEUVER_VENTRILOQUISM = "Ventriloquism"

    maneuver_type_options = (
        MANEUVER_ACTING, MANEUVER_DANCING, MANEUVER_MIMERY, MANEUVER_MIMICRY,
        MANEUVER_PLAY_INSTRUMENT, MANEUVER_POETIC_IMPROVISATION, MANEUVER_SINGING,
        MANEUVER_TALE_TELLING, MANEUVER_VENTRILOQUISM
    )

    maneuver_result_text = {
        BLUNDER:
            "Horror!  Your mind has gone blank, and the rest of your performance went with it! "
            "You are so rattled that you attempt to improvise and fail miserably, offending your "
            "patrons in what is most certainly the worst performance of your career.  "
            "Your reputation suffers commensurately, and you operate at a -20 modification "
            "(non-cumulative) to future attempts at this skill until you achieve a result of "
            "Absolute Success in a future attempt.",
        ABSOLUTE_FAILURE:
            "Your mind is out of sync with your body, and you somehow manage to fall all over "
            "yourself during a critical moment. Your audience laughs derisively and turns its "
            "attention elsewhere.  "
            "Maybe you should join the circus.  You abort the rest of your performance.",
        FAILURE:
            "Yeech.  A lacklustre performance leaves your audience yawning.  "
            "The snores drown out the feeble applause.",
        PARTIAL_SUCCESS:
            "Not bad.  Not good, but not bad.  You hold the attention of the audience, but a few "
            "key blunders spoil an otherwise satisfactory performance.",
        NEAR_SUCCESS:
            "You near the completion of the act.  Fine tuning is all that you lack. "
            "Roll again with a +10 modification to bring it home.",
        SUCCESS:
            "Bravo!  Your performance is a success, and the enthusiastic response of your audience "
            "warms your old performer's heart.",
        ABSOLUTE_SUCCESS:
            "You have surpassed yourself, and your audience mobs you for autographs, bits of "
            "string from your outfit, and kisses.  What will you do for an encore?"
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

    def __init__(self, **kwargs):
        trace.entry()
        super().__init__(**kwargs)
        self.practised_bonus = IntVar()
        self.is_improvised = IntVar()
        self.with_partner = IntVar()
        self.lore_skill = IntVar()

        trace.exit()

    @staticmethod
    def select_artistic_active_table(maneuver_type):
        """
        Set the current artistic/active maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=too-many-return-statements
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.artistic_active.acting_maneuver_table import ActingManeuverTable
        from maneuvers.artistic_active.mimery_maneuver_table import MimeryManeuverTable
        from maneuvers.artistic_active.mimicry_maneuver_table import MimicryManeuverTable
        from maneuvers.artistic_active.poetic_improvisation_maneuver_table import \
            PoeticImprovisationManeuverTable
        from maneuvers.artistic_active.singing_maneuver_table import SingingManeuverTable
        from maneuvers.artistic_active.tale_telling_maneuver_table import TaleTellingManeuverTable
        from maneuvers.artistic_active.ventriloquism_maneuver_table import \
            VentriloquismManeuverTable

        if maneuver_type == ArtisticActiveManeuverTable.MANEUVER_ACTING:
            trace.flow("Acting maneuver")
            trace.exit()
            return ActingManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_DANCING:
            trace.flow("Dancing maneuver")
            trace.exit()
            return ArtisticActiveManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_MIMERY:
            trace.flow("Mimery maneuver")
            trace.exit()
            return MimeryManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_MIMICRY:
            trace.flow("Mimicry maneuver")
            trace.exit()
            return MimicryManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_PLAY_INSTRUMENT:
            trace.flow("Play Instrument maneuver")
            trace.exit()
            return ArtisticActiveManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_POETIC_IMPROVISATION:
            trace.flow("Poetic Improvisation maneuver")
            trace.exit()
            return PoeticImprovisationManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_SINGING:
            trace.flow("Singing maneuver")
            trace.exit()
            return SingingManeuverTable()

        elif maneuver_type == ArtisticActiveManeuverTable.MANEUVER_TALE_TELLING:
            trace.flow("Tale Telling maneuver")
            trace.exit()
            return TaleTellingManeuverTable()

        else:
            trace.flow("Ventriloquism maneuver")
            assert maneuver_type == ArtisticActiveManeuverTable.MANEUVER_VENTRILOQUISM
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
            frame_utils.setup_entry_frame(parent_frame, PRACTISED_TEXT, self.practised_bonus)
            trace.exit()

        def setup_improvised_frame():
            """
            Create a frame with a Checkbox indicating whether the piece is improvised.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, IMPROVISATION_TEXT, self.is_improvised)
            trace.exit()

        def setup_partner_frame():
            """
            Create a frame with a Checkbox indicating whether the performance is with a partner.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, PARTNER_TEXT, self.with_partner)
            trace.exit()

        def setup_lore_frame():
            """
            Create a frame with a Checkbox indicating whether the performance is with a partner.
            """
            trace.entry()
            frame_utils.setup_checkbox_frame(parent_frame, LORE_TEXT, self.lore_skill)
            trace.exit()

        trace.entry()

        frame_utils.destroy_frame_objects(parent_frame)
        self.practised_bonus.set(0)
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
            trace.flow("lore skill: +10")
            bonus += LORE_BONUS

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus

    @staticmethod
    def get_maneuver_preferred_skills(maneuver_type):
        """
        Return a list of skills that are the preferred skills to use for this maneuver.
        :param maneuver_type: The type of maneuver selected.
        """
        maneuver_to_skills = {
            ArtisticActiveManeuverTable.MANEUVER_ACTING: [SKILL_ACTING, ],
            ArtisticActiveManeuverTable.MANEUVER_DANCING: [SKILL_DANCING, ],
            ArtisticActiveManeuverTable.MANEUVER_MIMERY: [SKILL_MIMERY, ],
            ArtisticActiveManeuverTable.MANEUVER_MIMICRY: [SKILL_MIMICRY, ],
            ArtisticActiveManeuverTable.MANEUVER_PLAY_INSTRUMENT: [SKILL_PLAY_INSTRUMENT, ],
            ArtisticActiveManeuverTable.MANEUVER_POETIC_IMPROVISATION:
                [SKILL_POETIC_IMPROVISATION, ],
            ArtisticActiveManeuverTable.MANEUVER_SINGING: [SKILL_SINGING, ],
            ArtisticActiveManeuverTable.MANEUVER_TALE_TELLING: [SKILL_TALE_TELLING, ],
            ArtisticActiveManeuverTable.MANEUVER_VENTRILOQUISM: [SKILL_VENTRILOQUISM, ]
        }

        skills_list = maneuver_to_skills.get(maneuver_type, [])
        trace.detail("Maneuver type %s, skills list %r" % (maneuver_type, skills_list))
        return skills_list
