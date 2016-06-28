# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sublime
import sublime_plugin
import webbrowser

def query_selection(view, on_query):
    """ Function for querying a site using the current selection """
    for selection in view.sel():
        if not selection.empty():
            query = view.substr(selection)
            on_query(query)
        else:
            print("No selection was found.")

# MDN Queries
# ==========================
def query_mdn(query):
    url = "https://developer.mozilla.org/en-US/search?q={0}".format(query)
    webbrowser.open_new_tab(url)

class MdnSearchCommand(sublime_plugin.WindowCommand):
    """ Command for searching through MDN """
    def run(self):
        sublime.active_window().show_input_panel("MDN Search Query: ", "", query_mdn, None, None)

class MdnSearchSelectionCommand(sublime_plugin.TextCommand):
    """ Command for searching current selection through MDN """
    def run(self, edit):
        query_selection(self.view, query_mdn)

# DXR Queries
# ==========================
def query_dxr(query):
    url = "https://dxr.mozilla.org/mozilla-central/search?q={0}&redirect=false".format(query)
    webbrowser.open_new_tab(url)

class DxrSearchCommand(sublime_plugin.WindowCommand):
    """ Command for doing a code search through DXR """
    def run(self):
        sublime.active_window().show_input_panel("DXR Search Query: ", "", query_dxr, None, None)

class DxrSearchSelectionCommand(sublime_plugin.TextCommand):
    """ Command for doing a code search on current selection through DXR """
    def run(self, edit):
        query_selection(self.view, query_dxr)

# Bugzilla Queries
# ==========================
def query_bugzilla(query):
    url = "https://bugzilla.mozilla.org/buglist.cgi?quicksearch={0}".format(query)
    webbrowser.open_new_tab(url)

class BugzillaSearchCommand(sublime_plugin.WindowCommand):
    """ Command for searching through Bugzilla """
    def run(self):
        sublime.active_window().show_input_panel("Bugzilla Search Query: ", "", query_bugzilla, None, None)

class BugzillaSearchSelectionCommand(sublime_plugin.TextCommand):
    """ Command for doing a file search on the current selection through DXR """
    def run(self, edit):
        query_selection(self.view, query_bugzilla)
