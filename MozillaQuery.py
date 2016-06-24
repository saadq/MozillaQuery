# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sublime
import sublime_plugin
import webbrowser

# MDN Queries
def query_mdn(query):
    url = "https://developer.mozilla.org/en-US/search?q={0}".format(query)
    webbrowser.open_new_tab(url)

class MdnSearchCommand(sublime_plugin.ApplicationCommand):
    """ Command for searching through MDN """
    def run(self):
        text = "MDN Search Query:"
        sublime.active_window().show_input_panel(text, "", query_mdn, None, None)

class MdnSearchSelectionCommand(sublime_plugin.TextCommand):
    """ Command for searching current selection through MDN """
    def run(self, edit):
        for selection in self.view.sel():
            if not selection.empty():
                query = self.view.substr(selection)
                query_mdn(query)
            else:
                print("No selection was found.")

# DXR Queries
def query_dxr(query):
    url = "https://dxr.mozilla.org/mozilla-central/search?q={0}&redirect=false".format(query)
    webbrowser.open_new_tab(url)

class DxrSearchCommand(sublime_plugin.ApplicationCommand):
    """ Command for doing a code search through DXR """
    def run(self):
        text = "DXR Search Query:"
        sublime.active_window().show_input_panel(text, "", query_dxr, None, None)

class DxrSearchSelectionCommand(sublime_plugin.TextCommand):
    """ Command for doing a code search on current selection through DXR """
    def run(self, edit):
        for selection in self.view.sel():
            if not selection.empty():
                query = self.view.substr(selection)
                query_dxr(query)
            else:
                print("No selection was found.")

# DXR File Queries
def file_query_dxr(query):
    url = "https://dxr.mozilla.org/mozilla-central/search?q=file:{0}&redirect=false".format(query)
    webbrowser.open_new_tab(url)

class DxrfSearchCommand(sublime_plugin.ApplicationCommand):
    """ Command for doing a file search through DXR """
    def run(self):
        text = "DXR File Search Query:"
        sublime.active_window().show_input_panel(text, "", query_dxr, None, None)

class DxrfSearchSelectionCommand(sublime_plugin.TextCommand):
    """ Command for doing a file search on the current selection through DXR """
    def run(self, edit):
        for selection in self.view.sel():
            if not selection.empty():
                query = self.view.substr(selection)
                file_query_dxr(query)
            else:
                print("No selection was found.")

# Bugzilla Queries
def query_bugzilla(query):
    url = "https://bugzilla.mozilla.org/buglist.cgi?quicksearch={0}".format(query)
    webbrowser.open_new_tab(url)

class BugzillaSearchCommand(sublime_plugin.ApplicationCommand):
    """ Command for searching through Bugzilla """
    def run(self):
        text = "Bugzilla Search Query: "
        sublime.active_window().show_input_panel(text, "", query_bugzilla, None, None)

class BugzillaSearchSelectionCommand(sublime_plugin.TextCommand):
    """ Command for doing a file search on the current selection through DXR """
    def run(self, edit):
        for selection in self.view.sel():
            if not selection.empty():
                query = self.view.substr(selection)
                query_bugzilla(query)
            else:
                print("No selection was found.")
