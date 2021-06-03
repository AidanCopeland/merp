#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import json

import trace_log as trace

from Tkinter import Tk, LEFT, RIGHT, BOTH, RAISED, OptionMenu, StringVar, Listbox, Menubutton, END, MULTIPLE, Text, WORD
from ttk import Frame, Label, Style, Button
from tk_helper import clear_option_menu, refresh_option_menu
from Character import Character

sys.path.append('../')


class CharacterViewer(Frame):
    def __init__(self, master, parent_console, character_database):
        trace.entry()

        def initialize_variables(this):
            trace.entry()
            this.style = Style()
            this.style.theme_use("default")

            trace.exit()

        Frame.__init__(self, master)
        self.parent_console = parent_console
        self.master = master
        self.character_database = character_database

        self.style = None
        self.character_display_frame = None
        self.character_list = None

        initialize_variables(self)
        self.init_ui()

        trace.exit()

    def init_ui(self):
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
                                (character.name, character.basic_stats.level, character.stats["ST"].value))
            self.character_list.insert(END, character_string)

        trace.exit()

    def characters_updated(self):
        """
        Redraw the character display with the new database
        """
        trace.entry()
        self.populate_character_display()
        trace.exit()


def main(master=None, parent_console=None, character_database=None):
    trace.init("Character Viewer")
    root = Tk()
    app = CharacterViewer(master, parent_console, character_database)
    root.mainloop()


if __name__ == '__main__':
    main()
