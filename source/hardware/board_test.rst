===========================
Testing the GeoMCU Hardware
===========================


Tools Needed
============

1. Multimeter (to check voltages)
2. Oscilloscope and Waveform Generator (we typically use an `Analog
   Discovery <https://digilent.com/reference/test-and-measurement/>`__ for
   both)
3. The GeoMCU board
4. USB-to-serial cable
5. serial terminal software installed (to communicate via the serial terminal)
6. Power supply: 12V jack with adapter

Individual PCB Testing
======================

.. note::

   Version 2.7 boards are tested as described here. Version 2.9 boards will
   **require the gain to be set** before use, so modify this process
   accordingly.

1. **Voltage Checks**

   - The ESP should briefly flash blue when powered on. If it does **not**, do
     **not** continue testing.
   - ``AGND`` and ``DGND`` should both be 0 V.
   - ``12V`` should read whatever voltage is supplied.
   - ``5V`` is the switching line (should measure around 5 V).
   - ``3.3V`` powers most logic components.

   Check the analog reference voltages as well:

   - ``AGND``, ``3.3 V REF``, and ``1.65 V REF``.

2. **Amplifier Check:**

   - The pin to the right of the geophone connector is the amplifier input
     (labeled ``AMP``)
   - The inner center pin of the connector should be the **output** going to
     the ADC.

3. **Dynamic Checks**

   (Performed after :any:`flashing the firmware <flashing>` and initial setting
   up the board.)

   - Connect to the board via USB-to-serial.
   - Run the ``adc dump`` command in the serial terminal.
   - Tap the geophone and observe data changes.

4. **Testing Gain:**

   Use the Analog Discovery’s wave generator and scope to observe where the
   signal clips.

   Steps:

   - Connect to the board over serial.
   - Set the gain using e.g., ``gain 10`` (replace *10* with your desired
     value).
   - Check the configured gain using ``gain`` without a number — this verifies
     the math behind the gain setting.


Board Grading
-------------

- Hardware bugs with the v2.7 boards make them unstable at high gain values
  depending on part tolerances. So, we separate them into two grades:

     - **A-Grade** boards will not clip until very high gain values.
     - **B-Grade** boards show instability or clipping at relatively lower gain
       (e.g., 10–12).



If your board passes all of the above, testing is complete. Otherwise, further
debugging may be required.


Power Supplies Check
--------------------

.. TODO: reference or add the power testing instructions here

*(Insert power rail verification steps or table here, if available.)*


Flash Firmware
--------------

Follow the instructions in :any:`flashing` to install and run the firmware on
the sensor board.

Gain Checking
-------------

1. In your serial terminal, after confirming that you can view data, enter the
   ``adc`` command to switch to the ADC configuration menu
2. If you are unsure about available commands at any point, type ``help`` in
   the terminal.

.. note::

   **Quick Functional Check**

   To quickly verify vibration sensing:

   1. Connect a geophone to the board.
   2. Shake or tap the geophone while monitoring one of the following:

      - MQTT data (requires the :any:`broker` and the on-board ADC)
      - Wired analog output (requires an oscilloscope)
      - Output from ``adc dump`` (requires only serial connection and the
        on-board ADC)

   The signal should vary significantly (swinging between min and max values)
   when the geophone is moved. If the output remains flat, the board is not
   properly sensing vibrations.

Networked Geophone Testing
==========================

*(Add procedures for multi-node or MQTT-based geophone testing here.)*
