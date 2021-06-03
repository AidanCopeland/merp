#!/usr/bin/python
# -*- coding: utf-8 -*-
import trace_log as trace
from Tkinter import Tk


class CharacterDatabase:
    def __init__(self):
        trace.entry()

        self.database = []

        trace.exit()

    def add_character(self, character):
        """
        Add a character to the character database
        :param character: Character to add to the database
        """
        trace.entry()
        self.database.append(character)
        for entry in self.database:
            trace.detail("Database entry %r" % entry)
        trace.exit()

    def num_entries_in_database(self):
        """
        Return the number of entries in the database.
        """
        trace.entry()

        trace.exit()
        return len(self.database)

    def entries_in_database(self):
        """
        Return a the entries in the database.
        """
        trace.entry()

        trace.exit()
        return self.database

    def names_with_indices(self):
        """
        Return a list of names with indices in the database.
        The index values begin with 0.
        A final entry of "Other" is added.
        """
        entries = []
        index = 0
        for entry in self.database:
            entries.append("%s: %s" % (index, entry.name))
            index += 1
        entries.append("%s: Other" % index)

        trace.exit()
        return entries

    def get_character(self, index):
        """
        Return the character entry matching the specified index.
        :param index: Index of character to return.
        :return: Character entry.
        """
        trace.entry()
        trace.detail("Return character index %d" % index)

        trace.exit()
        return self.database[index]

def main():
    trace.init("Character Database")
    root = Tk()
    app = CharacterDatabase()
    root.mainloop()


if __name__ == '__main__':
    main()