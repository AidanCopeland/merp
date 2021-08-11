#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the CharacterImporter used for importing characters into the database of active characters.

Classes:
    CategoryEntry
    CharacterImporter
"""
import sys
import os
import json
from tkinter import Tk, LEFT, RIGHT, BOTH, RAISED, OptionMenu, StringVar, Listbox, END, MULTIPLE
from tkinter.ttk import Frame, Label, Style
from future import standard_library

import frame_utils
import trace_log as trace

from tk_helper import refresh_option_menu, clear_option_menu
from .character import Character

standard_library.install_aliases()

sys.path.append('../../')

CHARACTER_DIRECTORY = '../user_data/characters/'


class CategoryEntry:
    """
    Defines a category of characters to import.

    Methods:
        __init__(self, name, directory, sub_directory_present)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, name, directory, sub_directory_present):
        self.name = name
        self.directory = directory
        self.sub_directory_present = sub_directory_present


# noinspection SpellCheckingInspection
class CharacterImporter(Frame):
    """
    Defines functions for importing characters into the database of active characters.
    Functions:
        __init__(self, master, parent_console, character_database)
        init_ui(self)
        get_categories()
        get_names_in_category(category)
        category_change_callback(self)
        character_select_callback(self)
        import_character(self, character_object)
    """
    def __init__(self, master, parent_console, character_database):
        trace.entry()

        Frame.__init__(self, master)
        self.parent_console = parent_console
        self.master = master
        self.character_database = character_database

        self.options = None
        self.current_directory = None
        self.category = None
        self.character_name = None
        self.style = None
        self.selector_frame = None
        self.character_selector_frame = None
        self.category_selector = None
        self.character_selector = None
        self.category_map = {}
        self.categories = []
        self.character_map = {}
        self.characters = []

        self._initialize_variables()
        self.init_ui()

        trace.exit()

    def _initialize_variables(self):
        trace.entry()
        self.style = Style()
        self.style.theme_use("default")

        (self.category_map, self.categories) = self.get_categories()
        self.options = {}

        trace.exit()

    def init_ui(self):
        """
        Initializes the visible components of the CharacterImporter window.
        """
        trace.entry()

        self._init_ui_title()
        self._init_ui_variables()
        self._init_category_selector()
        self._init_character_selector()
        frame_utils.init_ui_go_button(self, 'Import character', self.character_import_callback)

        self._add_entries_to_category_selector()

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def _init_ui_title(self):
        trace.entry()
        title_frame = Frame(self, relief=RAISED, borderwidth=1)
        title_frame.pack(fill=BOTH, expand=True)
        title_label = Label(title_frame, text="Character Importer")
        title_label.pack()
        trace.exit()

    def _init_ui_variables(self):
        trace.entry()
        self.category = StringVar()
        self.category.set(self.categories[0])
        self.category.trace("w", lambda *args: self.category_change_callback())
        trace.exit()

    def _init_category_selector(self):
        trace.entry()
        self.selector_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.selector_frame.pack(fill=BOTH, expand=True)

        selector_prompt_label = Label(self.selector_frame, text="Category: ")
        selector_prompt_label.pack(side=LEFT)

        self.category_selector = OptionMenu(self.selector_frame,
                                            self.category,
                                            "Player characters",
                                            *self.categories)
        self.category_selector.pack(side=RIGHT)
        trace.exit()

    def _init_character_selector(self):
        trace.entry()
        self.character_selector_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.character_selector_frame.pack(fill=BOTH, expand=True)

        selector_prompt_label = Label(self.character_selector_frame, text="Character(s):")
        selector_prompt_label.pack(side=LEFT)

        self.character_selector = Listbox(self.character_selector_frame, selectmode=MULTIPLE)
        self.character_selector.pack(side=RIGHT)

        trace.exit()

    def _add_entries_to_category_selector(self):
        trace.entry()
        clear_option_menu(self.category_selector)
        refresh_option_menu(self.category_selector, self.category, self.categories)
        trace.exit()

    # noinspection SpellCheckingInspection
    @staticmethod
    def get_categories():
        """
        Read the file indicating the categories of character import available.
        :return: Tuple of:
                   Map of character import categories and their associated CategoryEntry
                   List of the character import categories
        """
        trace.entry()

        # read file
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, '%scategories.json' % CHARACTER_DIRECTORY)
        with open(filename, 'r') as myfile:
            data = myfile.read()

        # parse file
        directory_object = json.loads(data)
        trace.detail("Loaded object %r" % directory_object)
        category_list = directory_object["categories"]
        trace.detail("Category list %r" % category_list)

        category_map = {}
        categories = []

        for entry in category_list:
            trace.detail("Category entry %r" % entry)
            category_entry = CategoryEntry(entry["name"],
                                           entry["directory"],
                                           entry["sub-directory-present"])
            category_map[entry["name"]] = category_entry
            categories.append(entry["name"])

        trace.exit()
        return category_map, categories

    @staticmethod
    def get_names_in_category(category):
        """
        Read the files in the directory indicated by the category entry and return
        the character objects in that directory.
        :return: Tuple of:
                   Map of character names and their associated character dictionary object
                   List of the character names
        """
        trace.entry()
        trace.detail("Category entry is %r" % category)
        character_map = {}
        names = []

        current_directory = os.path.dirname(__file__)
        character_directory = \
            os.path.join(current_directory, '%s%s' % (CHARACTER_DIRECTORY, category.directory))
        trace.detail("Look for files in %s" % character_directory)

        for entry in os.listdir(character_directory):
            trace.detail("File is %s" % entry)
            filename = os.path.join(character_directory, entry)
            with open(filename, 'r', encoding='utf-8') as myfile:
                data = myfile.read()

            # parse file
            character_object = json.loads(data)
            trace.detail("Loaded object %r" % character_object)
            name = character_object["name"]
            trace.detail("Name %s" % name)
            character_map[name] = character_object
            names.append(name)

        trace.exit()
        return character_map, names

    def category_change_callback(self):
        """
        Handles the callback when the category of characters to import has been changed.
        """
        trace.entry()
        category_name = self.category.get()
        trace.detail("Category %s" % category_name)
        category_entry = self.category_map[category_name]
        (self.character_map, self.characters) = self.get_names_in_category(category_entry)

        self.character_selector.delete(0, END)
        for name in self.characters:
            self.character_selector.insert(END, name)
        self.character_selector.pack(side=RIGHT)

        trace.exit()

    def character_select_callback(self):
        """
        Handles the callback when a character has been selected.
        """
        trace.entry()
        trace.detail("Selected %s" % self.character_name.get())
        self.current_directory = os.path.dirname(__file__)
        trace.detail("Current directory %r" % self.current_directory)
        trace.exit()

    def character_import_callback(self):
        """
        Handles the callback when a character has been selected to be imported into the database
        of active characters.
        """
        trace.entry()
        selection_indices = self.character_selector.curselection()
        for index in selection_indices:
            character_name = self.character_selector.get(index)
            trace.detail("Character selected %s" % character_name)
            character_object = self.character_map[character_name]
            self.import_character(character_object)
        self.character_selector.selection_clear(0, END)
        self.parent_console.characters_updated()

        trace.exit()

    def import_character(self, character_object):
        """
        Imports a character into the database of active characters.
        :param character_object: The character object to import.
        """
        trace.entry()
        character_entry = Character(character_object)
        self.character_database.add_character(character_entry)
        trace.exit()


def main(master=None, parent_console=None, character_database=None):
    """
    Starts the Character Importer window.
    :param master: The owning window.
    :param parent_console: The Console object that started this Character Importer.
    :param character_database: Database of all active character information.
    """
    trace.init("Character Importer")
    root = Tk()
    CharacterImporter(master, parent_console, character_database)
    root.mainloop()


if __name__ == '__main__':
    main()
