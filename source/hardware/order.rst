Ordering Hardware
=================

.. _exports:

Export the PCB Manufacturing Files
------------------------------------

For JLCPCB, which is what we've been using, by far the easiest way to export the needed fabrication files is using `KiKit <https://yaqwsx.github.io/KiKit/v1.4/fabrication/jlcpcb/>`_, which already happens on each GitHub release. To generate them manually, install KiKit (probably through ``pip``), then run ```kikit fab jlcpcb GeoMCU.kicad_pcb --assembly --schematic GeoMCU.kicad_sch OUTPUT_DIR/```.

KiKit `supports several other fabrication houses <https://yaqwsx.github.io/KiKit/upstream/fabrication/intro/>`_ as well, with similar ease of use.

.. _gerbers:

Gerber Files
+++++++++++++++++++++++++++

The :wikipedia:`Gerber format` files show the physical layout of the copper traces, board outlines, and drill holes for the PCB. Essentially any fabrication house will need these, though the exact export settings will vary (e.g., imperial or metric units, drill file format, etc). Check the fabrication house's website for instructions. The `KiCAD documentation <https://docs.kicad.org/8.0/en/pcbnew/pcbnew.html#generating_outputs>`_ shows the options available and how to access them from the `pcbnew` interface.
For JLCPCB (and many other fabrication houses), they `provide explicit instructions <https://jlcpcb.com/help/article/how-to-generate-gerber-and-drill-files-in-kicad-8>`_ for exporting the gerbers in the format they need.


.. _bom_cpl:

Assembly Files
+++++++++++++++++++++++++++++++++++

For pre-assembled PCBs (with components soldered by machine at the production house instead of by hand), two additional files will be needed:

- a Bill of Materials (BoM): listing the parts used with their part number and reference on the board
- a Component Placement List (CPL, sometimes called a Centroid file): listing the cordinates and rotation position of each part on the board by reference designator

For KiCAD, these two are exported differently since the BoM is only reliant on schematic information, while the CPL also requires layout information. In general, the former will come from the "Schematic Editor" (``eeschema``, through ``Tools → Generate Bill of Materials``) and the latter from the "PCB Editor" (``pcbnew``, through ``File → Fabrication Outputs → Component Placement``). Exact naming of columns and what type of part numbers are acceptable will vary depending on the PCB fabricator.
