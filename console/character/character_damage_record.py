#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the CharacterDamageRecord used to view and update character damage information.

Classes:
    DamageRecordSheet
"""
import sys
from tkinter import Tk, BOTH, RAISED, LEFT, StringVar, FLAT, IntVar
from tkinter.ttk import Frame, Label, Style

from future import standard_library

import frame_utils
import trace_log as trace
from console.character.total_damage import ACTIVE, OUT_OF_COMBAT, DYING, UNCONSCIOUS, DEAD
from verify_utils import verify_int_value, verify_int_value_or_empty

standard_library.install_aliases()

sys.path.append('../../')

COMBAT_READINESS_OPTIONS = (ACTIVE, OUT_OF_COMBAT, DYING, UNCONSCIOUS, DEAD)
HITS_TAKEN_LABEL = "Hits taken:"
TOTAL_HITS_LABEL = "Total hits:"
HITS_PER_ROUND_LABEL = "Hits per round:"
ROUNDS_STUNNED_LABEL = "Rounds stunned:"
ROUNDS_STUNNED_NO_PARRY_LABEL = "Rounds stunned (no parry):"
SUBTRACTION_FROM_BONUSES_LABEL = "Subtraction from bonuses:"
ROUNDS_TO_DEATH_LABEL = "Rounds to death:"
COMBAT_READINESS_LABEL = "Combat readiness:"
WOUNDS_LABEL = "Wounds:"


class CharacterDamageRecord(Frame):
    """
    The console allowing viewing and updating of a single character information.

    Methods:
        __init__(self, master, parent_console, character_database)
        populate_damage_record_sheet(self)
        characters_updated(self)
    """
    def __init__(self, master, parent_console, character_database, character_index):
        trace.entry()

        Frame.__init__(self, master)
        self.character = character_database.get_character(character_index)
        self.total_damage = self.character.total_damage
        self.parent_console = parent_console
        self.master = master

        self.style = None
        self.columns_frame = Frame()
        self.combat_readiness_frame = Frame()
        self.wounds_frame = Frame()

        self.hits_taken = StringVar()
        self.hits_taken_delta = StringVar()
        self.total_hits = StringVar()
        self.total_hits_delta = StringVar()
        self.bleeding = StringVar()
        self.bleeding_delta = StringVar()
        self.stun = StringVar()
        self.stun_delta = StringVar()
        self.stun_no_parry = StringVar()
        self.stun_no_parry_delta = StringVar()
        self.subtraction_from_bonuses = StringVar()
        self.subtraction_from_bonuses_delta = StringVar()
        self.rounds_to_death = StringVar()
        self.rounds_to_death_delta = StringVar()
        self.combat_readiness = StringVar()
        self.wounds = []

        self._initialize_variables()
        self._init_ui()
        self._init_ui_hits_taken()
        self._init_ui_total_hits()
        self._init_ui_bleeding()
        self._init_ui_stun()
        self._init_ui_stun_no_parry()
        self._init_ui_subtraction_from_bonuses()
        self._init_ui_rounds_to_death()
        #self._init_ui_combat_readiness()
        #self._init_ui_wounds()

        frame_utils.init_ui_go_button(
            self, 'Apply updates', self._apply_updates)
        self._populate_damage_record_sheet()

        self._display_frames()

        trace.exit()

    def _initialize_variables(self):
        trace.entry()
        self.style = Style()
        self.style.theme_use("default")

        trace.exit()

    def _init_ui(self):
        """
        Initializes the components of the CharacterDamageRecord window.
        """
        trace.entry()

        def init_ui_title(this):
            trace.entry()
            title_frame = Frame(this, relief=RAISED, borderwidth=1)
            title_frame.pack(fill=BOTH, expand=True)
            title_label = Label(title_frame, text="%s: Damage Record Sheet" % this.character.name)
            title_label.pack()
            trace.exit()

        def init_ui_columns(this):
            trace.entry()
            this.columns_frame = Frame(this, relief=RAISED, borderwidth=1)
            this.columns_frame.columnconfigure(0, weight=2)
            this.columns_frame.columnconfigure(1, weight=1)
            this.columns_frame.columnconfigure(2, weight=1)
            value_label = Label(this.columns_frame, text="Current/desired value")
            value_label.grid(row=0, column=1)
            delta_label = Label(this.columns_frame, text="Delta to apply")
            delta_label.grid(row=0, column=2)
            this.columns_frame.pack()
            trace.exit()

        init_ui_title(self)
        init_ui_columns(self)

        trace.exit()

    def _init_ui_hits_taken(self):
        trace.entry()
        frame_utils.setup_grid_double_entry(
            self.columns_frame,
            HITS_TAKEN_LABEL,
            self.hits_taken,
            self.hits_taken_delta,
            1
        )

    def _init_ui_total_hits(self):
        trace.entry()
        frame_utils.setup_grid_double_entry(
            self.columns_frame,
            TOTAL_HITS_LABEL,
            self.total_hits,
            self.total_hits_delta,
            2
        )

    def _init_ui_bleeding(self):
        trace.entry()
        frame_utils.setup_grid_double_entry(
            self.columns_frame,
            HITS_PER_ROUND_LABEL,
            self.bleeding,
            self.bleeding_delta,
            3
        )

    def _init_ui_stun(self):
        trace.entry()
        frame_utils.setup_grid_double_entry(
            self.columns_frame,
            ROUNDS_STUNNED_LABEL,
            self.stun,
            self.stun_delta,
            4
        )

    def _init_ui_stun_no_parry(self):
        trace.entry()
        frame_utils.setup_grid_double_entry(
            self.columns_frame,
            ROUNDS_STUNNED_NO_PARRY_LABEL,
            self.stun_no_parry,
            self.stun_no_parry_delta,
            5
        )

    def _init_ui_subtraction_from_bonuses(self):
        trace.entry()
        frame_utils.setup_grid_double_entry(
            self.columns_frame,
            SUBTRACTION_FROM_BONUSES_LABEL,
            self.subtraction_from_bonuses,
            self.subtraction_from_bonuses_delta,
            6
        )

    def _init_ui_rounds_to_death(self):
        trace.entry()
        frame_utils.setup_grid_double_entry(
            self.columns_frame,
            ROUNDS_TO_DEATH_LABEL,
            self.rounds_to_death,
            self.rounds_to_death_delta,
            7
        )

    def _init_ui_combat_readiness(self):
        trace.entry()
        self.combat_readiness_frame = Frame(self, relief=FLAT, borderwidth=1)
        self.combat_readiness_frame.pack(fill=BOTH, expand=True)
        frame_utils.setup_optionmenu_frame(
            self.combat_readiness_frame,
            COMBAT_READINESS_LABEL,
            self.combat_readiness.get(),
            self.combat_readiness,
            *COMBAT_READINESS_OPTIONS)

    def _init_ui_wounds(self):
        trace.entry()
        self.wounds_frame = Frame(self, relief=FLAT, borderwidth=1)
        self.wounds_frame.pack(fill=BOTH, expand=True)

        wounds_label = Label(self.wounds_frame, text=WOUNDS_LABEL)
        wounds_label.pack(side=LEFT)
        trace.exit()

    def _display_frames(self):
        """
        Displays all frames that have been set up.
        """
        trace.entry()

        self.columns_frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def _populate_damage_record_sheet(self):
        """
        Populate the damage record sheet with all entries in the database.
        """
        trace.entry()
        self.hits_taken.set(self.total_damage.hits_taken)
        self.total_hits.set(self.character.basic_stats.hits)
        self.bleeding.set(self.total_damage.hits_per_round)
        self.stun.set(self.total_damage.stun)
        self.stun_no_parry.set(self.total_damage.stun_no_parry)
        self.subtraction_from_bonuses.set(self.total_damage.subtraction_from_bonuses)
        self.rounds_to_death.set(self.total_damage.rounds_to_death)
        self.combat_readiness.set(self.total_damage.combat_readiness)

        trace.exit()

    def _apply_updates(self):
        """
        Apply any updates to the character.
        """
        trace.entry()

        self._verify_values()
        self._update_absolute_values()
        self._apply_deltas()

        self._populate_damage_record_sheet()
        self.parent_console.characters_updated()

        # Apply deltas to the character
        # Clear delta values

    def _verify_values(self):
        """
        Police for invalid configured values.
        """
        verify_int_value(self.hits_taken, self.total_damage.hits_taken)
        verify_int_value_or_empty(self.hits_taken_delta, "")

        verify_int_value(self.total_hits, self.character.basic_stats.hits)
        verify_int_value_or_empty(self.total_hits_delta, "")

        verify_int_value(self.bleeding, self.total_damage.hits_per_round)
        verify_int_value_or_empty(self.bleeding_delta, "")

        verify_int_value(self.stun, self.total_damage.stun)
        verify_int_value_or_empty(self.stun_delta, "")

        verify_int_value(self.stun_no_parry, self.total_damage.stun_no_parry)
        verify_int_value_or_empty(self.stun_no_parry_delta, "")

        verify_int_value(self.subtraction_from_bonuses, self.total_damage.subtraction_from_bonuses)
        verify_int_value_or_empty(self.subtraction_from_bonuses_delta, "")

        verify_int_value(self.rounds_to_death, self.total_damage.rounds_to_death)
        verify_int_value_or_empty(self.rounds_to_death_delta, "")

    def _update_absolute_values(self):
        """
        Update absolute values as specified.
        """
        trace.entry()
        self.total_damage.hits_taken = int(self.hits_taken.get())
        self.character.basic_stats.hits = int(self.total_hits.get())
        self.total_damage.hits_per_round = int(self.bleeding.get())
        self.total_damage.stun = int(self.stun.get())
        self.total_damage.stun_no_parry = int(self.stun_no_parry.get())
        self.total_damage.subtraction_from_bonuses = int(self.subtraction_from_bonuses.get())
        self.total_damage.rounds_to_death = int(self.rounds_to_death.get())

        trace.exit()

    def _apply_deltas(self):
        """
        Apply deltas to values as required.
        """
        self.total_damage.hits_taken = self._apply_delta(
            self.hits_taken_delta,
            self.total_damage.hits_taken)
        self.character.basic_stats.hits = self._apply_delta(
            self.total_hits_delta,
            self.character.basic_stats.hits)
        self.total_damage.hits_per_round = self._apply_delta(
            self.bleeding_delta,
            self.total_damage.hits_per_round)
        self.total_damage.stun = self._apply_delta(
            self.stun_delta,
            self.total_damage.stun)
        self.total_damage.stun_no_parry = self._apply_delta(
            self.stun_no_parry_delta,
            self.total_damage.stun_no_parry)
        self.total_damage.subtraction_from_bonuses = self._apply_delta(
            self.subtraction_from_bonuses_delta,
            self.total_damage.subtraction_from_bonuses)
        self.total_damage.rounds_to_death = self._apply_delta(
            self.rounds_to_death_delta,
            self.total_damage.rounds_to_death)

        self.hits_taken_delta.set('')
        self.total_hits_delta.set('')
        self.bleeding_delta.set('')
        self.stun_delta.set('')
        self.stun_no_parry_delta.set('')
        self.subtraction_from_bonuses_delta.set('')
        self.rounds_to_death_delta.set('')

    @staticmethod
    def _apply_delta(delta_value, stored_value):
        """
        Apply a delta to a value.
        """
        if delta_value.get() != '':
            trace.flow("Apply delta %d, original value %d" %
                       (int(delta_value.get()), stored_value))
            stored_value = max(0, stored_value + int(delta_value.get()))
        return stored_value

def main(master=None, parent_console=None, character_database=None, character_index=None):
    """
    Starts the CharacterDamageRecord window.
    :param master: The owning window.
    :param parent_console: The Character Manager that started this Damage Record Sheet.
    :param character_database: The database of all active character information.
    :param character_index: The index of the character corresponding to this record.
    """
    trace.init("Character Damage Record")
    root = Tk()
    CharacterDamageRecord(master, parent_console, character_database, character_index)
    root.mainloop()


if __name__ == '__main__':
    main()
