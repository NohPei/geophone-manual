Installing the GeoMCU Firmware
==============================

Getting the Source Code
-----------------------

1. Download the latest GeoMCU firmware from the official documentation site:

   https://geomcu.readthedocs.io/en/latest/

2. Ensure you have the required hardware:
   - GeoMCU v2.7 board
   - Geophone sensor
   - Power cable ↔ board adapter cable


Building the Firmware
---------------------

1. Determine the IP address of your computer (the machine that will host the MQTT broker):

   - Log into your router.
   - The router’s IP address is usually printed on its label (unless you use a custom network setup).

2. Set up your development environment:

   - Install **Visual Studio Code**.
   - From the Extensions tab, install the **PlatformIO** extension.

3. Open the GeoMCU firmware directory you downloaded earlier, and make the following configuration edits.

   **In `data/config/mqtt`:**
   - ``clientid`` → Change from the default ``S-21`` to a unique name
     *(important if flashing multiple boards — each needs its own ID)*.
   - ``ip`` → Set to the IP address of your MQTT broker (e.g., your laptop).

   **In `data/config/net`:**
   - ``dns`` → IP address of your router.
   - ``gateway`` → IP address of your router.
   - ``ssid`` → Name (SSID) of your Wi-Fi network.
   - ``key`` → Password for your Wi-Fi network.

.. _flashing:

Flashing to the PCB
-------------------

1. Connect the ESP8266 GeoMCU board to your computer using a USB-to-serial cable with the following wiring:

   +-------------------+-------------------+
   | **ESP8266 Pin**   | **USB Serial Pin**|
   +-------------------+-------------------+
   | GND               | GND               |
   | TX                | RX                |
   | RX                | TX                |
   +-------------------+-------------------+

   Provide power to the GeoMCU board through the 12 V barrel jack adapter.

2. Flash the board firmware with:

   .. code-block:: bash

      platformio run -t upload --upload-port /dev/ttyUSB0

3. Upload the filesystem:

   .. code-block:: bash

      platformio run -t uploadfs --upload-port /dev/ttyUSB0

4. Verify the board is running correctly.
   Open a serial terminal (e.g., **minicom**) and press Enter — you should see a prompt like ``CMD>``.
   You can also press the **reset** button on the board to view startup messages.

   .. code-block:: bash

      minicom -b 115200 -D /dev/ttyUSB1


.. _flash_config:

Flashing Configuration in Bulk
------------------------------
