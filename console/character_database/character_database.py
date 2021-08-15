#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The database of all active characters.

Classes:
    character_database
"""
from tkinter import Tk
from future import standard_library
import trace_log as trace

standard_library.install_aliases()


class CharacterDatabase:
    """
    The database of all active characters.

    Methods:
        __init__(self)
        add_characters(self, character)
        num_entries_in_database(self)
        entries_in_database(self)
        names_with_indices(self)
        get_character(self, index)
        get_character_skills(self, index)
    """
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

    def get_character_skills(self, index):
        """
        Return information about the character's skills.
        :param index: Index of character to return.
        :return: Dict of character's skills.
        """
        trace.entry()
        trace.detail("Get skills for character index %d" % index)

        if index > (len(self.database) - 1):
            trace.flow("No entry in database")
            trace.exit()
            return self.__return_unknown_skills()
        else:
            trace.flow("Return database entry for %s" % self.database[index].name)
            trace.exit()
            return self.__return_character_skills(index)

    def __return_character_skills(self, index):
        """
        Return a list containing the set of skills that a character may use.
        """
        skills = self.database[index].abilities.get_skills_list()
        trace.detail("Skills %r" % skills)
#        skills_dict = self.database[index].abilities.get_skills()
#        skills = []

#        for (skill_name, skill_value) in skills_dict.items():
#            skills.append("%s: %s" % (skill_name, skill_value))

        return skills

    @staticmethod
    def __return_unknown_skills():
        return ["Untrained: -25",]




def main():
    """
    Starts the Character Database.
    """
    trace.init("Character Database")
    root = Tk()
    CharacterDatabase()
    root.mainloop()


if __name__ == '__main__':
    main()
