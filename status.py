#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# shoud i comment this?

from i3pystatus import Status
from i3pystatus import get_module
from os import environ
import toml
import subprocess

status = Status()

status.register("clock")

status.register("battery",
    format="{bar} {percentage_design:.2f}%{remaining:%E %hh:%Mm}",
    not_present_text="--",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "▼",
        "CHR": "▲",
        "FULL": "",
        "DPL":"Meh",
    },
)

status.register("temp",
    format="{temp:.0f}°C",
    on_leftclick = "urxvt -e htop",
)

status.register("cpu_usage_bar",
    bar_type="vertical",
    format="{usage_bar_cpu0}{usage_bar_cpu1}{usage_bar_cpu2}{usage_bar_cpu3} {usage_bar}",
    on_leftclick = "urxvt -e htop",
)

status.register("mem_bar",
    format="{used_mem_bar}",
    on_leftclick = "urxvt -e htop",
)

@get_module
def toggle_eth_show(self):
    longer = "{v4}<span color=\"grey\">|</span>{v6}",
    short = "E",
    if self.format_up == short:
        self.format_up = longer
    else:
        self.format_up = short

status.register("network",
    interface="eth0",
    format_up="E",
    format_down="E",
    on_leftclick = toggle_eth_show,
    on_rightclick = [],
    on_upscroll = [],
    on_downscroll = [],
    hints = {"markup": "pango"},
)

@get_module
def toggle_wlan_show(self):
    longer = "<span color=\"grey\">(</span>{essid} {quality:02}%<span color=\"grey\">) </span>{v4}<span color=\"grey\">|</span>{v6}"
    short = "{essid} {quality}%"
    if self.format_up == short:
        self.format_up = longer
    else:
        self.format_up = short

status.register("network",
    interface = "wlan0",
    format_up = "{essid} {quality}%",
    format_down = "wlan",
    on_leftclick = toggle_wlan_show,
    on_rightclick = [],
    on_upscroll = [],
    on_downscroll = [],
    hints = {"markup": "pango"},
)

@get_module
def open_ncmpc(self):
    cmd = ["urxvt", "-e", "ncmpc", "-h", "{}".format(self.host), "-p", "{}".format(self.port)]
    subprocess.Popen(cmd)

@get_module
def change_server(self):
    config = environ.get('HOME') + "/.config/i3pystatus/mpd.toml"
    with open(config) as conf:
        m = toml.load(conf)

    s = ""
    for st in list(m.keys()):
        s += st + "\n"

    cmd = ["rofi", "-dmenu", "-p", "Select MPD > ", "-l", "{}".format(len(m))]
    p = subprocess.Popen(cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    serv = p.communicate(s.encode('utf-8'))[0].decode().rstrip()
    s = m.get(serv)
    if s is not None:
        if m.get(serv).get('host') is not None:
            self.host = m.get(serv).get('host')
            if m.get(serv).get('port') is not None:
                self.port = m.get(serv).get('port')
            else:
                self.port = 6600

            self.s = None

status.register("mpd",
    format="{artist} {status} {title}",
    status={
        "pause": "▷",
        "play": "▶",
        "stop": "◾",
    },
    on_rightclick=open_ncmpc,
    on_middleclick=change_server,
)

status.register("pulseaudio",
    format="♪{volume}",
    bar_type="vertical",
    vertical_bar_width=1,
)

status.run()

# ... nope
