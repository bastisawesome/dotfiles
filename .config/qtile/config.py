# TODO: Add more matches to 'WWW' Group for all web browsers
import autostart
import copy
from libqtile import (
    bar,
    layout,
    widget,
)
from libqtile.config import (
    EzKey as Key,
    Group,
    Match,
    Screen,
)
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import Any


#************************
# Configuration Variables
#************************

mod = "mod4"
terminal = 'alacritty'
editor = 'emacsclient -a "nvim" -c'

#***************
# Lazy Functions
#***************

#*******
# Groups
#*******

groups: list[Group] = [
    Group(
        '1',
        label='GEN'
    ),
    Group(
        '2',
        label='WWW',
        matches=[
            Match(wm_class=['Chromium'])
        ]
    ),
    Group(
        '3',
        label='DEV'
    )
]

#************
# Keybindings
#************

modifier_keys = {
    'M': 'mod4',        # Super
    'A': 'mod1',        # Alt
    'S': 'shift',       # Shift
    'C': 'control',     # Control
}

keys = [
    # General Qtile Bindings
    Key('M-r', lazy.reload_config()),
    Key('M-C-r', lazy.restart()),
    Key('M-<Return>', lazy.spawncmd()),
    Key('M-<space>', lazy.spawn(guess_terminal())),

    # Window Management Bindings
    ## Move between windows
    Key('M-h', lazy.layout.left()),
    Key('M-j', lazy.layout.down()),
    Key('M-k', lazy.layout.up()),
    Key('M-l', lazy.layout.right()),

    ## Move Windows around
    Key('M-S-h', lazy.layout.shuffle_left()),
    Key('M-S-j', lazy.layout.shuffle_down()),
    Key('M-S-k', lazy.layout.shuffle_up()),
    Key('M-S-l', lazy.layout.shuffle_right()),

    ## Grow/Shrink Windows
    Key('M-C-h', lazy.layout.grow_left()),
    Key('M-C-j', lazy.layout.grow_up()),
    Key('M-C-k', lazy.layout.grow_down()),
    Key('M-C-l', lazy.layout.grow_right()),

    ## Cycle through layouts
    Key('M-<Tab>', lazy.layout.next_layout()),
    Key('M-S-<Tab>', lazy.layout.prev_layout()),

    # Emacs
    Key('M-e', lazy.spawn(editor)),
]

# Group keybindings
for i in groups:
    keys.extend(
        [
            Key(f'M-{i.name}', lazy.group[i.name].toscreen()),
            Key(f'M-S-{i.name}', lazy.window.togroup(i.name, switch_group=True))
        ]
    )

#********
# Layouts
#********

#******
# Mouse
#******

#********
# Screens
#********

customBar = bar.Bar(
    [
        widget.GroupBox(),
        widget.CurrentLayoutIcon(),
        widget.WindowName(),
        widget.Prompt(),
        widget.Spacer(bar.STRETCH),
        widget.StatusNotifier(),
        widget.Volume(
            emoji=True
        ),
        widget.Clock(format='%H:%M %d/%m/%Y'),
        widget.Spacer(10)
    ],
    size=30
)

customBar2 = bar.Bar(
    [
        widget.GroupBox(),
        widget.CurrentLayoutIcon(),
        widget.WindowName(),
        widget.Prompt(),
        widget.Spacer(bar.STRETCH),
        widget.StatusNotifier(),
        widget.Volume(
            emoji=True
        ),
        widget.Clock(format='%H:%M %d/%m/%Y'),
        widget.Spacer(10)
    ],
    size=30
)

screens = [
    Screen(
        top = customBar
    ),
    Screen(
        top = customBar2
    )
]
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
floating_layout = layout.Floating(
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
