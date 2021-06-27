#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from future import standard_library
import sys
import dice
import trace_log as trace
import FrameUtils
from VerifyUtils import verify_int_value
from collections import namedtuple

from Maneuvers.StaticManeuverTable import StaticManeuverTable
from Maneuvers.MovingManeuverTable import MovingManeuverTable
from Maneuvers.InteractionManeuverTable import InteractionManeuverTable
from Maneuvers.TrapLockManeuverTable import TrapLockManeuverTable
from Maneuvers.RuneItemManeuverTable import RuneItemManeuverTable
from Maneuvers.PerceptionManeuverTable import PerceptionManeuverTable
from Maneuvers.ArtisticActiveManeuverTable import ArtisticActiveManeuverTable
from Maneuvers.ArtisticPassiveManeuverTable import ArtisticPassiveManeuverTable
from Maneuvers.AthleticBrawnManeuverTable import AthleticBrawnManeuverTable
from Maneuvers.AthleticEnduranceManeuverTable import AthleticEnduranceManeuverTable
from Maneuvers.AthleticGymnasticsManeuverTable import AthleticGymnasticsManeuverTable
from Maneuvers.AwarenessPerceptionsManeuverTable import AwarenessPerceptionsManeuverTable
from Maneuvers.AwarenessSearchingManeuverTable import AwarenessSearchingManeuverTable
from Maneuvers.AwarenessSensesManeuverTable import AwarenessSensesManeuverTable
from Maneuvers.CombatManeuversManeuverTable import CombatManeuversManeuverTable
from Maneuvers.CommunicationManeuverTable import CommunicationManeuverTable
from Maneuvers.CraftsManeuverTable import CraftsManeuverTable
from Maneuvers.InfluenceManeuverTable import InfluenceManeuverTable
from Maneuvers.LoreManeuverTable import LoreManeuverTable
from Maneuvers.OutdoorAnimalManeuverTable import OutdoorAnimalManeuverTable
from Maneuvers.OutdoorEnvironmentalManeuverTable import OutdoorEnvironmentalManeuverTable
from Maneuvers.PowerAwarenessManeuverTable import PowerAwarenessManeuverTable
from Maneuvers.PowerManipulationManeuverTable import PowerManipulationManeuverTable
from Maneuvers.ScienceAnalyticManeuverTable import ScienceAnalyticManeuverTable
from Maneuvers.SelfControlManeuverTable import SelfControlManeuverTable
from Maneuvers.SpecialAttacksManeuverTable import SpecialAttacksManeuverTable
from Maneuvers.SpecialDefencesManeuverTable import SpecialDefencesManeuverTable
from Maneuvers.SubterfugeAttackManeuverTable import SubterfugeAttackManeuverTable
from Maneuvers.SubterfugeMechanicsManeuverTable import SubterfugeMechanicsManeuverTable
from Maneuvers.SubterfugeStealthManeuverTable import SubterfugeStealthManeuverTable
from Maneuvers.TechnicalTradeGeneralManeuverTable import TechnicalTradeGeneralManeuverTable
from Maneuvers.TechnicalTradeVocationalManeuverTable import TechnicalTradeVocationalManeuverTable
from Maneuvers.UrbanManeuverTable import UrbanManeuverTable


from tkinter import Tk, LEFT, RIGHT, END, BOTH, FLAT, RAISED, WORD, StringVar, IntVar, Text, Menu, Menubutton
from tkinter.ttk import Frame, Style, Label, Button, OptionMenu
standard_library.install_aliases()

sys.path.append('../')  #

TITLE_TEXT = "Maneuver Table"
MANEUVER_TYPE_LABEL_TEXT = "Maneuver type required: "
MANEUVER_CHARACTER_LABEL_TEXT = "Character carrying out maneuver: "
SKILL_BONUS_LABEL_TEXT = "Skill bonus: "
IS_STUNNED_TEXT = "Is character stunned?"
CHARACTER_PENALTY_LABEL_TEXT = "Injury penalty to character: "
ADDITIONAL_BONUS_LABEL_TEXT = "Additional bonus: "
DICE_ROLL_LABEL_TEXT = "Dice roll (leave blank to roll automatically) "

