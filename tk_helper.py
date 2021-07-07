"""
Tk utility functions.

Functions:
    clear_option_menu(selector)
    refresh_option_menu(selector_parent_widget, choices)
"""
from tkinter import _setit
from future import standard_library
import trace_log as trace

standard_library.install_aliases()


def clear_option_menu(selector):
    """
    Remove all entries from an option menu.
    :param selector: The option selector.
    """
    trace.entry()
    selector['menu'].delete(0, 'end')
    trace.exit()


def refresh_option_menu(selector, parent_widget, choices):
    """
    Refresh an option menu with new choices.
    :param selector: The option selector.
    :param parent_widget: The owning widget.
    :param choices: The choices to add to the option menu.
    """
    trace.entry()
    trace.detail("Received choices %r, type %r" % (choices, type(choices)))

    for option in choices:
        trace.flow("Add option %s to menu" % option)
        selector['menu'].add_command(label=option, command=_setit(parent_widget, option))
    trace.exit()
