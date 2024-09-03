Getting Started
===================================

PCB Assembly
--------------------------------------------------

The first step to using a **GeoMCU** system is getting the boards fabricated and assembled.

In general, we've been using `JLCPCB <https://jlcpcb.com/>`_ for this, balancing time and cost.
However, any :abbr:`PCB (Printed Circuit Board` fabrication house should work, as long as they can create 4 layer boards.
This manual will proceed assuming our existing `KiCad <https://www.kicad.org/>`_ design files and ordering from `JLCPCB <https://jlcpcb.com/>`_

.. note::

        Switching PCB fabricators may require adjusting the board design to account for the new manufacturer's design rules.

The basic process for this is:

#. :any:`gerbers`
#. Get the :abbr:`BoM (Bill of Materials` and placement files (see :any:`bom_cpl`)
#. Place the order with the :abbr:`PCB (Printer Circuit Board)` fabrication house (see :any:`order`)
#. Solder the missing signal output connector, if using :any:`wired`.

After that, it's time for :any:`hardware/board_test`.

See :any:`hardware/order` for more details.


.. _usage_components:

Auxiliary Components
----------------------------------------

The supporting components needed depend on which :any:`configuration <hardware/configurations>` is in use.
All configurations will require, for each :abbr:`PCB (Printed Circuit Board)`

- One :any:`SM-24 Geophone <geophone>`
- 2x modular latching connectors compatible with `Molex SL <https://www.molex.com/en-us/products/part-detail/50579402>`_

        - There are `many <https://octopart.com/ci3302s0010-cvilux-28558780>`_ `compatible <https://www.te.com/en/product-104257-1.html>`_ `alternatives <https://www.digikey.com/short/7wf5508w>`_ to choose from.
        - One of these will connect the geophone to the :abbr:`PCB (Printed Circuit Board)`, the other will connect power to it.
        - You'll need to assemble these connectors as well, which usually involves `crimping contancts onto wires then inserting them into the housings <https://youtu.be/N_EG7beupek?si=WxPDgEj34tAt2yVy>`_.

- Some form of :any:`power`

Additionally, all configurations, even :any:`wired`, will need a minimal network setup:

- a WiFi network operating in the 2.4 GHz band, which can be secured by at most :wikipedia:`WPA2`-PSK.

        - The `ESP8266 <https://www.espressif.com/en/products/socs/esp8266>`_ microcontrollers on the :abbr:`PCB` cannot handle a :wikipedia:`Captive portal` or any form of :wikipedia:`WPA-Enterprise` and communicate in :wikipedia:`Cleartext`, so we recommend running them in an isolated network. See :any:`hardware/network` for suggestions of how to do this.
- A PC (preferably running some kind of Linux) running an :any:`broker`

- a PC (again, preferably running Linux. Can be on the same machine as the broker) running the :any:`gateway/index`


Check the :any:`configuration <hardware/configurations>` in use for other needed components, including which :any:`tools` are necessary.


Firmware Setup
------------------------

With :abbr:`PCB` in-hand and components ready, we need to upload the :any:`firmware/index` to the boards, as well as :any:`configure <firmware/config>` them for the local network.

For instructions, see :doc:`firmware/build`. As a short summary, you'll need to:

#. Get the source code from GitHub: :github:repo:`NohPei/geoscope-sensor`.
#. Compile it with :external:doc:`PlatformIO <what-is-platformio>` or `Arduino <https://docs.arduino.cc/software/ide/>`_
#. :any:`Flash it <flashing>` to the :abbr:`PCB`
#. Configure the sensor, either over the serial port/telnet (see :doc:`firmware/config`), or by :any:`flash_config`

Gateway and Networking Setup
------------------------------

To use or test the GeoMCU sensors, you'll need to :doc:`create the GeoMCU network <hardware/network>`, consisting of:

- a 2.4 GHz WiFi network
- the :any:`broker`
- the :any:`rpi`

GeoMCU Testing
---------------

When setting up with new hardware (or after an incident which could damage the PCB), it's a good idea to :doc:`test your boards <hardware/board_test>` before collecting vibration data.
It's also helpful to test the network by checking, for example:

- if data is being saved on the :any:`rpi` by the :doc:`gateway/index`
- if the vibration data appears as expected. You can use :github:repo:`NohPei/GeoMCU_plotter` to visualize the incoming MQTT packets to help with this

        - An oscilloscope can also be used to inspect the PCB's output from the center pin of the BNC connector, particularly useful if the MQTT data is suspect.
