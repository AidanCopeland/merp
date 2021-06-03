# -*- coding: utf-8 -*-
import sys
sys.path.append('../')

from StaticManeuverTable import *

class TrapLockManeuverTable(StaticManeuverTable):
    maneuver_result_text = {
        BLUNDER: "If picking a lock, your lockpick is broken and stuck in the lock, rendering it unopenable "
                 "until removed (this requires another roll to pick the lock by someone other than you). "
                 "Any traps are set off.",
        ABSOLUTE_FAILURE: "You have developed a mental block on this lock/trap and will automatically fail "
                          "on any further attempts to pick/disarm it. "
                          "There is a 50% chance that any traps will be activated.",
        FAILURE: "Currently you have no further ideas on how to pick/disarm this lock/trap. "
                 "After 24 hours you may make a Perception roll and if it succeeds you may make another attempt.",
        PARTIAL_SUCCESS: "You have figured out part of the lock/trap and have an intuitive feel for the rest. "
                         "Do something else for 10 minutes and then you can try again.",
        NEAR_SUCCESS: "You almost had it. If you spend 2 rounds thinking about your attempt (no other activity), "
                      "you may try again with an extra +5 bonus.",
        SUCCESS: "The lock/trap is picked/disarmed.  +50 on any future attempts to pick/disarm this lock/trap.",
        ABSOLUTE_SUCCESS: "In the future you may automatically pick/disarm (takes one round) this lock/trap "
                          "or any identical lock/trap.  +10 to attempts on similar locks/traps in the future."
    }
