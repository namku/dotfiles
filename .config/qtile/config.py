# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    #Key([mod], "space", lazy.layout.next(),
    #    desc="Move window focus to other window"),
    Key([mod], 'r', lazy.spawn('rofi -show run')),
    Key([mod], 'space', lazy.spawn('rofi -show drun')),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = []

group_names = ["1", "2", "3", "4", "5", "6",]
group_labels = ["Web ", "Term ", "Files ", "Code ", "Image ", "Video ",]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])

layouts = [
    #layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_width=2,
        #border_focus="#03fce8",
        border_focus="#1881f0",
        single_border_width=0,
        margin=6,
        single_margin=0
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# COLORS FOR THE BAR
colors = [
    ["#141417", "#141417"],  # ACTIVE WORKSPACES 0
    ["#6A6A6A", "#6A6A6A"],  # INACTIVE WORKSPACES 1
    #["#384149", "#384149"],  # background lighter 2
    ["#ff0000", "#ff0000"],  # background lighter 2
    ["#FF8080", "#FF8080"],  # red 3
    ["#97D59B", "#97D59B"],  # green 4
    ["#FFFE80", "#FFFE80"],  # yellow 5
    ["#80D1FF", "#80D1FF"],  # blue 6
    ["#C780FF", "#C780FF"],  # magenta 7
    ["#80FFE4", "#80FFE4"],  # cyan 8
    ["#D5D5D5", "#D5D5D5"],  # white 9
    ["#4c566a", "#4c566a"],  # grey 10
    ["#d08770", "#d08770"],  # orange 11
    ["#8fbcbb", "#8fbcbb"],  # super cyan12
    ["#181E23", "#0E131A"],  # super blue 13
    #["#181e23", "#181e23"],  # super dark background 14
    ["#ffffff", "#ffffff"],  # super dark background 14
]

widget_defaults = dict(
    font='novamono for powerline bold',
    fontsize=12,
    padding=3,
    background=colors[14],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 1,
                    padding = 10,
                    foreground = colors[14],
                    background = colors[14]
                ),
                widget.GroupBox(font="FontAwesome",
                        fontsize = 13,
                        margin_y = 3,
                        margin_x = 2,
                        padding_y = 5,
                        padding_x = 4,
                        borderwidth = 5,
                        disable_drag = True,
                        active = colors[0],
                        inactive = colors[1],
                        rounded = True,
                        highlight_method = "block",
                        highlight_color = colors[1],
                        this_screen_border = colors[1],
                        this_current_screen_border = colors[2],
                        foreground = colors[1],
                        background = colors[14]
                ),
                widget.Spacer(),
                # orbed
                widget.TextBox(
                    text = "",
                    font = "Iosevka_Nerd_Font",
                    fontsize = 23,
                    background = colors[14],
                    foreground = colors[7],
                    padding = 0
                ),
                widget.Net(
                    background = colors[7],
                    foreground = colors[14],
                ),
                widget.TextBox(
                    text = "",
                    font = "feather",
                    fontsize = 23,
                    background = colors[7],
                    foreground = colors[14],
                    padding = 0
                ),
                # orbed
                widget.TextBox(
                    text = "",
                    font = "Iosevka_Nerd_Font",
                    fontsize = 23,
                    background = colors[14],
                    foreground = colors[6],
                    padding = 0
                ),
                widget.TextBox(
                    text = "🕓",
                    font = "feather",
                    fontsize = 15,
                    background = colors[6],
                    foreground = colors[14],
                    padding = 0
                ),
                widget.CPU(
                    background = colors[6],
                    foreground = colors[14],
                ),
                widget.TextBox(
                    text = "",
                    font = "feather",
                    fontsize = 23,
                    background = colors[6],
                    foreground = colors[14],
                    padding = 0
                ),
                # orbed
                widget.TextBox(
                    text = "",
                    font = "Iosevka_Nerd_Font",
                    fontsize = 23,
                    background = colors[14],
                    foreground = colors[5],
                    padding = 0
                ),
                widget.TextBox(
                    text = "🕓",
                    font = "feather",
                    fontsize = 15,
                    background = colors[5],
                    foreground = colors[14],
                    padding = 0
                ),
                widget.Memory(
                    background = colors[5],
                    foreground = colors[14],
                    format =' {MemUsed: .0f} MB '
                ),
                widget.TextBox(
                    text = "",
                    font = "feather",
                    fontsize = 23,
                    background = colors[5],
                    foreground = colors[14],
                    padding = 0
                ),
                # orbed
                widget.TextBox(
                    text = "",
                    font = "Iosevka_Nerd_Font",
                    fontsize = 23,
                    background = colors[14],
                    foreground = colors[4],
                    padding = 0
                ),
                widget.Systray(
                    background = colors[4],
                    foreground = colors[14],
                ),
                widget.TextBox(
                    text = "",
                    font = "feather",
                    fontsize = 23,
                    background = colors[4],
                    foreground = colors[14],
                    padding = 0
                ),
                # orbed
                widget.TextBox(
                    text = "",
                    font = "Iosevka_Nerd_Font",
                    fontsize = 23,
                    background = colors[14],
                    foreground = colors[3],
                    padding = 0
                ),
                widget.TextBox(
                    text = "🕓",
                    font = "feather",
                    fontsize = 15,
                    background = colors[3],
                    foreground = colors[14],
                    padding = 0
                ),
                widget.Clock(
                    background = colors[3],
                    foreground = colors[14],
                    icons_size = 20,
                    padding = 8
                ),
                widget.TextBox(
                    text = "",
                    font = "feather",
                    fontsize = 23,
                    background = colors[3],
                    foreground = colors[14],
                    padding = 0
                ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# Autostart programas
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
