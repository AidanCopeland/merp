#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Describes a wound taken by a character.

Classes:
    Wound
"""
import sys
import trace_log as trace

sys.path.append('../../')

ACTIVE = "Active"
OUT_OF_COMBAT = "Out of combat"
DYING = "Dying"
UNCONSCIOUS = "Unconscious"
DEAD = "Dead"


class Wound:
    """
    Information about one wound or all damage taken by a character.

    Methods:
        __init__(self)
        add_hits(self, hits)
        set_hits(self, hits)
        add_bleeding(self, bleeding)
        set_bleeding(self, bleeding)
        add_stun(self, stun)
        set_stun(self, stun)
        add_stun_no_parry(self, stun)
        set_stun_no_parry(self, stun)
        add_penalty(self, penalty)
        set_penalty(self, penalty)
        set_rounds_to_death(self, penalty)
    """
    # pylint: disable = too-few-public-methods
    def __init__(self):
        trace.entry()
        self.hits = 0
        self.bleeding = 0
        self.stun = 0
        self.stun_no_parry = 0
        self.penalty = 0
        self.temporary = False
        self.duration_remain = 0
        self.rounds_to_death = 0
        self.location = ""
        self.severity = ""
        self.incapacitation = ACTIVE
        trace.exit()

    def add_hits(self, hits):
        """
        Adds (or subtracts) the number of hits specified to self.hits,
        ensuring that the resulting value is greater than or equal to 0.
        :param hits: The number of hits to add.
        """
        trace.entry()
        self.hits += hits
        self.hits = max(0, self.hits)
        trace.detail("Added {} hits, total now {} hits".format(hits, self.hits))
        trace.exit()

    def set_hits(self, hits):
        """
        Sets the number of hits taken to the value passed in, ensuring that this
        is greater than or equal to 0.
        :param hits: The number of hits that the character has taken.
        """
        trace.entry()
        self.hits = max(0, hits)
        trace.detail("Set hits total to {}".format(self.hits))
        trace.exit()

    def add_bleeding(self, bleeding):
        """
        Updates the number of hits per round being taken by the character by
        adding (or subtracting) the bleeding specified, ensuring that the
        resulting value is greater than or equal to 0.
        :param bleeding: The number of hits per round to add.
        """
        trace.entry()
        self.bleeding += bleeding
        self.bleeding = max(0, self.bleeding)
        trace.detail(
            "Added {} bleeding, total now {} hits per round".format(bleeding, self.bleeding))
        trace.exit()

    def set_bleeding(self, bleeding):
        """
        Sets the number of hits per round being taken by a character, ensuring
        that the value is greater than or equal to 0.
        :param bleeding: The number of hits per round being taken by the
        character.
        """
        trace.entry()
        self.bleeding = max(0, bleeding)
        trace.detail("Set bleeding to {} hits per round".format(self.bleeding))
        trace.exit()

    def add_stun(self, stun):
        """
        Updates the number of rounds that the character is stunned by adding
        (or subtracting) the number of rounds specified, ensuring that the
        resulting value is greater than or equal to 0.
        :param stun: The number of rounds stunned to add.
        """
        trace.entry()
        self.stun += stun
        self.stun = max(0, self.stun)
        trace.detail("Added {} rounds stun, total now {} rounds".format(stun, self.stun))
        trace.exit()

    def set_stun(self, stun):
        """
        Sets the number of rounds that the character is stunned, ensuring that
        the value is greater than or equal to 0.
        :param stun: The number of rounds the character is stunned for.
        """
        trace.entry()
        self.stun = max(0, stun)
        trace.detail("Set stun to {} rounds".format(self.stun))
        trace.exit()

    def add_stun_no_parry(self, stun):
        """
        Updates the number of rounds that the character is stunned and cannot
        parry for by adding (or subtracting) the number of rounds specified,
        ensuring that the resulting value is greater than or equal to 0.
        :param stun: The number of rounds stunned with no parry to add.
        """
        trace.entry()
        self.stun_no_parry += stun
        self.stun_no_parry = max(0, self.stun_no_parry)
        trace.detail(
            "Added {} rounds stun no parry, total now {} rounds".format(stun, self.stun_no_parry))
        trace.exit()

    def set_stun_no_parry(self, stun):
        """
        Sets the number of rounds that the character is stunned and cannot
        parry for, ensuring that the value is greater than or equal to 0.
        :param stun: The number of rounds the character is stunned and cannot
        parry for.
        """
        trace.entry()
        self.stun_no_parry = max(0, stun)
        trace.detail("Set stun no parry to {} rounds".format(self.stun_no_parry))
        trace.exit()

    def add_penalty(self, penalty):
        """
        Updates the penalty that the character is taking to their bonuses by
        adding (or subtracing) the penalty specified, ensuring that the
        resulting penalty is greater than or equal to 0.
        :param penalty: The penalty to add.
        """
        trace.entry()
        self.penalty += penalty
        self.penalty = max(0, penalty)
        trace.detail(
            "Added {} penalty, total subtraction from bonuses {}".format(penalty, self.penalty))
        trace.exit()

    def set_penalty(self, penalty):
        """
        Sets the penalty that the character is taking to their bonuses,
        ensuring that the value is greater than or equal to 0.
        :param penalty: The penalty to set.
        """
        trace.entry()
        self.penalty = max(0, penalty)
        trace.detail("Set subtraction from bonuses to {}".format(self.penalty))
        trace.exit()

    def set_rounds_to_death(self, rounds):
        """
        Sets the number of rounds until death for the character.
        :param rounds: Number of rounds until death.
        """
        trace.entry()
        self.rounds_to_death = max(0, rounds)
        trace.detail("Set rounds to death to {}".format(self.rounds_to_death))
