#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the CharacterDamageRecord used to view and update character damage information.

Classes:
    DamageRecordSheet
"""
import sys
from tkinter import Tk, BOTH, RAISED, END, Text, WORD, NO, CENTER, RIGHT, X
from tkinter.ttk import Frame, Label, Style, Treeview, Scrollbar

from future import standard_library

import frame_utils
import trace_log as trace

standard_library.install_aliases()

sys.path.append('../../')


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
        self.parent_console = parent_console
        self.master = master

        self.style = None

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
            title_label = Label(title_frame, text="%s: Damage Record Sheet" % this.character.name)
            title_label.pack()
            trace.exit()

        init_ui_title(self)

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
