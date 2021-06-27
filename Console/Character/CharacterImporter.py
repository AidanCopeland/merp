#!/usr/bin/python
# -*- coding: utf-8 -*-
from future import standard_library
from builtins import object
import sys
import os
import json

import trace_log as trace

from tkinter import Tk, LEFT, RIGHT, BOTH, RAISED, OptionMenu, StringVar, Listbox, END, MULTIPLE
from tkinter.ttk import Frame, Label, Style, Button
from tk_helper import refresh_option_menu, clear_option_menu
from .Character import Character

standard_library.install_aliases()

sys.path.append('../../')

CHARACTER_DIRECTORY = '../UserData/Characters/'


class CategoryEntry(object):
    def __init__(self, name, directory, sub_directory_present):
        self.name = name
        self.directory = directory
        self.sub_directory_present = sub_directory_present


# noinspection SpellCheckingInspection
class CharacterImporter(Frame):
    def __init__(self, master, parent_console, character_database):
        trace.entry()

        def initialize_variables(this):
            trace.entry()
            this.style = Style()
            this.style.theme_use("default")

            (this.category_map, this.categories) = self.get_categories()
            this.options = {}

            trace.exit()

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

        initialize_variables(self)
        self.init_ui()

        trace.exit()

    def init_ui(self):
        trace.entry()

        def init_ui_title(this):
            trace.entry()
            title_frame = Frame(this, relief=RAISED, borderwidth=1)
            title_frame.pack(fill=BOTH, expand=True)
            title_label = Label(title_frame, text="Character Importer")
            title_label.pack()
            trace.exit()

        def init_ui_variables(this):
            trace.entry()
            this.category = StringVar()
            this.category.set(this.categories[0])
            this.category.trace("w", lambda *args: this.category_change_callback())
            trace.exit()

        def init_category_selector(this):
            trace.entry()
            this.selector_frame = Frame(self, relief=RAISED, borderwidth=1)
            this.selector_frame.pack(fill=BOTH, expand=True)

            selector_prompt_label = Label(this.selector_frame, text="Category: ")
            selector_prompt_label.pack(side=LEFT)

            this.category_selector = OptionMenu(this.selector_frame, this.category, *this.categories)
            this.category_selector.pack(side=RIGHT)
            trace.exit()

        def init_character_selector(this):
            trace.entry()
            this.character_selector_frame = Frame(self, relief=RAISED, borderwidth=1)
            this.character_selector_frame.pack(fill=BOTH, expand=True)

            selector_prompt_label = Label(self.character_selector_frame, text="Character(s):")
            selector_prompt_label.pack(side=LEFT)

            self.character_selector = Listbox(self.character_selector_frame, selectmode=MULTIPLE)
            self.character_selector.pack(side=RIGHT)

            trace.exit()

        def init_ui_go_button(this):
            trace.entry()
            selection_frame = Frame(this, relief=RAISED, borderwidth=1)
            selection_frame.pack(fill=BOTH, expand=True)
            selection_button = Button(selection_frame,
                                      text='Import character',
                                      command=this.character_import_callback)
            selection_button.pack()
            trace.exit()

        def add_entries_to_category_selector(this):
            trace.entry()
            clear_option_menu(this.category_selector)
            refresh_option_menu(self.category_selector, self.category, self.categories)
            trace.exit()

        init_ui_title(self)
        init_ui_variables(self)
        init_category_selector(self)
        init_character_selector(self)
        init_ui_go_button(self)

        add_entries_to_category_selector(self)

        self.pack(fill=BOTH, expand=True)

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
        character_directory = os.path.join(current_directory, '%s%s' % (CHARACTER_DIRECTORY, category.directory))
        trace.detail("Look for files in %s" % character_directory)

        for entry in os.listdir(character_directory):
            trace.detail("File is %s" % entry)
            filename = os.path.join(character_directory, entry)
            with open(filename, 'r') as myfile:
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
        trace.entry()
        trace.detail("Selected %s" % self.character_name.get())
        self.current_directory = os.path.dirname(__file__)
        trace.detail("Current directory %r" % self.current_directory)
        trace.exit()

    def character_import_callback(self):
        trace.entry()
        selection_indices = self.character_selector.curselection()
        for index in selection_indices:
            character_name = self.character_selector.get(index)
            trace.detail("Character selected %s" % character_name)
            character_object = self.character_map[character_name]
            self.import_character(character_object)

        trace.exit()

    def import_character(self, character_object):
        trace.entry()
        character_entry = Character(character_object)
        self.character_database.add_character(character_entry)
        self.parent_console.characters_updated()
        trace.exit()


def main(master=None, parent_console=None, character_database=None):
    trace.init("Character Importer")
    root = Tk()
    CharacterImporter(master, parent_console, character_database)
    root.mainloop()


if __name__ == '__main__':
    main()
