# -*- coding: utf-8 -*-
"""
The Communication static maneuver table.

Classes:
    CommunicationManeuverTable
"""
from __future__ import absolute_import
import sys

from maneuvers.static_maneuver_table import StaticManeuverTable
from maneuvers.static_maneuver_table import BLUNDER, ABSOLUTE_FAILURE, FAILURE
from maneuvers.static_maneuver_table import PARTIAL_SUCCESS, NEAR_SUCCESS, SUCCESS, ABSOLUTE_SUCCESS
import trace_log as trace

sys.path.append('../')


# noinspection SpellCheckingInspection
class CommunicationManeuverTable(StaticManeuverTable):
    """
    communication static maneuver table.

    Methods:
        select_communication_table(maneuver_type)
    """
    MANEUVER_LIP_READING = "Lip Reading"
    MANEUVER_MAGICAL_LANGUAGES = "Magical Languages"
    MANEUVER_SIGNALLING = "Signalling"

    maneuver_type_options = (
        MANEUVER_LIP_READING, MANEUVER_MAGICAL_LANGUAGES, MANEUVER_SIGNALLING
    )

    # noinspection SpellCheckingInspection
    maneuver_result_text = {
        BLUNDER:
            "If this was an attempt at normal communication, you have just delivered (or "
            "received) what seems to be a mortal insult.  If this was an attempt to utilize "
            "a magical language, you have just opened a Lesser Demonic Gate (Evil Essence "
            "list: Entity Summons).  Pretty glib, dude.",
        ABSOLUTE_FAILURE:
            "After a brief attempt at this communication, you realize that you seem to be "
            "conveying (or understanding) exactly the opposite of what was intended.  "
            "You certainly _thought_ that ""Glubmuk"" was a term of respect...",
        FAILURE:
            "Freeboad skiinkeedo meerpblorpop.  Scibi-ibi?  Fwooshikinoosh.  Bork bork bork. "
            "(Whoa.  Gibberish.)",
        PARTIAL_SUCCESS:
            "You appear to be communicating somewhat, but all these strange references to "
            "your grandmother and cream cheese keep confusing the issue.  Keep trying.  "
            "communication was at 2 ranks less efficacy than normal.",
        NEAR_SUCCESS:
            "Cursed homonyms!  Why is it that every language has fifty different words that "
            "sound alike?  If appropriate, you may continue to elucidate for another round to "
            "make yourself clear.  communication was at 1 rank less efficacy than normal.",
        SUCCESS:
            "You are clear, if not concise.  communication is fully achieved, and now you can "
            "explain what it was you were doing with the headman's daughter...",
        ABSOLUTE_SUCCESS:
            "Your command of the language is absolute, and the words fall effortlessly from you.  "
            "If you have any speeches to make, make 'em now!  Reactions to this communication "
            "are modified +30 in your favour.  communication was at 1 rank more efficacy than "
            "normal. "
    }

    maneuver_result_stats = {
        BLUNDER: (-100, 2, -30),
        ABSOLUTE_FAILURE: (-25, 1.5, -10),
        FAILURE: (0, 1, 0),
        PARTIAL_SUCCESS: (30, 1.5, 5),
        NEAR_SUCCESS: (70, 1.25, 15),
        SUCCESS: (100, 1, 20),
        ABSOLUTE_SUCCESS: (120, 0.8, 30)
    }

    @staticmethod
    def select_communication_table(maneuver_type):
        """
        Set the current communication maneuver table to use.
        :param maneuver_type: The type of maneuver selected.
        :return: The maneuver table.
        """
        # pylint: disable=import-outside-toplevel
        # Avoid circular import problems
        from maneuvers.communication.lip_reading_maneuver_table import LipReadingManeuverTable

        if maneuver_type == CommunicationManeuverTable.MANEUVER_LIP_READING:
            trace.flow("Lip Reading maneuver")
            trace.exit()
            return LipReadingManeuverTable()
        else:
            return CommunicationManeuverTable()
