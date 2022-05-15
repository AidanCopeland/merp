#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Creates the DamageRecordSheet used to view and update character damage information.

Classes:
    DamageRecordSheet
"""
import sys
from tkinter import Tk, BOTH, RAISED, NO, CENTER, RIGHT, Toplevel
from tkinter.ttk import Frame, Label, Style, Treeview, Scrollbar

from future import standard_library

from console.character.character_damage_record import CharacterDamageRecord
import frame_utils
import trace_log as trace

standard_library.install_aliases()

sys.path.append('../../')

# Work to do:
# Feed stun into maneuvers
# Allow maneuvers (fumbles) to update damage sheet
# Add combat readiness for a single character: track weapon arm, inactive, unconscious, dead separately
# Add end of round trigger: add bleeding, subtract stun (stun no parry first), update rounds to death
# Update incapacity if rounds to death reaches zero
# Allow collected wounds to determine incapacity state
# Update state based on hits, total hits
# Add checker to verify resetting character/party/all

DAMAGE_RECORD_SHEET = ": Damage Record Sheet"


def _clear_table(damage_record_table):
    trace.entry()
    table_entries = damage_record_table.get_children()
    for entry in table_entries:
        trace.flow("Delete entry ID {}".format(entry))
        damage_record_table.delete(entry)


class DamageRecordSheet(Frame):
    """
    The console allowing viewing and updating of character information.

    Methods:
        __init__(self, master, merp_console, parent_console, character_database)
        populate_damage_record_sheet(self)
    """
    def __init__(self, master, merp_console, parent_console, character_database):
        trace.entry()

        Frame.__init__(self, master)
        self.merp_console = merp_console
        self.parent_console = parent_console
        self.master = master
        self.character_database = character_database

        self.style = None
        self.damage_record_sheet_frame = None
        self.damage_record_table = None
        self.damage_record_scrollbar = None

        self.character_damage_record = {}
        self.character_damage_record_window = {}

        self._initialize_variables()
        self._init_ui()

        trace.exit()

    def _initialize_variables(self):
        trace.entry()
        self.style = Style()
        self.style.theme_use("default")

        trace.exit()

    def _init_ui(self):
        """
        Initializes the components of the CharacterViewer window.
        """
        trace.entry()

        def init_ui_title(this):
            trace.entry()
            title_frame = Frame(this, relief=RAISED, borderwidth=1)
            title_frame.pack(fill=BOTH, expand=True)
            title_label = Label(title_frame, text="Damage Record Sheet")
            title_label.pack()
            trace.exit()

        def init_damage_record_sheet(this):
            this.damage_record_sheet_frame = Frame(self, relief=RAISED, borderwidth=1)
            damage_record_table = Treeview(
                self.damage_record_sheet_frame,
                columns=("Name", "Hits", "Hits/rnd", "Stun", "Stun no parry", "Penalties", "State"),
                selectmode="browse"
            )
            damage_record_table.column('#0', width=0, stretch=NO)
            damage_record_table.column("Name", width=200)
            damage_record_table.column("Hits", anchor=CENTER, width=60)
            damage_record_table.column("Hits/rnd", anchor=CENTER, width=60)
            damage_record_table.column("Stun", anchor=CENTER, width=60)
            damage_record_table.column("Stun no parry", anchor=CENTER, width=80)
            damage_record_table.column("Penalties", anchor=CENTER, width=80)
            damage_record_table.column("State", anchor=CENTER, width=300)

            damage_record_table.heading('#0', text='', anchor=CENTER)
            damage_record_table.heading("Name", text="Name")
            damage_record_table.heading("Hits", text="Hits", anchor=CENTER)
            damage_record_table.heading("Hits/rnd", text="Hits/rnd", anchor=CENTER)
            damage_record_table.heading("Stun", text="Stun", anchor=CENTER)
            damage_record_table.heading("Stun no parry", text="Stun no parry", anchor=CENTER)
            damage_record_table.heading("Penalties", text="Penalties", anchor=CENTER)
            damage_record_table.heading("State", text="State", anchor=CENTER)

            this.damage_record_table = damage_record_table

            this.damage_record_scrollbar = Scrollbar(
                self.damage_record_sheet_frame,
                orient="vertical")
            this.damage_record_scrollbar.configure(command=this.damage_record_table.yview)
            this.damage_record_table.configure(yscrollcommand=this.damage_record_scrollbar.set)
            this.damage_record_scrollbar.pack(side=RIGHT, fill=BOTH)
            this.damage_record_table.pack()
            this.damage_record_sheet_frame.pack(fill=BOTH, expand=True)

        init_ui_title(self)
        init_damage_record_sheet(self)
        frame_utils.init_ui_go_buttons(
            self,
            [
                ('View/edit selected', self.view_edit_character),
                ('Reset selected', self.reset_character),
                ('Reset party', self.reset_party),
                ('Reset all', self.reset_all)
            ]
        )

        self.populate_damage_record_sheet(self.damage_record_table)

        self.pack(fill=BOTH, expand=True)

        trace.exit()

    def populate_damage_record_sheet(self, damage_record_table):
        """
        Populate the damage record sheet with all entries in the database.
        """
        trace.entry()
        _clear_table(damage_record_table)
        characters = self.character_database.entries_in_database_with_indices()
        for (character, index) in characters:
            trace.detail("Character stats %r" % character.stats)
            character_damage = character.total_damage
            damage_record_table.insert(
                parent="",
                index=index,
                iid=index,
                values=(
                    character.name,
                    character_damage.hits_taken,
                    character_damage.hits_per_round,
                    character_damage.stun,
                    character_damage.stun_no_parry,
                    character_damage.subtraction_from_bonuses,
                    character_damage.combat_readiness
                )
            )

        trace.exit()

    def characters_updated(self):
        """
        Redraw the character display with the new database
        """
        trace.entry()
        self.populate_damage_record_sheet(self.damage_record_table)
        trace.exit()

    def view_edit_character(self):
        """
        View or edit the currently selected character.
        """
        trace.entry()
        character_index_str = self.damage_record_table.focus()
        if character_index_str != '':
            character_index = int(character_index_str)
            if self.character_damage_record.get(character_index) is None:
                trace.flow("Open character damage record sheet, index %s" % character_index)
                character = self.character_database.get_character(int(character_index))
                self.character_damage_record_window[character_index] = Toplevel(self)
                self.character_damage_record_window[character_index].wm_title(
                    "%s%s" % (character.name, DAMAGE_RECORD_SHEET))
                self.character_damage_record_window[character_index].protocol(
                    "WM_DELETE_WINDOW",
                    lambda character=character_index: self.character_damage_window_closed(character_index))
                self.character_damage_record[character_index] = \
                    CharacterDamageRecord(
                        self.character_damage_record_window[character_index],
                        self.merp_console,
                        self,
                        self.character_database,
                        int(character_index)
                    )

            elif self.character_damage_record_window[character_index].state() == 'normal':
                trace.flow("Switch focus to damage record sheet")
                self.character_damage_record_window[character_index].focus_set()
            else:
                trace.flow("Deiconify character viewer")
                self.character_damage_record_window[character_index].deiconify()
        trace.exit()

    def character_damage_window_closed(self, character_index):
        """
        Callback when a request is received to close the character damage record window.
        """
        trace.entry()
        self.character_damage_record_window[character_index].destroy()
        self.character_damage_record_window[character_index] = None
        self.character_damage_record[character_index] = None

        trace.exit()

    def reset_character(self):
        """
        Reset the currently selected character.
        """
        trace.entry()
        character_index_str = self.damage_record_table.focus()
        if character_index_str != '':
            trace.flow("Reset character index %d" % int(character_index_str))
            character_index = int(character_index_str)
            character = self.character_database.get_character(character_index)
            self._reset_character(character, character_index)
            self.merp_console.characters_updated()
        trace.exit()

    def reset_party(self):
        """
        Reset all PCs.
        """
        trace.entry()
        characters_with_indices = self.character_database.entries_in_database_with_indices()
        for (character, character_index) in characters_with_indices:
            trace.flow("Check character index %d" % character_index)
            if character.is_pc:
                trace.flow("Reset character")
                self._reset_character(character, character_index)
        self.merp_console.characters_updated()
        trace.exit()

    def reset_all(self):
        """
        Reset all PCs and NPCs.
        """
        trace.entry()
        characters_with_indices = self.character_database.entries_in_database_with_indices()
        for (character, character_index) in characters_with_indices:
            trace.flow("Reset character index %d" % character_index)
            self._reset_character(character, character_index)
        self.merp_console.characters_updated()
        trace.exit()

    def _reset_character(self, character, character_index):
        """
        Reset all damage for the specified character.
        :param character: The character to reset.
        :param character_index: The index of the character to reset.
        """
        trace.entry()
        character.total_damage.reset()
        if self.character_damage_record.get(character_index) is not None:
            trace.flow("Reset character record window for index %s" % character_index)
            self.character_damage_record[character_index].populate_damage_record_sheet()
        trace.exit()


def main(master=None, merp_console=None, parent_console=None, character_database=None):
    """
    Starts the DamageRecordSheet window.
    :param master: The owning window.
    :param merp_console: The ancestor MERP console.
    :param parent_console: The Character Manager that started this Damage Record Sheet.
    :param character_database: The database of all active character information.
    """
    trace.init("Damage Record Sheet")
    root = Tk()
    DamageRecordSheet(master, merp_console, parent_console, character_database)
    root.mainloop()


if __name__ == '__main__':
    main()