SKILL_BONUS_DEFAULT = -25
STUN_DEFAULT = 0
CHARACTER_PENALTY_DEFAULT = 0
ADDITIONAL_BONUS_DEFAULT = 0
DICE_ROLL_DEFAULT = ''

MANEUVER_GENERAL_STATIC = "General (static)"
MANEUVER_GENERAL_MOVING = "General (moving)"
MANEUVER_INTERACTION = "Interaction and Influence"
MANEUVER_TRAP_LOCK = "Disarming Traps and Picking Locks"
MANEUVER_RUNE_ITEM = "Reading Runes and Using Items"
MANEUVER_PERCEPTION = "Perception and Tracking"
FUMBLE = "Fumble"

base_maneuver_type_options = (
    MANEUVER_GENERAL_STATIC, MANEUVER_GENERAL_MOVING, MANEUVER_INTERACTION,
    MANEUVER_TRAP_LOCK, MANEUVER_RUNE_ITEM, MANEUVER_PERCEPTION
)

maneuver_type_options = \
    (MANEUVER_GENERAL_STATIC, MANEUVER_GENERAL_MOVING, MANEUVER_INTERACTION,
     MANEUVER_TRAP_LOCK, MANEUVER_RUNE_ITEM, MANEUVER_PERCEPTION) + \
    ArtisticActiveManeuverTable.maneuver_type_options + \
    ArtisticPassiveManeuverTable.maneuver_type_options

ManeuverResult = \
    namedtuple(
        "ManeuverResult",
        ["ResultText", "PercentSuccessful", "TimeTaken", "SubsequentModifier", "Fumble"])


