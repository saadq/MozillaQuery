# MozillaQuery
> Improve your workflow when working in a Mozilla environment.

A plugin that allows you to query DXR, MDN, and Bugzilla from within Sublime.

## Installation
1. Open the Command Palette by pressing <kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Mac or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Windows
2. Type in `Package Control: Install Package` and press <kbd>Enter</kbd>
3. Type `MozillaQuery` and hit <kbd>Enter</kbd>

## Usage
1. Open up the Command Palette by pressing <kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Mac or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> on Windows
2. Type in the the command for the site you want to query (Ex: **MDN Search**) and press <kbd>Enter</kbd>
3. Enter in your query (Ex: **Arrow Functions**) and press <kbd>Enter</kbd>

## Command Palette Actions:
### Input Commands
* **MDN Search...** (command name: *mdn_search*)
* **DXR Search...** (command name: *dxr_search*)
* **DXR File Search...** (command name: *dxrf_search*)
* **Bugzilla Search...** (command name: *bugzilla_search*)

### Selection Commands
* **MDN Search Current Selection** (command name: *mdn_search_selection*)
* **DXR Search Current Selection** (command name: *dxr_search_selection*)
* **DXR File Search Current Selection** (command name: *dxrf_search_selection*)
* **Bugzilla Search Current Selection** (command name: *bugzilla_search_selection*)

## Setting up hotkeys:
1. Open up your User keybindings file (**Preferences -> Key Bindings -> User**)
2. Add an entry with the key combination you want to use as well as the name of the command

Example:

```
[
    ...
    { "keys": ["alt+m"], "command": "mdn_search" }
]
```

## License
[**MPL**](https://www.mozilla.org/en-US/MPL/2.0/)
