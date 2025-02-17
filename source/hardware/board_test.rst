Testing the GeoMCU Hardware
===========================

Tools Needed
++++++++++++++

Individual PCB Testing
+++++++++++++++++++++++++

Power Supplies Check
--------------------

Flash Firmware
--------------

Follow the instructions for :any:`flashing` to get the firmware running on the sensor board.

Gain Checking
--------------


.. note::

        For a quick check if the board is correctly collecting vibrations:
                1. connect a geophone to the board
                2. shake the geophone or tap on it while monitoring any of:
                        * the MQTT data (which requires the :any:`broker` and the on-board ADC to work)
                        * the wired output (requires an oscilloscope)
                        * the output from ``adc dump`` (which just relies on a serial power and the on-board ADC)

        It should be fairly obvious if the geophone's signal is being measured
        or not since it should swing wildly between its maximum and minimum
        values while the geohpone is shaken.



Networked Geophone Testing
++++++++++++++++++++++++++++++
