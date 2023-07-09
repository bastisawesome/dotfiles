import autostart
from libqtile import layout
from libqtile.config import Match
from typing import Any

#************************
# Configuration Variables
#************************
mod = "mod4"
terminal = 'alacritty'

#*************
# Lazy Objects
#*************

#************
# Keybindings
#************

#********
# Layouts
#********

#******
# Mouse
#******

#********
# Screens
#********

#******
# Hooks
#******

#****************
# QTile Variables
#****************

# Allow windows to make themselves full screen
auto_fullscreen = True

# Bring window forward when clicked if the window is floating.
bring_front_click = 'floating_only'

# Disable cursor following the active window
cursor_warp = False

# Do not create group binding hotkeys
dgroups_key_binder = None

# Do not create Rule objects for groups
dgroups_app_rules: list[Any] = []

# Default settings for extensions
extension_defaults = dict(font='sans', fontsize=12, padding=2)

# Default floating window layout
floating_layout = floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# Prevent applications like DISCORD from stealing passwords.
# (Never automatically focus any window on request)
focus_on_window_activation = 'never'

# Allow the mouse to activate windows
follow_mouse_focus = True

# Default settings for bar widgets
widget_defaults = dict(font='sans', fontsize=12, padding=2)

# Reconfigure screens when RandR updates
reconfigure_screens = True

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# PREVENT PC BUILDING SIMULATOR FROM BEING TRASH!
auto_minimize = False
