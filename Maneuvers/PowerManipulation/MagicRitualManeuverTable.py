# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

from Maneuvers.PowerManipulationManeuverTable import \
    PowerManipulationManeuverTable, BLUNDER, ABSOLUTE_FAILURE, FAILURE, \
    PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS

from ttk import Frame, Label, OptionMenu

import FrameUtils
import trace_log as trace

from Tkinter import LEFT, RIGHT, BOTH, RAISED, IntVar, StringVar

TIME_PROMPT = "Duration of effect (no more than): "

ONE_ROUND = "1 round"
TWO_ROUNDS = "2 rounds"
THREE_ROUNDS = "3 rounds"
FOUR_ROUNDS = "4 rounds"
ONE_MINUTE = "1 minute"
FIVE_MINUTES = "5 minutes"
FIFTEEN_MINUTES = "15 minutes"
THIRTY_MINUTES = "30 minutes"
ONE_HOUR = "1 hour"

TIME_DEFAULT = FOUR_ROUNDS

time_options = (
    ONE_ROUND, TWO_ROUNDS, THREE_ROUNDS, FOUR_ROUNDS, ONE_MINUTE, FIVE_MINUTES,
    FIFTEEN_MINUTES, THIRTY_MINUTES, ONE_HOUR
)

maneuver_difficulty_bonuses = {
    ONE_ROUND: 30,
    TWO_ROUNDS: 20,
    THREE_ROUNDS: 10,
    FOUR_ROUNDS: 0,
    ONE_MINUTE: -10,
    FIVE_MINUTES: -20,
    FIFTEEN_MINUTES: -30,
    THIRTY_MINUTES: -50,
    ONE_HOUR: -70
}

TAKING_TIME_TEXT = "Additional bonus/penalty: time taken on ritual"
CASTER_TYPE_PROMPT = "Type of ritualist"
CASTER_PURE_HYBRID_TEXT = "Pure or hybrid caster"
CASTER_SEMI_SPELL_TEXT = "Semi-spell user"
CASTER_NON_SPELL_TEXT = "Non-spell user"
caster_type_options = {
    CASTER_PURE_HYBRID_TEXT, CASTER_SEMI_SPELL_TEXT, CASTER_NON_SPELL_TEXT
}

CASTER_PURE_HYBRID_BONUS = 5
CASTER_SEMI_SPELL_BONUS = -10
CASTER_NON_SPELL_BONUS = -25


def caster_type_bonus(caster_type):
    """
    Determine the bonus to the maneuver based on the caster type of the ritualist.
    :param caster_type: The caster type of the ritualist.
    :return: The bonus to the maneuver.
    """
    if caster_type == CASTER_PURE_HYBRID_TEXT:
        trace.flow("Pure/hybrid caster: +5")
        return CASTER_PURE_HYBRID_BONUS
    elif caster_type == CASTER_SEMI_SPELL_TEXT:
        trace.flow("Semi-spell user: -10")
        return CASTER_SEMI_SPELL_BONUS
    else:
        trace.flow("Non-spell user: -25")
        return CASTER_NON_SPELL_BONUS


class MagicRitualManeuverTable(PowerManipulationManeuverTable):

    maneuver_result_text = {
        BLUNDER:
            "All participants in the ritual lose their minds, their bodies are drooling "
            "vegetables (all mental stats are reduced to 1).",
        ABSOLUTE_FAILURE:
            "Total failure.  All participants suffer a decrease of one mental stat to "
            "1 for 1 month.",
        FAILURE:
            "All magic is sucked out of the participants (no PPs are available to the "
            "casters for 1 week per level of the ritual).  All participants suffer a "
            "d10 decrease to one mental stat for 1 month.",
        PARTIAL_SUCCESS:
            "All participants lose PPs for one hour per level of the ritual. The ritual "
            "can be tried again after a rest.",
        NEAR_SUCCESS:
            "A very near success. The PPs committed are lost but the ritualist can start "
            "from the beginning.",
        SUCCESS:
            "The ritual works: However everyone is exhausted and needs a full sleep "
            "period to recover.",
        ABSOLUTE_SUCCESS:
            "The ritual works as planned and the ritualist gains an extra +5 to any "
            "future attempts to cast this ritual as he realizes what has just happened."
    }

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_difficulty_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

        maneuver_difficulty_prompt = Label(maneuver_difficulty_frame, text=TIME_PROMPT)
        maneuver_difficulty_prompt.pack(side=LEFT)

        self.maneuver_difficulty_options = time_options

        self.maneuver_difficulty_selector = \
            OptionMenu(
                maneuver_difficulty_frame,
                self.maneuver_difficulty,
                FOUR_ROUNDS,
                *self.maneuver_difficulty_options)
        self.maneuver_difficulty_selector.pack(side=RIGHT)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_caster_type_frame():
            """
            Create a frame with an OptionMenu indicating the caster type of the
            ritualist.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame, CASTER_TYPE_PROMPT, CASTER_PURE_HYBRID_TEXT, self.caster_type, *caster_type_options)

            trace.exit()

        def setup_gm_bonus_frame():
            """
            Create a frame with an Entry indicating additional bonus given by the GM.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, TAKING_TIME_TEXT, self.gm_bonus)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.caster_type = StringVar()
        self.gm_bonus = IntVar()
        setup_caster_type_frame()
        setup_gm_bonus_frame()
        self.gm_bonus.set(0)

        trace.exit()

    def difficulty_bonus(self):
        """
        Determine the difficulty to apply to a maneuver based on its difficulty.
        :return: The maneuver difficulty bonus
        """
        trace.entry()

        bonus = maneuver_difficulty_bonuses[self.maneuver_difficulty.get()]
        trace.detail("Returning %d" % bonus)

        trace.exit()
        return bonus

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += caster_type_bonus(self.caster_type.get())
        bonus += self.gm_bonus.get()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus
