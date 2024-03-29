#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the DiceRoller used for handling all dice rolling actions.

Classes:
    DiceRoller
"""
from builtins import range
import sys
from tkinter import Tk, LEFT, RIGHT, END, BOTH, RAISED, StringVar, Text
from tkinter.ttk import Frame, Style, Label, Entry, Button, OptionMenu

from future import standard_library

import dice
import trace_log as trace
from tk_helper import clear_option_menu, refresh_option_menu

standard_library.install_aliases()

sys.path.append('../../')


D10 = "d10"
D100 = "d100"
D100_HIGH = "d100 (open high)"
D100_OPEN = "d100 (open)"
D1000 = "d1000"

dice_value_options = (D10, D100, D100_HIGH, D100_OPEN, D1000)

DICE_SEPARATE = "Separate"
DICE_COMBINED = "Combined"
DICE_SEPARATE_COMBINED = "Separate then combined"

combine_dice_options = (DICE_SEPARATE, DICE_COMBINED, DICE_SEPARATE_COMBINED)


class DiceRoller(Frame):
    """
    The console handling dice rolling.

    Methods:
        __init__(self, master, parent_console)
        single_roll(self)
        roll_dice(self)
        reset_num_dice(self)
        dice_value_change_callback(self, *_args)
        num_dice_change_callback(self, *_args)
        combine_dice_change_callback(self, *_args)
    """

    def __init__(self, master, parent_console):
        self.style = Style()
        self.dice_value = StringVar()
        self.dice_value_options = None
        self.dice_value_selector = None

        self.num_dice = StringVar()

        self.combine_dice_options = combine_dice_options
        self.combine_dice_choice = StringVar()

        self.combine_dice_selector = None
        self.roll_result_text = None

        trace.entry()

        Frame.__init__(self, master)

        self.parent_console = parent_console

        self._initialize_variables()
        dice.randomize()

        self._display_title()
        self._display_dice_value_choice()
        self._display_num_dice_choice()
        self._display_combine_dice_choice()
        self._display_roll_dice()
        self._display_roll_results()

        self._refresh_option_menus()

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def _initialize_variables(self):
        trace.entry()
        self.master.title("Dice Roller")
        self.style.theme_use("default")
        self.dice_value.set(D100_OPEN)
        self.num_dice.set("1")

        trace.exit()

    def _display_title(self):
        trace.entry()
        title_frame = Frame(self, relief=RAISED, borderwidth=1)
        title_frame.pack(fill=BOTH, expand=True)
        title_label = Label(title_frame, text="Dice Roller")
        title_label.pack(side=LEFT)
        trace.exit()

    def _display_dice_value_choice(self):
        trace.entry()
        dice_value_frame = Frame(self, relief=RAISED, borderwidth=1)
        dice_value_frame.pack(fill=BOTH, expand=True)

        dice_value_prompt = Label(dice_value_frame, text="Value of dice to roll: ")
        dice_value_prompt.pack(side=LEFT)

        self.dice_value_options = dice_value_options
        self.dice_value.trace("w", self.dice_value_change_callback)

        self.dice_value_selector = \
            OptionMenu(
                dice_value_frame,
                self.dice_value,
                *self.dice_value_options)
        self.dice_value_selector.pack(side=RIGHT)

        self.dice_value.set(D100_OPEN)
        trace.exit()

    def _display_num_dice_choice(self):
        trace.entry()

        num_dice_frame = Frame(self, relief=RAISED, borderwidth=1)
        num_dice_frame.pack(fill=BOTH, expand=True)

        num_dice_prompt = Label(num_dice_frame, text="Number of dice to roll: ")
        num_dice_prompt.pack(side=LEFT)

        num_dice_input = Entry(num_dice_frame, textvariable=self.num_dice)
        self.num_dice.trace("w", self.num_dice_change_callback)
        num_dice_input.pack(side=RIGHT)
        trace.exit()

    def _display_combine_dice_choice(self):
        trace.entry()
        combine_dice_frame = Frame(self, relief=RAISED, borderwidth=1)
        combine_dice_frame.pack(fill=BOTH, expand=True)

        combine_dice_prompt = Label(combine_dice_frame,
                                    text="Combine dice or report separately: ")
        combine_dice_prompt.pack(side=LEFT)

        self.combine_dice_selector = \
            OptionMenu(
                combine_dice_frame,
                self.combine_dice_choice,
                *self.combine_dice_options)
        self.combine_dice_selector.pack(side=RIGHT)

        self.combine_dice_choice.set(DICE_SEPARATE)
        self.combine_dice_choice.trace("w", self.combine_dice_change_callback)
        trace.exit()

    def _display_roll_dice(self):
        trace.entry()
        trigger_frame = Frame(self, relief=RAISED, borderwidth=1)
        trigger_frame.pack(fill=BOTH, expand=True)
        trigger_button = Button(trigger_frame, text='Roll dice', command=self.roll_dice)
        trigger_button.pack()
        trace.exit()

    def _display_roll_results(self):
        trace.entry()
        roll_results_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.roll_result_text = Text(roll_results_frame)
        roll_results_frame.pack(fill=BOTH, expand=True)
        self.roll_result_text.pack(fill=BOTH)
        trace.exit()

    def _refresh_option_menus(self):
        trace.entry()
        clear_option_menu(self.dice_value_selector)
        refresh_option_menu(self.dice_value_selector,
                            self.dice_value,
                            self.dice_value_options)

        clear_option_menu(self.combine_dice_selector)
        refresh_option_menu(self.combine_dice_selector,
                            self.combine_dice_choice,
                            self.combine_dice_options)
        trace.exit()

    def single_roll(self):
        """
        Makes a single dice roll.
        """
        trace.entry()
        if self.dice_value.get() == D10:
            trace.flow("Roll d10")
            result = dice.d10()
        elif self.dice_value.get() == D100:
            trace.flow("Roll d100")
            result = dice.d100()
        elif self.dice_value.get() == D100_HIGH:
            trace.flow("Roll d100 (open high)")
            result = dice.d100high()
        elif self.dice_value.get() == D100_OPEN:
            trace.flow("Roll d100 (open)")
            result = dice.d100open()
        else:
            trace.flow("Roll d1000")
            result = dice.d1000()
        trace.exit()
        return result

    def roll_dice(self):
        """
        Rolls the selected dice and outputs the result.
        """
        trace.entry()
        self.roll_result_text.delete(1.0, END)
        total_result = 0
        for _roll in range(0, int(self.num_dice.get())):
            result = self.single_roll()
            if self.combine_dice_choice.get() != DICE_COMBINED:
                self.roll_result_text.insert(END, ("Roll: %d\n" % result))
            total_result += result
        if self.combine_dice_choice.get() != DICE_SEPARATE:
            self.roll_result_text.insert(END, ("Total value was %d" % total_result))
        trace.exit()

    def reset_num_dice(self):
        """
        Resets the number of dice to roll to 1.
        """
        trace.entry()
        self.num_dice.set(1)
        trace.exit()

    def dice_value_change_callback(self, *_args):
        """
        Handles the callback when the value of the dice to roll is updated.
        :return:
        """
        trace.entry()
        trace.detail("Dice value changed to %r" % self.dice_value.get())
        if self.num_dice.get() != "1":
            self.reset_num_dice()
        trace.exit()

    def num_dice_change_callback(self, *_args):
        """
        Handles the callback when the setting of the number of dice to roll is updated.
        """
        trace.entry()
        if not self.num_dice.get().isdigit():
            trace.flow("Bad value set")
            self.num_dice.set(1)
        trace.detail("Number of dice changed to %r" % self.num_dice.get())
        trace.exit()

    def combine_dice_change_callback(self, *_args):
        """
        Handles the callback when the setting of whether to combine multiple dice rolls is updated.
        """
        trace.entry()
        trace.detail("Combine dice changed to %r" % self.combine_dice_choice.get())
        trace.exit()


def main(master=None, parent_console=None):
    """
    Starts the Dice Roller window.
    :param master: The owning window.
    :param parent_console: The console that started this instance of dice_roller.
    """
    trace.init("dice_roller")
    root = Tk()
    DiceRoller(master, parent_console)
    root.mainloop()


if __name__ == '__main__':
    main()