class ManeuverTable(Frame, object):

    def __init__(self, master, parent_console):
        """
        Start up an instance of ManeuverTable, including arranging the required display windows.
        :param master: The parent window containing this instance of ManeuverTable
        :param parent_console: The parent console running this instance of ManeuverTable
        """

        self.style = Style()
        self.maneuver_table_frame = Frame()
        self.maneuver_skill_frame = Frame()
        self.maneuver_fumble_frame = Frame()
        self.maneuver_difficulty_frame = Frame()
        self.maneuver_character_frame = Frame()
        self.maneuver_type = StringVar()
        self.old_maneuver_type = StringVar()
        self.skill_bonus = StringVar()
        self.is_stunned = IntVar()
        self.character_penalty = StringVar()
        self.additional_bonus = StringVar()
        self.dice_roll = StringVar()
        self.result_text = Text(wrap=WORD)
        self.maneuver_table = None
        self.maneuver_character = StringVar()
        self.maneuver_character_selector = None

        self.maneuver_type_options = maneuver_type_options

        trace.entry()

        def initialize_variables():
            """
            Initializes the global variables for this instance of ManeuverTable.
            """
            trace.entry()

            self.master.title(TITLE_TEXT)
            self.style = Style()
            self.style.theme_use("default")
            self.maneuver_type.set(MANEUVER_GENERAL_STATIC)
            self.old_maneuver_type.set(MANEUVER_GENERAL_STATIC)
            self.maneuver_table = StaticManeuverTable()
            self.reset_inputs()

            trace.exit()

        def setup_title_frame():
            """
            Creates a frame to display the title of this window in a Label widget.
            :return:
            """
            trace.entry()
            title_frame = Frame(self, relief=RAISED, borderwidth=1)
            title_frame.pack(fill=BOTH, expand=True)
            title_label = Label(title_frame, text=TITLE_TEXT)
            title_label.pack()
            trace.exit()

        def setup_maneuver_type_menu():
            """
            Creates a frame to allow selection of the maneuver type using a cascaded Menubutton widget.
            :return:
            """
            trace.entry()

            maneuver_type_frame = Frame(self, relief=RAISED, borderwidth=1)
            maneuver_type_frame.pack(fill=BOTH, expand=True)

            maneuver_type_prompt = Label(maneuver_type_frame, text=MANEUVER_TYPE_LABEL_TEXT)
            maneuver_type_prompt.pack(side=LEFT)

            self.maneuver_type.set(MANEUVER_GENERAL_STATIC)
            self.maneuver_type.trace("w", self.maneuver_type_change_callback)

            maneuver_type_menubutton = \
                Menubutton(
                    maneuver_type_frame,
                    textvariable=self.maneuver_type,
                    indicatoron=True,
                    background='light grey',
                    relief=RAISED,
                    borderwidth=1)
            maneuver_type_top_menu = Menu(maneuver_type_menubutton, tearoff=False)
            maneuver_type_menubutton.configure(menu=maneuver_type_top_menu)

            maneuver_options = {
                "General": base_maneuver_type_options,
                "Artistic/Active": ArtisticActiveManeuverTable.maneuver_type_options,
                "Artistic/Passive": ArtisticPassiveManeuverTable.maneuver_type_options,
                "Athletic/Brawn": AthleticBrawnManeuverTable.maneuver_type_options,
                "Athletic/Endurance": AthleticEnduranceManeuverTable.maneuver_type_options,
                "Athletic/Gymnastics": AthleticGymnasticsManeuverTable.maneuver_type_options,
                "Awareness/Perceptions": AwarenessPerceptionsManeuverTable.maneuver_type_options,
                "Awareness/Searching": AwarenessSearchingManeuverTable.maneuver_type_options,
                "Awareness/Senses": AwarenessSensesManeuverTable.maneuver_type_options,
                "Combat Maneuvers": CombatManeuversManeuverTable.maneuver_type_options,
                "Communication": CommunicationManeuverTable.maneuver_type_options,
                "Crafts": CraftsManeuverTable.maneuver_type_options,
                "Influence": InfluenceManeuverTable.maneuver_type_options,
                "Lore": LoreManeuverTable.maneuver_type_options,
                "Outdoor/Animal": OutdoorAnimalManeuverTable.maneuver_type_options,
                "Outdoor/Environmental": OutdoorEnvironmentalManeuverTable.maneuver_type_options,
                "Power Awareness": PowerAwarenessManeuverTable.maneuver_type_options,
                "Power Manipulation": PowerManipulationManeuverTable.maneuver_type_options,
                "Science/Analytic": ScienceAnalyticManeuverTable.maneuver_type_options,
                "Self Control": SelfControlManeuverTable.maneuver_type_options,
                "Special Attacks": SpecialAttacksManeuverTable.maneuver_type_options,
                "Special Defences": SpecialDefencesManeuverTable.maneuver_type_options,
                "Subterfuge/Attack": SubterfugeAttackManeuverTable.maneuver_type_options,
                "Subterfuge/Mechanics": SubterfugeMechanicsManeuverTable.maneuver_type_options,
                "Subterfuge/Stealth": SubterfugeStealthManeuverTable.maneuver_type_options,
                "Technical/Trade General": TechnicalTradeGeneralManeuverTable.maneuver_type_options,
                "Technical/Trade Professional/Vocational": TechnicalTradeVocationalManeuverTable.maneuver_type_options,
                "Urban": UrbanManeuverTable.maneuver_type_options,
            }

            for key in sorted(maneuver_options.keys()):
                menu = Menu(maneuver_type_top_menu, tearoff=False)
                maneuver_type_top_menu.add_cascade(label=key, menu=menu)
                for value in maneuver_options[key]:
                    menu.add_radiobutton(label=value, variable=self.maneuver_type, value=value)

            maneuver_type_menubutton.pack(side=RIGHT)

            trace.exit()

        def setup_maneuver_difficulty_frame(this):
            """
            Creates a frame allowing the current maneuver table to fill in any difficulty selector..
            """
            trace.entry()

            this.maneuver_difficulty_frame = Frame(this, relief=FLAT, borderwidth=0)
            this.maneuver_difficulty_frame.pack(fill=BOTH, expand=True)

            this.maneuver_table.setup_difficulty_frame(this.maneuver_difficulty_frame)

            trace.exit()

        def setup_maneuver_character_frame():
            """
            Creates a frame allowing the current maneuver table to fill in a character selector.
            """
            trace.entry()

            self.maneuver_character_frame = Frame(self, relief=FLAT, borderwidth=0)
            self.maneuver_character_frame.pack(fill=BOTH, expand=True)

            self.populate_maneuver_character_frame(self.maneuver_character_frame)

        def setup_maneuver_table_frames():
            """
            Creates any frames as required by the current maneuver type.
            """
            trace.entry()

            self.maneuver_table_frame = Frame(self, relief=FLAT, borderwidth=0)
            self.maneuver_table_frame.pack(fill=BOTH, expand=True)

            self.maneuver_skill_frame = Frame(self, relief=FLAT, borderwidth=0)
            self.maneuver_skill_frame.pack(fill=BOTH, expand=True)

            self.maneuver_table.setup_maneuver_table_frames(self.maneuver_table_frame)
            self.maneuver_table.setup_maneuver_skill_frames(self.maneuver_skill_frame)

            trace.exit()

        def setup_maneuver_fumble_frame():
            """
            Creates the frame required for a fumble.
            """
            trace.entry()

            self.maneuver_fumble_frame = Frame(self, relief=FLAT, borderwidth=0)
            self.maneuver_fumble_frame.pack(fill=BOTH, expand=True)

            trace.exit()

        def setup_skill_bonus_entry():
            """
            Creates a frame allowing the input of the relevant skill bonus entry using an Entry widget.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(self, SKILL_BONUS_LABEL_TEXT, self.skill_bonus)
            trace.exit()

        def setup_stunned_checkbox():
            """
            Creates a frame with a Checkbox indicating whether the character is stunned.
            """
            trace.entry()
            FrameUtils.setup_checkbox_frame(self, IS_STUNNED_TEXT, self.is_stunned)
            trace.exit()

        def setup_character_penalty_frame():
            """
            Creates a frame allowing the input of any penalty applying to the character using an Entry widget.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(self, CHARACTER_PENALTY_LABEL_TEXT, self.character_penalty)
            trace.exit()

        def setup_additional_bonus_frame():
            """
            Creates a frame allowing the input of any additional bonus using an Entry widget.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(self, ADDITIONAL_BONUS_LABEL_TEXT, self.additional_bonus)
            trace.exit()

        def setup_dice_roll_frame():
            """
            Creates a frame allowing the input of a dice roll using an Entry widget.
            """
            trace.entry()
            FrameUtils.setup_entry_frame(self, DICE_ROLL_LABEL_TEXT, self.dice_roll)
            trace.exit()

        def setup_trigger_button():
            """
            Creates a frame with a button to trigger resolution of the maneuver.
            """
            trace.entry()
            trigger_frame = Frame(self, relief=RAISED, borderwidth=1)
            trigger_frame.pack(fill=BOTH, expand=True)
            trigger_button = Button(trigger_frame, text='Resolve maneuver', command=self.resolve_maneuver)
            trigger_button.pack()
            trace.exit()

        def setup_result_display():
            """
            Creates a frame with a Text widget to display the results of the current maneuver.
            :return:
            """
            trace.entry()
            results_frame = Frame(self, relief=RAISED, borderwidth=1)
            self.result_text = Text(results_frame, wrap=WORD)
            results_frame.pack(fill=BOTH, expand=True)
            self.result_text.pack(fill=BOTH)
            trace.exit()

        def display_frames():
            """
            Displays all frames that have been set up.
            :return:
            """
            trace.entry()

            self.pack(fill=BOTH, expand=True)

            trace.exit()

        Frame.__init__(self, master)

        self.parent_console = parent_console

        initialize_variables()
        dice.randomize()

        setup_title_frame()
        setup_maneuver_type_menu()
        setup_maneuver_difficulty_frame(self)
        setup_maneuver_character_frame()
        setup_maneuver_table_frames()
        setup_skill_bonus_entry()
        setup_stunned_checkbox()
        setup_character_penalty_frame()
        setup_additional_bonus_frame()
        setup_dice_roll_frame()
        setup_trigger_button()
        setup_maneuver_fumble_frame()
        setup_result_display()

        display_frames()

        trace.exit()

    def reset_inputs(self):
        """
        Reset all inputs to their default.
        This is called when the type of selected maneuver changes.
        """
        trace.entry()

        self.skill_bonus.set(SKILL_BONUS_DEFAULT)
        self.is_stunned.set(STUN_DEFAULT)
        self.character_penalty.set(CHARACTER_PENALTY_DEFAULT)
        self.additional_bonus.set(ADDITIONAL_BONUS_DEFAULT)
        self.dice_roll.set(DICE_ROLL_DEFAULT)
        self.result_text.delete(1.0, END)

        trace.exit()

    def characters_updated(self):
        """
        Redraw the character display with the new database
        """
        trace.entry()

        self.populate_maneuver_character_frame(self.maneuver_character_frame)

        trace.exit()

    def populate_maneuver_character_frame(self, parent_frame):
        FrameUtils.destroy_frame_objects(parent_frame)

        maneuver_character_frame = Frame(parent_frame, relief=RAISED, borderwidth=1)
        maneuver_character_frame.pack(fill=BOTH, expand=True)

        maneuver_character_prompt = Label(maneuver_character_frame, text=MANEUVER_CHARACTER_LABEL_TEXT)
        maneuver_character_prompt.pack(side=LEFT)

        names_with_indices = tuple(self.parent_console.character_database.names_with_indices())

        self.maneuver_character_selector = \
            OptionMenu(
                maneuver_character_frame,
                self.maneuver_character,
                names_with_indices[0],
                *names_with_indices)
        self.maneuver_character_selector.pack(side=RIGHT)

    def maneuver_type_change_callback(self, *_args):
        """
        Callback made when the type of selected maneuver changes
        """

        def select_maneuver_table():
            """
            Set the current maneuver table to use.
            :return: The maneuver table.
            """
            trace.entry()

            if maneuver_type == MANEUVER_INTERACTION:
                trace.flow("Interaction maneuver")
                trace.exit()
                return InteractionManeuverTable()
            elif maneuver_type == MANEUVER_TRAP_LOCK:
                trace.flow("Traps/Locks maneuver")
                trace.exit()
                return TrapLockManeuverTable()
            elif maneuver_type == MANEUVER_RUNE_ITEM:
                trace.flow("Read Runes/Use Items maneuver")
                trace.exit()
                return RuneItemManeuverTable()
            elif maneuver_type == MANEUVER_PERCEPTION:
                trace.flow("Perception maneuver")
                trace.exit()
                return PerceptionManeuverTable()
            elif maneuver_type in ArtisticActiveManeuverTable.maneuver_type_options:
                trace.flow("Artistic/Active maneuver")
                trace.exit()
                return ArtisticActiveManeuverTable.select_artistic_active_table(maneuver_type)
            elif maneuver_type in ArtisticPassiveManeuverTable.maneuver_type_options:
                trace.flow("Artistic/Passive maneuver")
                trace.exit()
                return ArtisticPassiveManeuverTable.select_artistic_passive_table(maneuver_type)
            elif maneuver_type in AthleticBrawnManeuverTable.maneuver_type_options:
                trace.flow("Athletic/Brawn maneuver")
                trace.exit()
                return AthleticBrawnManeuverTable.select_athletic_brawn_table(maneuver_type)
            elif maneuver_type in AthleticEnduranceManeuverTable.maneuver_type_options:
                trace.flow("Athletic/Endurance maneuver")
                trace.exit()
                return AthleticEnduranceManeuverTable.select_athletic_endurance_table(maneuver_type)
            elif maneuver_type in AthleticGymnasticsManeuverTable.maneuver_type_options:
                trace.flow("Athletic/Gymnastics maneuver")
                trace.exit()
                return AthleticGymnasticsManeuverTable.select_athletic_gymnastics_table(maneuver_type)
            elif maneuver_type in AwarenessPerceptionsManeuverTable.maneuver_type_options:
                trace.flow("Awareness/Perceptions maneuver")
                trace.exit()
                return AwarenessPerceptionsManeuverTable.select_awareness_perceptions_table(maneuver_type)
            elif maneuver_type in AwarenessSearchingManeuverTable.maneuver_type_options:
                trace.flow("Awareness/Searching maneuver")
                trace.exit()
                return AwarenessSearchingManeuverTable.select_awareness_searching_table(maneuver_type)
            elif maneuver_type in AwarenessSensesManeuverTable.maneuver_type_options:
                trace.flow("Awareness/Senses maneuver")
                trace.exit()
                return AwarenessSensesManeuverTable.select_awareness_senses_table(maneuver_type)
            elif maneuver_type in CombatManeuversManeuverTable.maneuver_type_options:
                trace.flow("Combat Maneuvers maneuver")
                trace.exit()
                return CombatManeuversManeuverTable.select_combat_maneuvers_table(maneuver_type)
            elif maneuver_type in CommunicationManeuverTable.maneuver_type_options:
                trace.flow("Communication maneuver")
                trace.exit()
                return CommunicationManeuverTable.select_communication_table(maneuver_type)
            elif maneuver_type in CraftsManeuverTable.maneuver_type_options:
                trace.flow("Crafts maneuver")
                trace.exit()
                return CraftsManeuverTable.select_crafts_table()
            elif maneuver_type in InfluenceManeuverTable.maneuver_type_options:
                trace.flow("Influence maneuver")
                trace.exit()
                return InfluenceManeuverTable.select_influence_table(maneuver_type)
            elif maneuver_type in LoreManeuverTable.maneuver_type_options:
                trace.flow("Lore maneuver")
                trace.exit()
                return LoreManeuverTable.select_lore_table(maneuver_type)
            elif maneuver_type in OutdoorAnimalManeuverTable.maneuver_type_options:
                trace.flow("Outdoor/Animal maneuver")
                trace.exit()
                return OutdoorAnimalManeuverTable.select_outdoor_animal_table(maneuver_type)
            elif maneuver_type in OutdoorEnvironmentalManeuverTable.maneuver_type_options:
                trace.flow("Outdoor/Environmental maneuver")
                trace.exit()
                return OutdoorEnvironmentalManeuverTable.select_outdoor_environmental_table(maneuver_type)
            elif maneuver_type in PowerAwarenessManeuverTable.maneuver_type_options:
                trace.flow("Power Awareness maneuver")
                trace.exit()
                return PowerAwarenessManeuverTable.select_power_awareness_table(maneuver_type)
            elif maneuver_type in PowerManipulationManeuverTable.maneuver_type_options:
                trace.flow("Power Manipulation maneuver")
                trace.exit()
                return PowerManipulationManeuverTable.select_power_manipulation_table(maneuver_type)
            elif maneuver_type in ScienceAnalyticManeuverTable.maneuver_type_options:
                trace.flow("Science/Analytic maneuver")
                trace.exit()
                return ScienceAnalyticManeuverTable.select_science_analytic_table(maneuver_type)
            elif maneuver_type in SelfControlManeuverTable.maneuver_type_options:
                trace.flow("Self Control maneuver")
                trace.exit()
                return SelfControlManeuverTable.select_self_control_table(maneuver_type)
            elif maneuver_type in SpecialAttacksManeuverTable.maneuver_type_options:
                trace.flow("Special Attacks maneuver")
                trace.exit()
                return SpecialAttacksManeuverTable.select_special_attacks_table()
            elif maneuver_type in SpecialDefencesManeuverTable.maneuver_type_options:
                trace.flow("Special Defences maneuver")
                trace.exit()
                return SpecialDefencesManeuverTable.select_special_defences_table()
            elif maneuver_type in SubterfugeAttackManeuverTable.maneuver_type_options:
                trace.flow("Subterfuge/Attack maneuver")
                trace.exit()
                return SubterfugeAttackManeuverTable.select_subterfuge_attack_table()
            elif maneuver_type in SubterfugeMechanicsManeuverTable.maneuver_type_options:
                trace.flow("Subterfuge/Mechanics maneuver")
                trace.exit()
                return SubterfugeMechanicsManeuverTable.select_subterfuge_mechanics_table(maneuver_type)
            elif maneuver_type in SubterfugeStealthManeuverTable.maneuver_type_options:
                trace.flow("Subterfuge/Mechanics maneuver")
                trace.exit()
                return SubterfugeStealthManeuverTable.select_subterfuge_stealth_table(maneuver_type)
            elif maneuver_type in TechnicalTradeGeneralManeuverTable.maneuver_type_options:
                trace.flow("Technical/Trade General maneuver")
                trace.exit()
                return TechnicalTradeGeneralManeuverTable.select_technical_trade_general_table()
            elif maneuver_type in TechnicalTradeVocationalManeuverTable.maneuver_type_options:
                trace.flow("Technical/Trade Professional/Vocational maneuver")
                trace.exit()
                return TechnicalTradeVocationalManeuverTable.select_technical_trade_vocational_table()
            elif maneuver_type in UrbanManeuverTable.maneuver_type_options:
                trace.flow("Urban maneuver")
                trace.exit()
                return UrbanManeuverTable.select_urban_table()
            elif maneuver_type == MANEUVER_GENERAL_STATIC:
                trace.flow("General maneuver (static)")
                trace.exit()
                return StaticManeuverTable()
            else:
                trace.flow("General maneuver (moving)")
                trace.exit()
                return MovingManeuverTable()

        trace.entry()
        trace.detail("Maneuver type changed to %r" % self.maneuver_type.get())
        maneuver_type = self.maneuver_type.get()
        if maneuver_type != self.old_maneuver_type.get():
            trace.flow("Set up new maneuver table")
            self.maneuver_table = select_maneuver_table()

            """Redraw the frames specific to the new maneuver table type"""
            self.maneuver_table.setup_difficulty_frame(self.maneuver_difficulty_frame)
            self.maneuver_table.setup_maneuver_table_frames(self.maneuver_table_frame)
            self.maneuver_table.setup_maneuver_skill_frames(self.maneuver_skill_frame)
            self.reset_inputs()
        self.old_maneuver_type.set(self.maneuver_type.get())
        trace.exit()

    def verify_inputs(self):
        """
        Function to verify any inputs and reset any with an illegal value to the default.
        """
        trace.entry()

        verify_int_value(self.skill_bonus, SKILL_BONUS_DEFAULT)
        verify_int_value(self.character_penalty, CHARACTER_PENALTY_DEFAULT)
        verify_int_value(self.additional_bonus, ADDITIONAL_BONUS_DEFAULT)

        if self.dice_roll.get() != DICE_ROLL_DEFAULT:
            try:
                test = int(self.dice_roll.get())
                trace.detail("Dice roll set to %d" % test)
            except ValueError:
                self.dice_roll.set(DICE_ROLL_DEFAULT)
                trace.detail("Dice roll reset to default")

        trace.exit()

    def calculate_modifiers(self):
        """
        Calculate the modifiers to apply to the current dice roll.
        :return: The total modifier to apply.
        """
        skill_bonus = int(self.skill_bonus.get())
        trace.detail("Skill bonus: %d" % skill_bonus)

        difficulty_bonus = self.maneuver_table.difficulty_bonus()
        trace.detail("Difficulty bonus: %d" % difficulty_bonus)

        stun_bonus = 0
        if self.is_stunned.get() == 1:
            trace.flow("Stunned")
            stun_bonus = -50

        character_penalty = int(self.character_penalty.get())
        trace.detail("Character penalty: %d" % character_penalty)

        table_bonus = self.maneuver_table.table_bonus()
        trace.detail("Table bonus: %d" % table_bonus)

        skill_type_bonus = self.maneuver_table.skill_type_bonus()
        trace.detail("Skill type bonus: %d" % skill_type_bonus)

        additional_bonus = int(self.additional_bonus.get())
        trace.detail("Additional bonus: %d" % additional_bonus)

        total_bonus = \
            skill_bonus + \
            difficulty_bonus + \
            stun_bonus - \
            character_penalty + \
            table_bonus + \
            skill_type_bonus + \
            additional_bonus
        trace.detail("Total bonus: %d" % total_bonus)
        trace.exit()
        return total_bonus

    def resolve_maneuver(self):
        """
        Callback made to resolve the current maneuver.
        """
        trace.entry()

        self.verify_inputs()
        dice_roll = self.roll_dice()
        modifiers = self.calculate_modifiers()

        self.result_text.delete(1.0, END)
        self.result_text.insert(END, ("Roll: %d\n" % dice_roll))
        self.result_text.insert(END, ("Modified roll: %d\n" % (dice_roll + modifiers)))

        maneuver_resolution = self.maneuver_table.maneuver_resolution(dice_roll + modifiers)
        self.result_text.insert(END, maneuver_resolution.ResultText + "\n\n\n")

        if maneuver_resolution.Fumble:
            self.result_text.insert(
                END,
                "The attempt was fumbled.  Roll again to resolve the fumble.\n"
            )
            self.setup_fumble()

        if maneuver_resolution.PercentSuccessful != 100 and maneuver_resolution.PercentSuccessful != 0:
            self.result_text.insert(
                END,
                "If partial success was possible, the maneuver was %d%% successful.\n" %
                maneuver_resolution.PercentSuccessful)
        if maneuver_resolution.TimeTaken != 1:
            self.result_text.insert(
                END,
                "The result took %r times the normal time for the maneuver.\n" % maneuver_resolution.TimeTaken)
        if maneuver_resolution.SubsequentModifier != 0:
            self.result_text.insert(
                END,
                "There is a %+d modifier to any subsequent related action by this character.\n"
                % maneuver_resolution.SubsequentModifier)
        self.result_text.insert(END, "")

        trace.exit()

    def roll_dice(self):
        """
        Function to roll the dice if required.
        :return: The dice roll to use
        """
        trace.entry()

        if self.dice_roll.get() == DICE_ROLL_DEFAULT:
            trace.flow("Roll dice")
            result = dice.d100open()
        else:
            trace.flow("Dice roll supplied")
            result = int(self.dice_roll.get())

        trace.exit()
        return result

    def setup_fumble(self):
        """
        Set up requirements to resolve a fumbled maneuver.
        """
        trace.entry()

        self.dice_roll.set(DICE_ROLL_DEFAULT)
        self.setup_fumble_trigger_button()

        trace.exit()

    def setup_fumble_trigger_button(self):
        """
        Creates a frame with a button to trigger resolution of the maneuver.
        """
        trace.entry()
        trigger_frame = Frame(self.maneuver_fumble_frame, relief=RAISED, borderwidth=1)
        trigger_frame.pack(fill=BOTH, expand=True)
        trigger_button = Button(trigger_frame, text='Resolve fumble', command=self.resolve_fumble)
        trigger_button.pack()
        trace.exit()

    def resolve_fumble(self):
        """
        Resolve a fumbled maneuver.
        :return:
        """
        trace.entry()

        dice_roll = self.roll_fumble_dice()
        fumble_text = self.maneuver_table.resolve_fumble(dice_roll)

        self.result_text.delete(1.0, END)
        self.result_text.insert(END, fumble_text)
        FrameUtils.destroy_frame_objects(self.maneuver_fumble_frame)

        trace.exit()

    def roll_fumble_dice(self):
        """
        Function to roll the dice for a fumble if required.
        :return: The dice roll to use
        """
        trace.entry()

        if self.dice_roll.get() == DICE_ROLL_DEFAULT:
            trace.flow("Roll dice")
            result = dice.d100()
        else:
            trace.flow("Dice roll supplied")
            result = int(self.dice_roll.get())

        trace.exit()
        return result


def main(master=None, parent_console=None):
    trace.init("ManeuverTable")
    root = Tk()
    ManeuverTable(master, parent_console)
    root.mainloop()


if __name__ == '__main__':
    main()
