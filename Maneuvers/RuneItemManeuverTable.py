# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from StaticManeuverTable import *

import FrameUtils
import trace_log as trace

from Tkinter import IntVar

DIFFERENT_REALM_TEXT = "Is the realm of the spell different from the character's?"
KNOWS_SPELL_TEXT = "Does the character know what the spell or ability is?"
CAN_CAST_TEXT = "Can the character cast the spell intrinsically?"
LEVEL_TEXT = "Spell level:"

DIFFERENT_REALM_BONUS = -30
KNOWS_SPELL_BONUS = 20
DOES_NOT_KNOW_SPELL_PENALTY = 10
CAN_CAST_BONUS = 30

class RuneItemManeuverTable(StaticManeuverTable):
    maneuver_result_text = {
        BLUNDER: "Whatever spells or abilities are in the item or on the rune paper are activated and directed "
                 "against you.  Any runes on rune paper are gone, and you will never be able to use any of the "
                 "spells or abilities contained in the item",
        ABSOLUTE_FAILURE: "You have developed a mental block on this rune/item and will automatically fail on "
                          "any further attempts to read or use it. "
                          "There is a 50% chance that a spell will be activated.",
        FAILURE: "Currently you have no further ideas on how to read/use this rune/item.  "
                 "After you have gone up a level, you may make another attempt to read/use this rune/item.",
        PARTIAL_SUCCESS: "You learn how many spells and abilities it contains and what they are.  "
                         "However, you cannot yet read/use it, and you may not make another attempt until 1 week has "
                         "passed.",
        NEAR_SUCCESS: "You learn how many spells and abilities it contains and what they are.  "
                      "If you wait 24 hours, you may try again with an extra +10 bonus.",
        SUCCESS: "You learn one of the spells or abilities in an item or on a piece of rune paper, and you "
                 "may use it whenever you hold the item or rune paper (runes are only usable once).",
        ABSOLUTE_SUCCESS: "You learn all of the spells and abilities in an item or on a piece of rune paper, "
                          "and you may used them whenever you hold the item or rune paper (runes are only usable once)."
    }

    def setup_difficulty_frame(self, parent_frame):
        trace.entry()
        FrameUtils.destroy_frame_objects(parent_frame)

        trace.exit()

    def setup_maneuver_table_frames(self, parent_frame):
        """
        Set up the frames specific to the maneuver table.
        """

        def setup_different_realm_frame(parent_frame):
            """
            Create a frame with a Checkbox indicating whether spell realm is different from the character's
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, DIFFERENT_REALM_TEXT, self.different_realm)
            trace.exit()

        def setup_knows_spell_frame(parent_frame):
            """
            Create a frame with a Checkbox indicating whether the character knows the spell.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, KNOWS_SPELL_TEXT, self.knows_spell)
            trace.exit()

        def setup_can_cast_frame(parent_frame):
            """
            Create a frame with a Checkbox indicating whether the character can cast the spell.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(parent_frame, CAN_CAST_TEXT, self.can_cast)
            trace.exit()

        def setup_spell_level_frame(parent_frame):
            """
            Create a frame with an Entry specifying the level of the spell.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(parent_frame, LEVEL_TEXT, self.spell_level)
            trace.exit()

        trace.entry()

        FrameUtils.destroy_frame_objects(parent_frame)
        self.different_realm = IntVar()
        self.knows_spell = IntVar()
        self.can_cast = IntVar()
        self.spell_level = IntVar()
        setup_different_realm_frame(parent_frame)
        setup_knows_spell_frame(parent_frame)
        setup_can_cast_frame(parent_frame)
        setup_spell_level_frame(parent_frame)

        trace.exit()

    def difficulty_bonus(self):
        return (0)

    def table_bonus(self):
        """
        Determine any additional bonuses to apply to a maneuver based on factors
        specific to this maneuver type.
        :return: The additional maneuver bonus
        """
        trace.entry()

        bonus = 0
        if self.different_realm.get() == 1:
            trace.flow("Different realm: -30")
            bonus += DIFFERENT_REALM_BONUS

        if self.knows_spell.get() == 1:
            trace.flow("Character knows spell/ability: +20")
            bonus += KNOWS_SPELL_BONUS
        else:
            trace.flow("Character does not know spell/ability: -10")
            bonus -= DOES_NOT_KNOW_SPELL_PENALTY

        if self.can_cast.get() == 1:
            trace.flow("Character can cast spell: +30")
            bonus += CAN_CAST_BONUS

        level = self.spell_level.get()
        trace.detail("Spell level %d" % level)
        bonus -= level

        trace.detail("Bonus %d" % bonus)

        trace.exit()
        return bonus