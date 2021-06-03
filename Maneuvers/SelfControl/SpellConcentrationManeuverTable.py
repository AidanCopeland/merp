# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

from Maneuvers.SelfControlManeuverTable import \
    SelfControlManeuverTable, BLUNDER, ABSOLUTE_FAILURE, FAILURE, \
    PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
from Tkinter import IntVar, StringVar

import FrameUtils
import trace_log as trace

MEDITATIVE_TRANCE_TEXT = "In a meditative trance?"
MEDITATIVE_TRANCE_BONUS = 20

ACTIVITY_TEXT = "Activity above 50% devoted to concentration"

SURROUNDINGS_TEXT = "Modifier dependent on surroundings (+20 to -30)"

INTERRUPTION_TEXT = "Number of ""interruptions"" successfully ignored"
INTERRUPTION_BONUS = -5

STARTLED_TEXT = "Startled?"
STARTLED_BONUS = -20

STRUCK_PROMPT = "Physically struck?"
STRUCK_NOT_STRUCK_TEXT = "Not struck, or undamaged"
STRUCK_CONCUSSION_HITS_TEXT = "Struck for concussion hits only"
STRUCK_A_CRIT_TEXT = "Received A critical"
STRUCK_B_CRIT_TEXT = "Received B critical"
STRUCK_C_CRIT_TEXT = "Received C critical"
STRUCK_D_CRIT_TEXT = "Received D critical"
STRUCK_E_CRIT_TEXT = "Received E critical (or higher)"
STRUCK_NOT_STRUCK_BONUS = 0
STRUCK_CONCUSSION_HITS_BONUS = -20
STRUCK_A_CRIT_BONUS = -30
STRUCK_B_CRIT_BONUS = -40
STRUCK_C_CRIT_BONUS = -50
STRUCK_D_CRIT_BONUS = -60
STRUCK_E_CRIT_BONUS = -70
STRUCK_OPTIONS = (
    STRUCK_NOT_STRUCK_TEXT, STRUCK_CONCUSSION_HITS_TEXT, STRUCK_A_CRIT_TEXT,
    STRUCK_B_CRIT_TEXT, STRUCK_C_CRIT_TEXT, STRUCK_D_CRIT_TEXT,
    STRUCK_E_CRIT_TEXT
)


