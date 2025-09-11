Installing the GeoMCU Firmware
=================================================


Getting the Source Code
----------------------------------------

The source code is available on GitHub: 
`geoscope-sensor <https://github.com/NohPei/geoscope-sensor>`_

Building the Firmware
----------------------------------------

We recommend using `PlatformIO <https://platformio.org/>`_ to build and flash the GeoMCU firmware. PlatformIO is a powerful open-source ecosystem for embedded development, supporting a wide range of boards and microcontrollers.

Common PlatformIO commands:

- **Build the firmware:**
  .. code-block:: bash

      pio run

- **Build and upload (flash) the firmware to the board:**
  .. code-block:: bash

      pio run --target upload

- **List available boards:**
  .. code-block:: bash

      pio boards

- **List available devices (such as USB serial ports):**
  .. code-block:: bash

      pio device list

For installation instructions and more details, please refer to the `PlatformIO documentation <https://platformio.org/>`_.


.. _flashing:

Flashing to the PCB
----------------------------------------

The following PlatformIO commands are commonly used (commands already listed above, such as `pio run` and `pio run -t upload`, are omitted here):

**Flash the config folder:**
.. code-block:: bash

    pio run -t uploadfs

**Open serial monitor:**
.. code-block:: bash

    pio run -t monitor

.. note::

    For `upload` and `uploadfs`, you may need to specify the upload port:
    
    - Windows: ``--upload-port COM3`` (replace COM3 with your actual port)
    - Linux/Mac: ``--upload-port /dev/ttyUSB0`` (replace with your actual device)

**Telnet connection:**
.. code-block:: bash

    nc -t SENSOR_ADDRESS 23

TODO: add the default SENSOR_ADDRESS and file setting

.. _flash_config:

Flashing Configuration in Bulk
--------------------------------------------------
