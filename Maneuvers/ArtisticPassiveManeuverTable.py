# -*- coding: utf-8 -*-
from __future__ import absolute_import

from Maneuvers.StaticManeuverTable import *

import trace_log as trace

sys.path.append('../')


class ArtisticPassiveManeuverTable(StaticManeuverTable):
    MANEUVER_MUSIC = "Music"
    MANEUVER_PAINTING = "Painting"
    MANEUVER_POETRY = "Poetry"
    MANEUVER_SCULPTING = "Sculpting"

    maneuver_type_options = (
        MANEUVER_MUSIC, MANEUVER_PAINTING, MANEUVER_POETRY, MANEUVER_SCULPTING
    )

    # noinspection SpellCheckingInspection
    maneuver_result_text = {
        BLUNDER: "You artist types!  In a fit of pique, there is a chance (50% - PR bonus) that you will destroy "
                 "your artistic materials, including any previous works you may have on hand (roll for each item). "
                 "Although you are sorry about it an hour later, the damage is done.  Any further work with this "
                 "skill will suffer for your lack of equipment and source material.",
        ABSOLUTE_FAILURE: "Your frustration knows no bounds.  In the course of trying to actualize your vision, "
                          "it is lost to distractions and pour media.  It will be at least a week before you will be "
                          "able to use this skill again.",
        FAILURE: "Whatever is locked in your head remains so.  You find yourself utterly unable to transfer your "
                 "concept to another medium.  "
                 "Perhaps another day will yield better results.",
        PARTIAL_SUCCESS: "Your temper flares as your attempts to create fall short of your expectations.  While your "
                         "work has merit, you clearly have not effectively grasped your own intent.  "
                         "A rest period might provide the centering necessary to complete this masterpiece.",
        NEAR_SUCCESS: "Your lip is raw from the chewing you've been giving it.  You can see the outline of your "
                      "creation within your work, but it refuses to emerge.  You take a deep breath and close your "
                      "eyes a moment, then try again with a +10 modification.",
        SUCCESS: "'Twas nothing!  You have once again demonstrated your ample genius to all with the ability to see. "
                 "If only the whole world weren't blind compared to you...",
        ABSOLUTE_SUCCESS: "Ahhh, Bach!  The masterstroke of your piece falls into place with the surety of perfection. "
                          "This piece will make your reputation, if not your fortune.  Who says you have to die to be "
                          "great?"
    }

    maneuver_result_stats = {
        BLUNDER: (-10, 1, -25),
        ABSOLUTE_FAILURE: (-100, 2.5, -10),
        FAILURE: (0, 1.5, 0),
        PARTIAL_SUCCESS: (25, 1.5, 5),
        NEAR_SUCCESS: (80, 1.25, 10),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (150, 1, 35)
    }

    @staticmethod
    def select_artistic_passive_table(maneuver_type):
        """
        Set the current artistic/passive maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        from Maneuvers.ArtisticPassive.MusicManeuverTable import MusicManeuverTable
        from Maneuvers.ArtisticPassive.PaintingManeuverTable import PaintingManeuverTable
        from Maneuvers.ArtisticPassive.PoetryManeuverTable import PoetryManeuverTable
        from Maneuvers.ArtisticPassive.SculptingManeuverTable import SculptingManeuverTable

        if maneuver_type == ArtisticPassiveManeuverTable.MANEUVER_MUSIC:
            trace.flow("Music maneuver")
            trace.exit()
            return MusicManeuverTable()

        elif maneuver_type == ArtisticPassiveManeuverTable.MANEUVER_PAINTING:
            trace.flow("Painting maneuver")
            trace.exit()
            return PaintingManeuverTable()

        elif maneuver_type == ArtisticPassiveManeuverTable.MANEUVER_POETRY:
            trace.flow("Music maneuver")
            trace.exit()
            return PoetryManeuverTable()

        elif maneuver_type == ArtisticPassiveManeuverTable.MANEUVER_SCULPTING:
            trace.flow("Music maneuver")
            trace.exit()
            return SculptingManeuverTable()
