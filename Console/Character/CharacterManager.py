#!/usr/bin/python
# -*- coding: utf-8 -*-
from future import standard_library
import sys

import trace_log as trace

from tkinter import Tk, LEFT, RIGHT, BOTH, RAISED, OptionMenu, StringVar, Toplevel
from tkinter.ttk import Frame, Label, Style, Button
from tk_helper import clear_option_menu, refresh_option_menu

from .CharacterImporter import CharacterImporter
from .CharacterViewer import CharacterViewer

standard_library.install_aliases()

sys.path.append('../../')

IMPORT_CHARACTERS = "Import characters"
UPDATE_CHARACTERS = "View/update/delete characters"

CHARACTER_IMPORTER = "Character importer"
CHARACTER_VIEWER = "Character viewer"
DAMAGE_RECORD_SHEET = "Damage record sheet"


class CharacterManager(Frame):
    def __init__(self, master, parent_console, character_database):
        trace.entry()

        def initialize_variables(this):
            trace.entry()
            this.style = Style()
            this.style.theme_use("default")

            this.options = (IMPORT_CHARACTERS, UPDATE_CHARACTERS, DAMAGE_RECORD_SHEET)
            this.current_option = IMPORT_CHARACTERS
            trace.exit()

        Frame.__init__(self, master)
        self.parent_console = parent_console
        self.master = master
        self.character_database = character_database

        self.options = None
        self.selector_widget = None
        self.current_option = None
        self.style = None
        self.selector_frame = None
        self.option_selector = None

        self.character_importer = None
        self.character_importer_window = None

        self.character_viewer = None
        self.character_viewer_window = None

        self.damage_record_sheet = None
        self.damage_record_sheet_window = None

        initialize_variables(self)
        self.init_ui()

        trace.exit()

    def init_ui(self):
        trace.entry()

        def init_ui_title(this):
            title_frame = Frame(this, relief=RAISED, borderwidth=1)
            title_frame.pack(fill=BOTH, expand=True)
            title_label = Label(title_frame, text="Character Manager")
            title_label.pack()

        def init_ui_variables(this):
            trace.entry()
            this.selector_widget = StringVar()
            this.selector_widget.set(this.options[0])
            this.selector_widget.trace("w", lambda *args: this.option_change_callback())
            trace.exit()

        def init_ui_selector(this):
            this.selector_frame = Frame(this, relief=RAISED, borderwidth=1)
            this.selector_frame.pack(fill=BOTH, expand=True)
            selector_prompt_label = Label(this.selector_frame, text="Option to select: ")
            selector_prompt_label.pack(side=LEFT)
            this.option_selector = OptionMenu(this.selector_frame,
                                              this.selector_widget,
                                              IMPORT_CHARACTERS,
                                              *this.options)
            this.selector_widget.set(IMPORT_CHARACTERS)
            this.option_selector.pack(side=RIGHT)

        def init_ui_go_button(this):
            selection_frame = Frame(this, relief=RAISED, borderwidth=1)
            selection_frame.pack(fill=BOTH, expand=True)
            selection_button = Button(selection_frame, text='Go!', command=this.launch_option)
            selection_button.pack()

        def add_entries_to_option_selector(this):
            trace.entry()
            clear_option_menu(this.option_selector)
            refresh_option_menu(this.option_selector, this.selector_widget, this.options)
            this.set_current_option(this.selector_widget.get())
            trace.exit()

        init_ui_title(self)
        init_ui_variables(self)
        init_ui_selector(self)
        init_ui_go_button(self)

        add_entries_to_option_selector(self)

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def option_change_callback(self):
        trace.entry()
        trace.detail("Option selected is %r" % self.selector_widget.get())
        self.set_current_option(self.selector_widget.get())
        trace.exit()

    def set_current_option(self, option):
        trace.entry()
        self.current_option = option
        trace.exit()

    def launch_option(self):
        trace.entry()
        trace.detail("Trigger option %s" % self.current_option)
        if self.current_option == IMPORT_CHARACTERS:
            trace.flow("Import characters")
            if self.character_importer_window is None:
                trace.flow("Open character importer")
                self.character_importer_window = Toplevel(self)
                self.character_importer_window.wm_title(CHARACTER_IMPORTER)
                self.character_importer_window.protocol("WM_DELETE_WINDOW", self.character_importer_closed)
                self.character_importer = CharacterImporter(self.character_importer_window,
                                                            self,
                                                            self.character_database)
            elif self.character_importer_window.state() == 'normal':
                trace.flow("Switch focus to character importer")
                self.character_importer_window.focus_set()
            else:
                trace.flow("Deiconify character importer")
                self.character_importer_window.deiconify()

        elif self.current_option == UPDATE_CHARACTERS:
            trace.flow("Character viewer")
            if self.character_viewer is None:
                trace.flow("Open character viewer")
                self.character_viewer_window = Toplevel(self)
                self.character_viewer_window.wm_title(CHARACTER_VIEWER)
                self.character_viewer_window.protocol("WM_DELETE_WINDOW", self.character_viewer_closed)
                self.character_viewer = CharacterViewer(self.character_viewer_window,
                                                        self,
                                                        self.character_database)
            elif self.character_viewer_window.state() == 'normal':
                trace.flow("Switch focus to character viewer")
                self.character_viewer_window.focus_set()
            else:
                trace.flow("Deiconify character viewer")
                self.character_viewer_window.deiconify()
        elif self.current_option == DAMAGE_RECORD_SHEET:
            trace.flow("Damage Record Sheet")
            if self.damage_record_sheet is None:
                trace.flow("Open damage record sheet")
                self.damage_record_sheet_window = Toplevel(self)
                self.damage_record_sheet_window.wm_title(DAMAGE_RECORD_SHEET)
                self.damage_record_sheet_window.protocol("WM_DELETE_WINDOW", self.damage_record_sheet_closed)
                self.damage_record_sheet = DamageRecordSheet(self.damage_record_sheet_window,
                                                             self,
                                                             self.character_database)
            elif self.damage_record_sheet_window.state() == 'normal':
                trace.flow("Switch focus to damage record sheet")
                self.damage_record_sheet_window.focus_set()
            else:
                trace.flow("Deiconify character viewer")
                self.damage_record_sheet_window.deiconify()
        trace.exit()

    def character_importer_closed(self):
        """
        Callback when a request is received to close the character importer
        """
        trace.entry()
        self.character_importer_window.destroy()
        self.character_importer_window = None
        self.character_importer = None

        trace.exit()

    def character_viewer_closed(self):
        """
        Callback when a request is received to close the character viewer
        """
        trace.entry()
        self.character_viewer_window.destroy()
        self.character_viewer_window = None
        self.character_viewer = None

        trace.exit()

    def damage_record_sheet_closed(self):
        """
        Callback when a request is received to close the damage record sheet
        """
        trace.entry()
        self.damage_record_sheet_window.destroy()
        self.damage_record_sheet_window = None
        self.damage_record_sheet = None

        trace.exit()

    def characters_updated(self):
        """
        Tell any other objects using the characters that the characters have been updated.
        """
        trace.entry()
        self.parent_console.characters_updated(self.parent_console)
        if self.character_viewer is not None:
            trace.flow("Kick character viewer")
            self.character_viewer.characters_updated()

        if self.damage_record_sheet is not None:
            trace.flow("Kick damage record sheet")
            self.damage_record_sheet.characters_updated()

        trace.exit()


def main(master=None, parent_console=None, character_database=None):
    trace.init("Character Manager")
    root = Tk()
    CharacterManager(master, parent_console, character_database)
    root.mainloop()


if __name__ == '__main__':
    main()
