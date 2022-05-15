#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the CharacterManager used for handling all actions regarding adding, updating and deleting
characters.

Classes:
    CharacterManager
"""
import sys
from tkinter import Tk, LEFT, RIGHT, BOTH, RAISED, OptionMenu, StringVar, Toplevel
from tkinter.ttk import Frame, Label, Style

from future import standard_library

import frame_utils
import trace_log as trace

from tk_helper import clear_option_menu, refresh_option_menu

from .character_importer import CharacterImporter
from .character_viewer import CharacterViewer
from .damage_record_sheet import DamageRecordSheet

standard_library.install_aliases()

sys.path.append('../../')

IMPORT_CHARACTERS = "Import characters"
UPDATE_CHARACTERS = "View/update/delete characters"

CHARACTER_IMPORTER = "Character importer"
CHARACTER_VIEWER = "Character viewer"
DAMAGE_RECORD_SHEET = "Damage record sheet"


class CharacterManager(Frame):
    """
    The console handling character information.
    Includes character import, update, deletion and damage record.

    Methods:
        __init__(self, master, merp_console, parent_console, character_database)
        init_ui(self)
        option_change_callback(self)
        set_current_option(self, option)
        launch_option(self)
        character_importer_closed(self)
        character_viewer_closed(self)
        damage_record_sheet_closed(self)
        characters_updated(self)
    """
    def __init__(self, master, merp_console, parent_console, character_database):
        trace.entry()

        Frame.__init__(self, master)
        self.merp_console = merp_console
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

        self._initialize_variables()
        self.init_ui()

        trace.exit()

    def _initialize_variables(self):
        trace.entry()
        self.style = Style()
        self.style.theme_use("default")

        self.options = (IMPORT_CHARACTERS, UPDATE_CHARACTERS, DAMAGE_RECORD_SHEET)
        self.current_option = IMPORT_CHARACTERS
        trace.exit()

    def init_ui(self):
        """
        Initializes the components of the CharacterManager window.
        """
        trace.entry()

        self._init_ui_title()
        self._init_ui_variables()
        self._init_ui_selector()
        frame_utils.init_ui_go_button(self, 'Go!', self.launch_option)

        self._add_entries_to_option_selector()

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def _init_ui_title(self):
        title_frame = Frame(self, relief=RAISED, borderwidth=1)
        title_frame.pack(fill=BOTH, expand=True)
        title_label = Label(title_frame, text="Character Manager")
        title_label.pack()

    def _init_ui_variables(self):
        trace.entry()
        self.selector_widget = StringVar()
        self.selector_widget.set(self.options[0])
        self.selector_widget.trace("w", lambda *args: self.option_change_callback())
        trace.exit()

    def _init_ui_selector(self):
        self.selector_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.selector_frame.pack(fill=BOTH, expand=True)
        selector_prompt_label = Label(self.selector_frame, text="Option to select: ")
        selector_prompt_label.pack(side=LEFT)
        self.option_selector = OptionMenu(self.selector_frame,
                                          self.selector_widget,
                                          IMPORT_CHARACTERS,
                                          *self.options)
        self.selector_widget.set(IMPORT_CHARACTERS)
        self.option_selector.pack(side=RIGHT)

    def _add_entries_to_option_selector(self):
        trace.entry()
        clear_option_menu(self.option_selector)
        refresh_option_menu(self.option_selector, self.selector_widget, self.options)
        self.set_current_option(self.selector_widget.get())
        trace.exit()

    def option_change_callback(self):
        """
        Handles the callback when a child console option is selected.
        """
        trace.entry()
        trace.detail("Option selected is %r" % self.selector_widget.get())
        self.set_current_option(self.selector_widget.get())
        trace.exit()

    def set_current_option(self, option):
        """
        Sets the current option to the option specified.
        :param option: The option to set.  Specifies which child console is desired.
        """
        trace.entry()
        self.current_option = option
        trace.exit()

    def launch_option(self):
        """
        Launches or switches focus to the specified option.
        """
        trace.entry()
        trace.detail("Trigger option %s" % self.current_option)
        if self.current_option == IMPORT_CHARACTERS:
            trace.flow("Import characters")
            if self.character_importer_window is None:
                trace.flow("Open character importer")
                self.character_importer_window = Toplevel(self)
                self.character_importer_window.wm_title(CHARACTER_IMPORTER)
                self.character_importer_window.protocol("WM_DELETE_WINDOW",
                                                        self.character_importer_closed)
                self.character_importer = CharacterImporter(self.character_importer_window,
                                                            self.merp_console,
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
                self.character_viewer_window.protocol("WM_DELETE_WINDOW",
                                                      self.character_viewer_closed)
                self.character_viewer = CharacterViewer(self.character_viewer_window,
                                                        self.merp_console,
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
                self.damage_record_sheet_window.protocol("WM_DELETE_WINDOW",
                                                         self.damage_record_sheet_closed)
                self.damage_record_sheet = DamageRecordSheet(self.damage_record_sheet_window,
                                                             self.merp_console,
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
        if self.character_viewer is not None:
            trace.flow("Kick character viewer")
            self.character_viewer.characters_updated()

        if self.damage_record_sheet is not None:
            trace.flow("Kick damage record sheet")
            self.damage_record_sheet.characters_updated()
        trace.exit()


def main(master=None, merp_console=None, parent_console=None, character_database=None):
    """
    Starts the Character Manager window.
    :param master: The owning window.
    :param merp_console: The ancestor MERP console object.
    :param parent_console: The Console object that started this Character Manager.
    :param character_database: The database of all active character information.
    """
    trace.init("Character Manager")
    root = Tk()
    CharacterManager(master, merp_console, parent_console, character_database)
    root.mainloop()


if __name__ == '__main__':
    main()
