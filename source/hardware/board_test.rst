Testing the GeoMCU Hardware
===========================

Tools Needed
++++++++++++++

The following tools are needed to test the GeoMCU hardware:
to test the PCB itself:
- An oscilloscope
- An function generator
- A 12v power supply
- A computer
to test with sensor data:
- An :any:`MQTT broker <network:broker>` or a computer running the :any:`gateway/index`
- A geophone

Individual PCB Testing
+++++++++++++++++++++++++

1. Connect 12v power to the board.
2. use the function generator to generate a 100hz sine wave at 0.5vpp.



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
