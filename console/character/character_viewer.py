#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the CharacterViewer used to view and update character information.

Classes:
    CharacterViewer
"""
import sys
from tkinter import Tk, BOTH, RAISED, END, Text, WORD
from tkinter.ttk import Frame, Label, Style

from future import standard_library

import trace_log as trace

standard_library.install_aliases()

sys.path.append('../../')


class CharacterViewer(Frame):
    """
    The console allowing viewing and updating of character information.

    Methods:
        __init__(self, master, merp_console, parent_console, character_database)
        populate_character_display(self)
        characters_updated(self)
    """
    def __init__(self, master, merp_console, parent_console, character_database):
        trace.entry()

        Frame.__init__(self, master)
        self.merp_console = merp_console
        self.parent_console = parent_console
        self.master = master
        self.character_database = character_database

        self.style = None
        self.character_display_frame = None
        self.character_list = None

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
            title_label = Label(title_frame, text="Character Viewer")
            title_label.pack()
            trace.exit()

        def init_character_display(this):
            this.character_display_frame = Frame(self, relief=RAISED, borderwidth=1)
            this.character_list = Text(this.character_display_frame, wrap=WORD)
            this.character_display_frame.pack(fill=BOTH, expand=True)
            this.character_list.pack(fill=BOTH)

        init_ui_title(self)
        init_character_display(self)

        self.populate_character_display()

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def populate_character_display(self):
        """
        Populate the character display with all entries in the database.
        """
        trace.entry()
        self.character_list.delete('1.0', END)
        self.character_list.insert(END, "List of characters:\n")
        characters = self.character_database.entries_in_database()
        for character in characters:
            trace.detail("Character stats %r" % character.stats)
            character_string = ("%s, level %d, ST stat %d\n" %
                                (character.name,
                                 character.basic_stats.level,
                                 character.stats["ST"].value))
            self.character_list.insert(END, character_string)

        trace.exit()

    def characters_updated(self):
        """
        Redraw the character display with the new database
        """
        trace.entry()
        self.populate_character_display()
        trace.exit()


def main(master=None, merp_console=None, parent_console=None, character_database=None):
    """
    Starts the CharacterViewer window.
    :param master: The owning window.
    :param merp_console: The ancestor MERP console.
    :param parent_console: The Character Manager that started this Character Viewer.
    :param character_database: The database of all active character information.
    """
    trace.init("Character Viewer")
    root = Tk()
    CharacterViewer(master, merp_console, parent_console, character_database)
    root.mainloop()


if __name__ == '__main__':
    main()
