
# friedɀ i3pystatus

My Status line Configuration using [i3pystatus](https://github.com/enkore/i3pystatus) syntax is


## It contains:

+ [Clock](https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.clock)
+ [Battery](https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.battery)
+ [CPU Temperature](https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.temp)
  + Open `htop` on left click

+ [CPU Usage Bar](https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.cpu_usage_bar)
  + Open `htop` on left click

+ [Memory Bar](https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.mem_ba)
  + Open `htop` on left click

+ [Wired Network Connection](https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.network)
  + Toggle show IP address with left click

+ [WiFi](https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.network)
  + Toggle show IP address with left click

+ [MPD](https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.mpd)
  + Toggle Play/Pause using left mouse button
  + Open `ncmpc` for current MPD Server on right mouse click
  + Open [`rofi`](https://davedavenport.github.io/rofi/) to select an MPD server

+ [PulseAudio Volume](https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.pulseaudio)


## Configuring MPD Server List

The configuration file is

```shell
~/.config/i3pystatus/mpd.toml
```

and the config file format is [toml](https://github.com/toml-lang/toml)

```toml
[<Name to show in rofi>]
host = "<URL or IP>"
port = <Port>
```
port can be left out for the standart port (`6600`)

it's really nothing special
