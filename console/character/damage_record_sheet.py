#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the DamageRecordSheet used to view and update character damage information.

Classes:
    DamageRecordSheet
"""
import sys
from tkinter import Tk, BOTH, RAISED, END, Text, WORD
from tkinter.ttk import Frame, Label, Style

from future import standard_library

import trace_log as trace

standard_library.install_aliases()

sys.path.append('../../')

# Work to do:
# Print the damage record sheet out as a table
# Add option to reset all damage
# Add option to reset PCs only
# Add option to view details of a single character
# Add option to update each field for a single character
# Feed penalty into maneuvers
# Feed stun into maneuvers
# Allow maneuvers (fumbles) to update damage sheet
# Add end of round trigger: add bleeding, subtract stun (stun no parry first), update rounds to death
# Update incapacity if rounds to death reaches zero
# Allow collected wounds to determine incapacity state


class DamageRecordSheet(Frame):
    """
    The console allowing viewing and updating of character information.

    Methods:
        __init__(self, master, parent_console, character_database)
        populate_damage_record_sheet(self)
        characters_updated(self)
    """
    def __init__(self, master, parent_console, character_database):
        trace.entry()

        Frame.__init__(self, master)
        self.parent_console = parent_console
        self.master = master
        self.character_database = character_database

        self.style = None
        self.damage_record_sheet_frame = None
        self.damage_record_list = None

        self._initialize_variables()
        self._init_ui()

        trace.exit()

    def _initialize_variables(self):
        trace.entry()
        self.style = Style()
        self.style.theme_use("default")

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
            title_label = Label(title_frame, text="Damage Record Sheet")
            title_label.pack()
            trace.exit()

        def init_damage_record_sheet(this):
            this.damage_record_sheet_frame = Frame(self, relief=RAISED, borderwidth=1)
            this.damage_record_list = Text(this.damage_record_sheet_frame, wrap=WORD)
            this.damage_record_sheet_frame.pack(fill=BOTH, expand=True)
            this.damage_record_list.pack(fill=BOTH)

        init_ui_title(self)
        init_damage_record_sheet(self)

        self.populate_damage_record_sheet()

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def populate_damage_record_sheet(self):
        """
        Populate the damage record sheet with all entries in the database.
        """
        trace.entry()
        self.damage_record_list.delete('1.0', END)
        self.damage_record_list.insert(END, "List of characters:\n")
        characters = self.character_database.entries_in_database()
        for character in characters:
            trace.detail("Character stats %r" % character.stats)
            character_damage = character.wounds.total_damage
            character_string = \
                ("{}, hits {}, hits/rnd {}, stun {}, stun no parry {}, penalty {}\n".format(
                    character.name,
                    character_damage.hits,
                    character_damage.bleeding,
                    character_damage.stun,
                    character_damage.stun_no_parry,
                    character_damage.penalty))
            self.damage_record_list.insert(END, character_string)

        trace.exit()

    def characters_updated(self):
        """
        Redraw the character display with the new database
        """
        trace.entry()
        self.populate_damage_record_sheet()
        trace.exit()


def main(master=None, parent_console=None, character_database=None):
    """
    Starts the DamageRecordSheet window.
    :param master: The owning window.
    :param parent_console: The Character Manager that started this Damage Record Sheet.
    :param character_database: The database of all active character information.
    """
    trace.init("Damage Record Sheet")
    root = Tk()
    DamageRecordSheet(master, parent_console, character_database)
    root.mainloop()


if __name__ == '__main__':
    main()
