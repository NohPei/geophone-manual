==============================
Installing the GeoMCU Firmware
==============================


Getting the Source Code
=======================

1. Download the latest GeoMCU firmware from GitHub:
   :github:repo:`NohPei/geoscope-sensor`.
2. Ensure you have the required hardware:

   - GeoMCU board
   - a :any:`Geophone element <geophone>`
   - :any:`Power Cable <power>`
   - :any:`Serial Adapter Cable <tools>`

Building the Firmware
=====================

1. Determine the IP address of your computer (the machine that will host the
   MQTT broker):

   - Log into your router.
   - The router’s IP address is usually printed on its label (unless you use a
     custom network setup).

2. Set up your development environment. Do one of:

   - Install `Visual Studio Code <http://code.visualstudio.com/>`__ with the
     :external:doc:`integration/ide/vscode`
   - Install :external:doc:`core/index` (``pip install platformio`` is usually
     enough)
   - Install `Arduino <https://docs.arduino.cc/software/ide/>`__ and manually
     ensure the dependencies in ``platformio.ini`` are all installed

1. Build the firmware

   - :external:doc:`core/userguide/cmd_run` is the primary command for PlatformIO

.. TODO: re-factor these config instructions into the config page

3. Open the GeoMCU firmware directory you downloaded earlier, and make the
   following configuration edits.

   ``data/config/mqtt``:

   - ``clientid`` → Change from the default ``S-21`` to a unique name
   - ``ip`` → Set to the IP address of your MQTT broker (e.g., your laptop).

   .. note::

      if flashing multiple boards — each needs its own ID

   ``data/config/net``:

   - ``dns`` → IP address of your router
   - ``gateway`` → IP address of your router
   - ``ip`` → the IP address for the sensor to use
   - ``ssid`` → Name (SSID) of your Wi-Fi network
   - ``key`` → Password for your Wi-Fi network

   .. note::

      You can have the sensor get its address automatically by setting ``dns``,
      ``gateway`` and ``ip`` to ``0.0.0.0``.

      You still always need to set ``ssid`` and ``key`` to match your network.

.. _flashing:

Flashing to the PCB
===================

1. Connect the ESP8266 GeoMCU board to your computer using a USB-to-serial
   cable with the following wiring:

   +-------------------+-------------------+
   | **ESP8266 Pin**   | **USB Serial      |
   |                   | Pin**             |
   +-------------------+-------------------+
   | GND TX RX         | GND RX TX         |
   +-------------------+-------------------+

   Provide power to the GeoMCU board through the 12 V barrel jack adapter.

2. Flash the board firmware with:

   .. code:: bash

      platformio run -t upload --upload-port /dev/ttyUSB0

3. Upload the filesystem:

   .. code:: bash

      platformio run -t uploadfs --upload-port /dev/ttyUSB0

4. Verify the board is running correctly. Open a serial terminal (see
   :any:`tools`) and press Enter — you should see a prompt like ``CMD>``. You
   can also press the **Reset** button on the board to view startup messages.

   .. code:: bash

      minicom -b 115200 -D /dev/ttyUSB1

.. _flash_config:

Flashing Configuration in Bulk
==============================
