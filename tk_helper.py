from future import standard_library
import trace_log as trace
from tkinter import _setit
standard_library.install_aliases()


def clear_option_menu(selector):
    trace.entry()
    selector['menu'].delete(0, 'end')
    trace.exit()


def refresh_option_menu(selector, parent_widget, choices):
    trace.entry()
    trace.detail("Received choices %r, type %r" % (choices, type(choices)))

    for option in choices:
        trace.flow("Add option %s to menu" % option)
        selector['menu'].add_command(label=option, command=_setit(parent_widget, option))
    trace.exit()
