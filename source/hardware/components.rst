===============
Auxiliary Parts
===============


.. _power:

Power Supply
============

.. _geophone:

Geophones
=========

similar performance to the `SM-24 <https://www.sparkfun.com/products/11744>`__
units we've been using

.. _box:

Housings
========

The boards are designed to fit a Bud Industries
`PN-1323 <https://www.budind.com/product/nema-ip-rated-boxes/pn-series-nema-box/ip65-nema-4x-box-pn-1323/>`__
Enclosure. For ease of mounting we recommend the
`PN-1323-MB <https://www.budind.com/product/nema-ip-rated-boxes/pn-series-nema-box/ip65-nema-4x-box-with-mounting-brackets-pn-1323-mb/>`__
or
`PN-1323-CMB <https://www.budind.com/product/nema-ip-rated-boxes/pn-series-nema-box/ip65-nema-4x-box-with-clear-cover-and-mounting-brackets-pn-1323-cmb/>`__
variations, the latter of which has a transparent lid that can help with
troubleshooting.

Connectors
==========

Networking
==========

See :any:`network`

.. _tools:

Assembly Tools
==============

For configuring and flashing the micontroller:

- 1x 3.3 V Serial Port adapter (UART). We recommend `these ones from
  Amazon <https://www.amazon.com/dp/B07WX2DSVB>`__.

- Serial terminal software for communicating with the board over serial port

     - On Windows this is usually :wikipedia:`PuTTY` or :wikipedia:`TeraTerm`
     - :manpage:`minicom` and :manpage:`picocom` are common examples for Linux and Mac
     - Once you have :external:doc:`PlatformIO <core/index>` set up, you can
       use :external:doc:`core/userguide/device/cmd_monitor` or
       :external:doc:`core/userguide/cmd_run` with ``target=monitor`` as your
       serial terminal
