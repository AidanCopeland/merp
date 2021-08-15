#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This module handles character skill bonuses.

Classes: Abilities
"""
import fnmatch
import sys
import trace_log as trace
from .movement_skills import init_movement_skills
from .weapon_skills import init_weapon_skills
from .general_skills import init_general_skills
from .subterfuge_skills import init_subterfuge_skills
from .magical_skills import init_magical_skills
from .leadership_skills import init_leadership_skills
from .language_skills import init_language_skills
from .secondary_skills import init_secondary_skills
sys.path.append('../../')


class Abilities:
    """Abilities class stores a characters skill bonuses.

    Methods:
        __init__(self, abilities_object)
        get_skills(self)
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, abilities_object):
        trace.entry()

        self.movement_skills = init_movement_skills(abilities_object.get("movement-skills"))
        trace.detail("Movement skills: %r" % self.movement_skills)

        self.weapon_skills = init_weapon_skills(abilities_object.get("weapon-skills"))
        trace.detail("Weapon skills: %r" % self.weapon_skills)

        self.general_skills = init_general_skills(abilities_object.get("general-skills"))
        trace.detail("General skills: %r" % self.general_skills)

        self.subterfuge_skills = init_subterfuge_skills(abilities_object.get("subterfuge-skills"))
        trace.detail("Subterfuge skills: %r" % self.subterfuge_skills)

        self.magical_skills = init_magical_skills(abilities_object.get("magical-skills"))
        trace.detail("Magical skills: %r" % self.magical_skills)

        self.leadership_skills = init_leadership_skills(abilities_object.get("leadership-skills"))
        trace.detail("Leadership skills: %r" % self.leadership_skills)

        self.language_skills = init_language_skills(abilities_object.get("language-skills"))
        trace.detail("Language skills: %r" % self.language_skills)

        self.secondary_skills = init_secondary_skills(abilities_object.get("secondary-skills"))
        trace.detail("Secondary skills: %r" % self.secondary_skills)

        trace.exit()

    def get_skills_list(self, preferred_skills):
        """
        Return the character's skill bonuses.
        :param preferred_skills: List of preferred skills to return.
        :return: Dict containing all the character's skills, with the preferred skills at the top,
        if known by the character.
        """
        trace.entry()
        skills_dict = self.__populate_skills_dict()

        preferred_skills_list = self.__populate_preferred_skills_list(skills_dict, preferred_skills)

        skills_list = self.__populate_skills_list()

        trace.detail("Returning %r" % skills_list)
        trace.exit()
        return preferred_skills_list + skills_list

    def __populate_skills_dict(self):
        trace.entry()
        skills = self.movement_skills.copy()
        skills.update(self.weapon_skills)
        skills.update(self.general_skills)
        skills.update(self.subterfuge_skills)
        skills.update(self.magical_skills)
        skills.update(self.leadership_skills)
        skills.update(self.language_skills)
        skills.update(self.secondary_skills)

        trace.exit()
        return skills

    @staticmethod
    def __populate_preferred_skills_list(skills_dict, preferred_skills):
        trace.entry()

        preferred_skills_list = []

        for skill_name in preferred_skills:
            trace.flow("Check skill %s" % skill_name)
            if '*' in skill_name:
                trace.flow("Wildcard skill %s" % skill_name)
                filtered_list = fnmatch.filter(skills_dict, skill_name)
                trace.flow("Filtered dict %r" % filtered_list)
                for skill_name in filtered_list:
                    trace.flow("Found skill %s" % skill_name)
                    preferred_skills_list.append("%s: %s" % (skill_name, skills_dict.get(skill_name)))
            elif skills_dict.get(skill_name) is not None:
                trace.flow("Skill is known by character")
                preferred_skills_list.append("%s: %s" % (skill_name, skills_dict.get(skill_name)))
            else:
                trace.flow("Skill is not known by character")

        trace.detail("Preferred skills list %r" % preferred_skills_list)
        trace.exit()
        return preferred_skills_list

    def __populate_skills_list(self):
        trace.entry()

        skills = self.__skills_category_as_list(self.movement_skills, "===MOVEMENT SKILLS===")
        skills.extend(self.__skills_category_as_list(self.weapon_skills, "===WEAPON SKILLS==="))
        skills.extend(self.__skills_category_as_list(self.general_skills, "===GENERAL SKILLS==="))
        skills.extend(
            self.__skills_category_as_list(self.subterfuge_skills, "===SUBTERFUGE SKILLS==="))
        skills.extend(self.__skills_category_as_list(self.magical_skills, "===MAGICAL SKILLS==="))
        skills.extend(
            self.__skills_category_as_list(
                self.leadership_skills,
                "===LEADERSHIP/INFLUENCE SKILLS==="))
        skills.extend(self.__skills_category_as_list(self.language_skills, "===LANGUAGE SKILLS==="))
        skills.extend(
            self.__skills_category_as_list(self.secondary_skills, "===SECONDARY SKILLS==="))

        skills.insert(0, "Untrained: -25")

        trace.exit()
        return skills

    @staticmethod
    def __skills_category_as_list(skills_dict, category):
        trace.detail("Skills dict %r" % skills_dict)
        skills = []

        for (skill_name, skill_value) in skills_dict.items():
            skills.append("%s: %s" % (skill_name, skill_value))

        trace.detail("Skills %r" % skills)
        if skills:
            skills.insert(0, category)
            trace.detail("Skills %r" % skills)

        return skills
