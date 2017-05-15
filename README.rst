
friedɀ i3pystatus
=================

My Status line Configuration using `i3pystatus<https://github.com/enkore/i3pystatus>`_ syntax is


It contains:
------------

+ `Clock<https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.clock>`_
+ `Battery<https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.battery>`_
+ `CPU Temperature<https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.temp>`_
  + Open `htop` on left click

+ `CPU Usage Bar<https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.cpu_usage_bar>`_
  + Open `htop` on left click

+ `Memory Bar<https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.mem_bar>`_
  + Open `htop` on left click

+ `Wired Network Connection<https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.network>`_
  + Toggle show IP address with left click

+ `WiFi<https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.network>`_
  + Toggle show IP address with left click

+ `MPD<https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.mpd>`_
  + Toggle Play/Pause using left mouse button
  + Open :code:`ncmpc` for current MPD Server on right mouse click
  + Open `:code:`rofi`<https://davedavenport.github.io/rofi/>`_ to select an MPD server

+ `PulseAudio Volume<https://i3pystatus.readthedocs.io/en/latest/i3pystatus.html#module-i3pystatus.pulseaudio>`_


Configuring MPD Server List
---------------------------

The configuration file is

.. code:: shell

   ~/.config/i3pystatus/mpd.toml

and the config file format is

.. code-block:: toml

   [<Name to show in rofi>]
   host = "<url/IP for the Server>"
   port = <Port of the MPD (can be left empty for 6600)>

it's really nothing special
