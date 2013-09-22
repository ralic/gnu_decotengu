Commandline Tools
------------------
DecoTengu library provides two commandline applications.

The ``dt-lint`` command prints dive decompression information and allows to
store dive profile steps data in a CSV file.

The ``dt-plot`` command plots dive profile steps data in the form of plots
stored in a PDF file.

Calculating Dive Decompression Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To calculate decompression information of a dive to 40m for 35 minutes on
air use the following command::

    $ dt-lint 40 35
    Dive profile:  40m for 35min
    Descent rate: 20.0m/min
    Ascent rate: 10.0m/min

    GF Low: 30%
    GF High: 85%
    Surface pressure: 1013.25 millibar

    Gas list:
     o2=21% at 0m

    Decompression stops (<decotengu.calc.ZH_L16B object at 0x7fd132205150>):
       21m   1min
       18m   1min
       15m   2min
       12m   5min
        9m   7min
        6m  14min
        3m  25min
    -------------
    Sum:    55min


The dive profile steps data can be saved using ``-f`` option. An example
of saving the data into ``dive.csv`` file::

    $ dt-lint -f dive.csv -t 60 -gl 20 -gh 90 -l '21,0@0 50,0@21 100,0@6' 40 35
    Dive profile:  40m for 35min
    Descent rate: 20.0m/min
    Ascent rate: 10.0m/min

    GF Low: 20%
    GF High: 90%
    Surface pressure: 1013.25 millibar

    Gas list:
     o2=21% at 0m
     o2=50% at 21m
     o2=100% at 6m

    Decompression stops (<decotengu.calc.ZH_L16B object at 0x7f127d87eb10>):
       24m   1min
       21m   1min
       18m   1min
       15m   1min
       12m   2min
        9m   4min
        6m   4min
        3m   8min
    -------------
    Sum:    22min

Plotting Dive Decompression Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once dive profile steps data is saved in a CSV file, the dive profile can
be plotted with ``dt-plot`` command::

    $ dt-plot dive.csv dive.pdf

The output, PDF file, contains plots for each of 16 tissues described by
Buhlmann model

- first page contains summary for each tissue
- second page has plot for leading tissue data (presented on figure
  :ref:`cmd-plot-leading-tissue`)
- next pages contain plots for each tissue

The plots show pressure value at given time of a dive. There are four lines
on the plot

blue
    Actual pressure (or in other words depth of a dive).
black
    Pressure of inert gases in a tissue.
orange
    Tissue pressure limit as implied by current gradient factor value (i.e.
    for GF low 30% and GF high 90%, gradient factor value is 30% until
    first decompression stop and it changes lineary to 90% at the surface).
red
    The maximum tissue pressure limit as required by Buhlmann model (or at
    100% gradient factor value).

.. _cmd-plot-leading-tissue:

.. figure:: dive.png

   Leading tissue data plot

.. todo:: describe plotting data of two different dives (i.e. to compare
   two different implementations of an algorithm)

.. vim: sw=4:et:ai