class SpellConcentrationManeuverTable(SelfControlManeuverTable):

    maneuver_result_text = {
        BLUNDER:
            "A sudden splitting headache breaks your concentration on the spell. All "
            "Spell Concentration maneuvers within the next ten minutes will be at -50. "
            "Warriors have it easy ...",
        ABSOLUTE_FAILURE:
            "You lose concentration on your spell as a wave of mental weariness "
            "overcomes you. Your next Spell Concentration maneuver, if within the next "
            "ten minutes, will be at -20. Take a break ....",
        FAILURE:
            "You should have paid more attention to those mental exercises during your "
            "apprenticeship. Too bad, you are distracted and lose concentration on your "
            "spell.",
        PARTIAL_SUCCESS:
            "Your control over the magical energies is slipping. If you do nothing this "
            "round other than attempt to maintain concentration, roll again on this "
            "table, otherwise you lose concentration.",
        NEAR_SUCCESS:
            "Your control over the magical energies is fragile. Focus your attention on "
            "the task at hand. Roll again on this table with a special bonus of +10.",
        SUCCESS:
            "Your mind is easily up to the strain of maintaining concentration on this "
            "spell.",
        ABSOLUTE_SUCCESS:
            "The long hours of mental exercises serve you in good stead as you retain "
            "concentration on your spell. Add +20 to your next Spell Concentration "
            "maneuver with this spell (non-cumulative)."
    }

    maneuver_result_stats = {
        BLUNDER: (0, 1, -20),
        ABSOLUTE_FAILURE: (0, 1, -25),
        FAILURE: (0, 1, -5),
        PARTIAL_SUCCESS: (100, 1, 0),
        NEAR_SUCCESS: (100, 1, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (100, 1, 30)
    }

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_skill_frames(self, parent_frame):
        """
        Set up the frames specific to the skill.
        """

        def setup_activity_frame():
            """
            Create a frame with an Entry indicating the amount of additional activity
            devoted to concentration.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, ACTIVITY_TEXT, self.additional_activity)
            trace.exit()

        def setup_meditative_trance_frame():
            """
            Create a frame with a Checkbox indicating whether the caster is in a meditative trance.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, MEDITATIVE_TRANCE_TEXT, self.meditative_trance)
            trace.exit()

        def setup_surroundings_frame():
            """
            Create a frame with an Entry indicating the bonus or penalty dependent on
            the surroundings.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, SURROUNDINGS_TEXT, self.surroundings)
            trace.exit()

        def setup_interruptions_frame():
            """
            Create a frame with an Entry indicating the number of interruptions successfully
            ignored.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, INTERRUPTION_TEXT, self.num_interruptions)
            trace.exit()

        def setup_startled_frame():
            """
            Create a frame with a Checkbox indicating whether the caster has been startled.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, STARTLED_TEXT, self.startled)
            trace.exit()

        def setup_physical_strike_frame():
            """
            Create a frame with an OptionMenu indicating any physical strike that the
            caster has received.
            """
            trace.entry()
            FrameUtils.setup_optionmenu_frame(
                parent_frame,
                STRUCK_PROMPT,
                STRUCK_NOT_STRUCK_TEXT,
                self.physical_strike,
                *STRUCK_OPTIONS)

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.additional_activity = IntVar()
        self.additional_activity.set(0)
        self.meditative_trance = IntVar()
        self.meditative_trance.set(0)
        self.surroundings = IntVar()
        self.surroundings.set(0)
        self.num_interruptions = IntVar()
        self.num_interruptions.set(0)
        self.startled = IntVar()
        self.startled.set(0)
        self.physical_strike = StringVar()

        setup_activity_frame()
        setup_meditative_trance_frame()
        setup_surroundings_frame()
        setup_interruptions_frame()
        setup_startled_frame()
        setup_physical_strike_frame()

        trace.exit()

    def skill_type_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this skill type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0

        bonus += self.activity_bonus()
        bonus += self.trance_bonus()
        bonus += self.surroundings_bonus()
        bonus += self.interruptions_bonus()
        bonus += self.startled_bonus()
        bonus += self.physical_strike_bonus()

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus

    def activity_bonus(self):
        """
        Determine any additional bonus to apply to this maneuver based on additional
        activity the caster is devoting to concentration.
        :return: The additional maneuver bonus
        """
        trace.entry()

        additional_activity = min(max(0, self.additional_activity.get()), 50)
        trace.detail("Additional activity: %d%%" % additional_activity)
        bonus = additional_activity

        trace.exit()
        return bonus

    def trance_bonus(self):
        """
        Determine any additional bonus to apply to this maneuver based on whether the
        caster is in a meditative trance.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.meditative_trance.get() == 1:
            trace.flow("In meditative trance: +20")
            bonus += MEDITATIVE_TRANCE_BONUS

        trace.exit()
        return bonus

    def surroundings_bonus(self):
        """
        Determine any additional bonus or penalty to apply to this maneuver based on the
        caster's surroundings.
        :return: The additional maneuver bonus or penalty.
        """
        trace.entry()

        surroundings_bonus = min(max(-30, self.surroundings.get()), 20)
        trace.detail("Surroundings bonus: %d" % surroundings_bonus)

        bonus = surroundings_bonus

        trace.exit()
        return bonus

    def interruptions_bonus(self):
        """
        Determine any additional penalty to apply to this maneuver based on whether the
        caster has already successfully ignored interruptions.
        :return: The additional maneuver penalty (as a negative bonus).
        """
        trace.entry()

        num_interruptions = max(0, self.num_interruptions.get())
        trace.detail("Ignored %d interruptions" % num_interruptions)

        bonus = INTERRUPTION_BONUS * num_interruptions
        trace.detail("Interruptions bonus: %d" % bonus)

        trace.exit()
        return bonus

    def startled_bonus(self):
        """
        Determine any additional penalty to apply to this maneuver based on whether the
        caster has been startled.
        :return: The additional maneuver penalty (as a negative bonus).
        """
        trace.entry()

        bonus = 0

        if self.startled.get() == 1:
            trace.flow("Startled: -20")
            bonus += STARTLED_BONUS

        trace.exit()
        return bonus

    def physical_strike_bonus(self):
        """
        Determine any additional penalty to apply to this maneuver based on whether the
        caster has been physically struck.
        :return: The additional maneuver penalty (as a negative bonus).
        """
        trace.entry()

        bonus = 0

        physical_strike = self.physical_strike.get()
        if physical_strike == STRUCK_NOT_STRUCK_TEXT:
            trace.flow("Not struck")
        elif physical_strike == STRUCK_CONCUSSION_HITS_TEXT:
            trace.flow("Concussion hits: -20")
            bonus += STRUCK_CONCUSSION_HITS_BONUS
        elif physical_strike == STRUCK_A_CRIT_TEXT:
            trace.flow("A critical: -30")
            bonus += STRUCK_A_CRIT_BONUS
        elif physical_strike == STRUCK_B_CRIT_TEXT:
            trace.flow("B critical: -40")
            bonus += STRUCK_B_CRIT_BONUS
        elif physical_strike == STRUCK_C_CRIT_TEXT:
            trace.flow("C critical: -50")
            bonus += STRUCK_C_CRIT_BONUS
        elif physical_strike == STRUCK_D_CRIT_TEXT:
            trace.flow("D critical: -60")
            bonus += STRUCK_D_CRIT_BONUS
        else:
            trace.flow("E critical: -70")
            bonus += STRUCK_E_CRIT_BONUS

        trace.exit()
        return bonus


