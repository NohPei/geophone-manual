Creating the GeoMCU Network
---------------------------

.. _wifi:

WiFi Configuration
--------------------



.. _rpi:

Gateway Computer
--------------------

- For testing or short-term, contained use, a laptop will suffice, as long it can connect to the :any:`broker`.
- For remote or longer term deployments

.. _broker:

MQTT Broker
--------------------

:wikipedia:`MQTT Broker <MQTT#MQTT_broker>`

- We recommend :manpage:`mosquitto(8)`, and provide example configuration and service files among the :any:`/gateway/system`.
- If your WiFi AP is running `OpenWRT <https://openwrt.org/>`_, you could instead use the router or access point itself as the MQTT broker.

.. note::
   Using a public MQTT broker should be technically possible, but would require modifying the :any:`firmware </firmware/index>` to securely log into the broker.
