# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sublime
import sublime_plugin
import webbrowser

class MdnSearchCommand(sublime_plugin.ApplicationCommand):
    """ Command for searching through MDN """
    def run(self):
        text = "MDN Search Query:"
        sublime.active_window().show_input_panel(text, "", self.on_query, None, None)

    def on_query(self, query):
        url = "https://developer.mozilla.org/en-US/search?q={0}".format(query)
        webbrowser.open_new_tab(url)

class DxrSearchCommand(sublime_plugin.ApplicationCommand):
    """ Command for doing a code search through DXR """
    def run(self):
        text = "DXR Search Query:"
        sublime.active_window().show_input_panel(text, "", self.on_query, None, None)

    def on_query(self, query):
        url = "https://dxr.mozilla.org/mozilla-central/search?q={0}&redirect=false".format(query)
        webbrowser.open_new_tab(url)

class DxrfSearchCommand(sublime_plugin.ApplicationCommand):
    """ Command for doing a file search through DXR """
    def run(self):
        text = "DXR File Search Query:"
        sublime.active_window().show_input_panel(text, "", self.on_query, None, None)

    def on_query(self, query):
        url = "https://dxr.mozilla.org/mozilla-central/search?q=file:{0}&redirect=false".format(query)
        webbrowser.open_new_tab(url)

class BugzillaSearchCommand(sublime_plugin.ApplicationCommand):
    """ Command for searching through Bugzilla """
    def run(self):
        text = "Bugzilla Search Query: "
        sublime.active_window().show_input_panel(text, "", self.on_query, None, None)

    def on_query(self, query):
        url = "https://bugzilla.mozilla.org/buglist.cgi?quicksearch={0}".format(query)
        webbrowser.open_new_tab(url)
