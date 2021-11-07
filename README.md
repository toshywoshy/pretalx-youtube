YouTube integration
====================

This is a plugin for `pretalx`.

Development setup
------------------

1. Make sure that you have a working `pretalx development setup`.

2. Clone this repository, eg to ``local/pretalx-youtube``.

3. Activate the virtual environment you use for pretalx development.

4. Execute ``python3 setup.py develop`` within this directory to register this application with pretalx's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretalx server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.


License
-------

Copyright 2021 Toshaan Bharvani

Released under the terms of the Apache License 2.0
