Testing the GeoMCU Hardware
===========================

Tools Needed
++++++++++++++
1. multimeter (To check voltages)
2. scope (we are using analog discovery pro 3000 series)
(obviously) the board
usb-to-serial cable
putty installed (That is the easiest way to check and communicate via the serial terminal)
power: 12v barrell jack with adapter to (...same connecters written elsewhere )

Individual PCB Testing
+++++++++++++++++++++++++
1) voltage checks (esp should breifly flash blue when you power the board -- if it doesn't then don't continue)
agnd, dgnd, should be 0, 12v should be whatever is coming in 
5v is the switching (should be around 5v)
3.3v is for everything

analog check voltage reference (agnd, 3.3 ref, 1.65ref)

amp is amplifier, pin to right of geophone is that pin
inside center pin of connector should be output going to ADC 

2) dynamic checks (flash the board first, set it up then test this)
simple check: connect via usb-to-serial to the board, 'adc dump' command and tap geophone to see data changes

testing gain: (analog discovery) wave generator and a scope to see where it clips
- use Putty to connect to the board via serial 
- in the serial terminal you can set the gain with 'gain 10' where that is what you can set
- you can run 'gain gain' to check the gain of the board (checking the math pretty much behind the scenes)

(( on laptop: Users\Julia\geoMCU-board-testing this is the saved waveform workspace))
A grade board vs. B grade board
A grade board won't have clipping until the gain gets super higher
B grade board would show unstable/clipping when the gain is lower (i.e. from 10 to 12)


this would be the end of board testing if you have a good board, otherwise other things would need to happen...
(v2.7 is used for this; v2.9 requires you set the gain to even use the board...we assume nothing with that version and test everything then set the gain)

Power Supplies Check
--------------------


Flash Firmware
--------------

Follow the instructions for :any:`flashing` to get the firmware running on the sensor board.

Gain Checking
--------------
1. In PuTTy, after verifying you are able to see data, you will want to run 'adc' to enable the gain testing mode 
- at any point, if you are unsure what command to run, type 'help' into the terminal

.. note::

        For a quick check if the board is correctly collecting vibrations:
                1. connect a geophone to the board
                2. shake the geophone or tap on it while monitoring any of:
                        * the MQTT data (which requires the :any:`broker` and the on-board ADC to work)
                        * the wired output (requires an oscilloscope)
                        * the output from ``adc dump`` (which just relies on a serial power and the on-board ADC)

        It should be fairly obvious if the geophone's signal is being measured
        or not since it should swing wildly between its maximum and minimum
        values while the geophone is shaken.



Networked Geophone Testing
++++++++++++++++++++++++++++++
