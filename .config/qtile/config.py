import subprocess

from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from vpn_widget import VPNWidget


mod = "mod4"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Switch focus to monitor
    Key([mod], "i", lazy.to_screen(0)),
    Key([mod], "o", lazy.to_screen(1)),
    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod], "r", lazy.spawn("kitty -e ranger")),
    Key([mod], "s", lazy.spawn("ksnip -r")),
    Key([mod], "c", lazy.spawn("galculator")),
    Key([mod], "m", lazy.spawn("magnus")),
    Key([mod], "a", lazy.spawn("pavucontrol")),
    Key([mod], "Escape", lazy.spawn("slock")),
    Key([mod, "shift"], "Escape", lazy.spawn("systemctl poweroff")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer -d 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5")),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "t", lazy.spawn("kitty -e tmux"), desc="Launch terminal"),
    Key(
        [mod],
        "v",
        lazy.spawn(
            "rofi -modi \"clipboard:/home/denis/.local/bin/greenclip print\" -show clipboard -run-command '{cmd}'"
        ),
        desc="Launch terminal",
    ),
    Key([mod], "b", lazy.spawn("blueman-manager"), desc="Launch terminal"),
    Key([mod], "g", lazy.spawn("firefox"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "x", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
    ),
    Key(
        [mod],
        "Return",
        lazy.window.toggle_floating(),
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod],
        "p",
        lazy.spawn("rofi -show drun -location 0 -monitor -1"),
        desc="Launch rofi application launcher",
    ),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
            ),
        ]
    )

layouts = [
    layout.Max(margin=15),
    layout.MonadTall(margin=15, border_focus="#78cff2"),
]

widget_defaults = dict(
    font="sans",
    fontsize=20,
    foreground="#88C0D0",
    padding=4,
)
extension_defaults = widget_defaults.copy()


bar = bar.Bar(
    [
        widget.GroupBox(
            active="#A3BE8C",
            this_current_screen_border="#81A1C1",
            disable_drag=True,
        ),
        widget.WindowName(),
        widget.Volume(
            fmt="Volume {}",
            volume_app="pamixer",
            get_volume_command="pamixer --get-volume-human",
            emoji=False,
        ),
        widget.Battery(
            format="Battery {percent:2.0%}",
        ),
        widget.Wlan(
            format="WLAN {percent:2.0%}",
            interface="wlp2s0",
            use_ethernet=True,
            update_interval=10,
        ),
        VPNWidget(),
        widget.Sep(),
        widget.CheckUpdates(
            distro="Void",
            initial_text="Checking updates...",
            colour_have_updates="#88C0D0",
            colour_no_updates="#88C0D0",
            display_format="Updates {updates}",
            no_update_string="No updates",
            update_interval=600,
        ),
        widget.Sep(),
        widget.Bluetooth(),
        widget.Sep(),
        widget.Clock(format="%Y-%m-%d %A %H:%M:%S"),
    ],
    36,
    border_color="#282738",
    border_width=[0, 0, 0, 0],
    margin=[6, 60, 0, 60],
    background="#2E3440",
)

screens = [
    Screen(top=bar),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
    border_focus="#ffffff",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="galculator"),  # GPG key password entry
        Match(title="Bluetooth Devices"),
        Match(title="Volume Control"),
        Match(title="Screen Layout Editor"),
        Match(title="Magnus"),
    ],
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False

@hook.subscribe.startup
def set_keyboard_layout():
    subprocess.run(["setxkbmap", "-option", "ctrl:swapcaps"])
