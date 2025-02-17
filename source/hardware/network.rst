Creating the GeoMCU Network
============================

.. _wifi:

WiFi Configuration
--------------------

The GeoMCU board is based on an :wikipedia:`ESP8266`, which gives us a few requirements for the WiFi network the sensors will connect to:

- Only 2.4 GHz WiFi can be used. The chip is compatible up to :wikipedia:`Wi-Fi 4/802.11n <802.11n>`, but can still connect to a newer access point since they're backwards compatible.
- The Arduino-based software can connect to :wikipedia:`WPA2`-secured networks or lower, but is *NOT* compatible with :wikipedia:`WPA3`

Because of these two requirements, most University networks will *NOT* work directly, and you will most likely need to manually configure the router or access point. We most commonly use one of:

- `GL-iNet GL-B1300 <https://www.gl-inet.com/products/gl-b1300/>`_
- `GL-iNet GL-A1300 <https://www.gl-inet.com/products/gl-a1300/>`_

for compatibility and configurability, but any :wikipedia:`Wi-Fi 4` router should work. Just make sure to manually configure a 2.4 GHz network with a password using at most :wikipedia:`WPA2` security. The :wikipedia:`SSID` and password need to be set in the :any:`firmware configuration </firmware/config>`.


.. _rpi:

Gateway Computer
--------------------

- For testing or short-term, contained use, a laptop will suffice, as long it can connect to the :any:`broker`.
- For remote or longer term deployments, we usually use an embedded :wikipedia:`Single-Board Computer`, such as as a `Raspberry Pi <https://raspberrypi.com>`_.

Recommended SBCs
+++++++++++++++++

- Raspberry Pi `3 <https://www.raspberrypi.com/products/raspberry-pi-3-model-b-plus/>`_, `4 <https://www.raspberrypi.com/products/raspberry-pi-4-model-b/>`_, or `5 <https://www.raspberrypi.com/products/raspberry-pi-5/>`_
        - The community around these is very large, so it's generally easy to find help when you run into problems
        - The Pi5 is very new (as of 2024) and much more powerful than the 3 or 4, with the same tradeoffs as the Rock4.
- Radxa `Rock4 <https://wiki.radxa.com/Rockpi4>`_
        - This board has a more robust processor than the RPi 3 or 4, and the added benefit of an :wikipedia:`NVMe` slot for SSDs. However, it does consequently consume more power and put out even more heat.
- Olimex `A20-OLinuXino-Lime2 <https://www.olimex.com/Products/OLinuXino/A20/A20-OLinuXino-LIME2/open-source-hardware>`_
        - This board is very low-powered, but has an on-board :wikipedia:`SATA` port for a hard drive or SSD. Sometimes will struggle with memory usage or processing power with a large number of sensors (>30) and/or when archiving sensor data. That said, it's also battle-tested and out-of-the-box compatible with just about any flavor of Linux you can think of, which leads to more stability compared with most SBCs.


.. _broker:

MQTT Broker
--------------------

You'll need an :wikipedia:`MQTT Broker <MQTT#MQTT_broker>` for the sensor nodes and the :any:`/gateway/index` to connect to. As long as all of the sensors and the aggregator software can connect to it, data will flow wirelessly. This is technically optional when using :any:`wired`, but we recommend keeping at least the sensors connected even this case for stability and easier configuration.

- We recommend :manpage:`mosquitto(8)`, and provide example configuration and service files among the :any:`/gateway/system`.
- If your WiFi AP is running `OpenWRT <https://openwrt.org/>`_, you could instead use the router or access point itself as the MQTT broker.

.. note::
   Using a public MQTT broker should be technically possible, but would require modifying the :any:`firmware </firmware/index>` to securely log into the broker.
