#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the CharacterDamageRecord used to view and update character damage information.

Classes:
    DamageRecordSheet
"""
import sys
from tkinter import Tk, BOTH, RAISED, LEFT, StringVar, FLAT
from tkinter.ttk import Frame, Label, Style

from future import standard_library

import frame_utils
import trace_log as trace
from console.character.total_damage import ACTIVE, OUT_OF_COMBAT, DYING, UNCONSCIOUS, DEAD

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
        self.hits_taken_frame = Frame()
        self.total_hits_frame = Frame()
        self.hits_per_round_frame = Frame()
        self.stun_frame = Frame()
        self.stun_no_parry_frame = Frame()
        self.subtraction_from_bonuses_frame = Frame()
        self.rounds_to_death_frame = Frame()
        self.combat_readiness_frame = Frame()
        self.wounds_frame = Frame()

        self.hits_taken = StringVar()
        self.total_hits = StringVar()
        self.bleeding = StringVar()
        self.stun = StringVar()
        self.stun_no_parry = StringVar()
        self.subtraction_from_bonuses = StringVar()
        self.rounds_to_death = StringVar()
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
        self._init_ui_combat_readiness()
        self._init_ui_wounds()

        self._display_frames()

        trace.exit()

    def _initialize_variables(self):
        trace.entry()
        self.style = Style()
        self.style.theme_use("default")
        self.hits_taken.set(self.total_damage.hits_taken)
        self.total_hits.set(self.character.basic_stats.hits)
        self.bleeding.set(self.total_damage.hits_per_round)
        self.stun.set(self.total_damage.stun)
        self.stun_no_parry.set(self.total_damage.stun_no_parry)
        self.subtraction_from_bonuses.set(self.total_damage.subtraction_from_bonuses)
        self.rounds_to_death.set(self.total_damage.rounds_to_death)
        self.combat_readiness.set(self.total_damage.combat_readiness)

        trace.exit()

    def _init_ui(self):
        """
        Initializes the components of the CharacterViewer window.
        """
        trace.entry()

        def init_ui_title(this):
            trace.entry()
            title_frame = Frame(this, relief=RAISED, borderwidth=1)
            title_frame.pack(fill=BOTH, expand=True)
            title_label = Label(title_frame, text="%s: Damage Record Sheet" % this.character.name)
            title_label.pack()
            trace.exit()

        init_ui_title(self)

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def _init_ui_hits_taken(self):
        trace.entry()
        self.hits_taken_frame = Frame(self, relief=FLAT, borderwidth=1)
        self.hits_taken_frame.pack(fill=BOTH, expand=True)
        frame_utils.setup_entry_frame(
            self.hits_taken_frame,
            HITS_TAKEN_LABEL,
            self.hits_taken)

    def _init_ui_total_hits(self):
        trace.entry()
        self.total_hits_frame = Frame(self, relief=FLAT, borderwidth=1)
        self.total_hits_frame.pack(fill=BOTH, expand=True)
        frame_utils.setup_label_frame(
            self.total_hits_frame,
            TOTAL_HITS_LABEL,
            self.total_hits)

    def _init_ui_bleeding(self):
        trace.entry()
        self.bleeding_frame = Frame(self, relief=FLAT, borderwidth=1)
        self.bleeding_frame.pack(fill=BOTH, expand=True)
        frame_utils.setup_entry_frame(
            self.bleeding_frame,
            HITS_PER_ROUND_LABEL,
            self.bleeding)

    def _init_ui_stun(self):
        trace.entry()
        self.stun_frame = Frame(self, relief=FLAT, borderwidth=1)
        self.stun_frame.pack(fill=BOTH, expand=True)
        frame_utils.setup_entry_frame(
            self.stun_frame,
            ROUNDS_STUNNED_LABEL,
            self.stun)

    def _init_ui_stun_no_parry(self):
        trace.entry()
        self.stun_no_parry_frame = Frame(self, relief=FLAT, borderwidth=1)
        self.stun_no_parry_frame.pack(fill=BOTH, expand=True)
        frame_utils.setup_entry_frame(
            self.stun_no_parry_frame,
            ROUNDS_STUNNED_NO_PARRY_LABEL,
            self.stun_no_parry)

    def _init_ui_subtraction_from_bonuses(self):
        trace.entry()
        self.subtraction_from_bonuses_frame = Frame(self, relief=FLAT, borderwidth=1)
        self.subtraction_from_bonuses_frame.pack(fill=BOTH, expand=True)
        frame_utils.setup_entry_frame(
            self.subtraction_from_bonuses_frame,
            SUBTRACTION_FROM_BONUSES_LABEL,
            self.subtraction_from_bonuses)

    def _init_ui_rounds_to_death(self):
        trace.entry()
        self.rounds_to_death_frame = Frame(self, relief=FLAT, borderwidth=1)
        self.rounds_to_death_frame.pack(fill=BOTH, expand=True)
        frame_utils.setup_entry_frame(
            self.rounds_to_death_frame,
            ROUNDS_TO_DEATH_LABEL,
            self.rounds_to_death)

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

    def _display_frames(self):
        """
        Displays all frames that have been set up.
        :return:
        """
        trace.entry()

        self.pack(fill=BOTH, expand=True)

        trace.exit()


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
