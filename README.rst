Channel Archive Config Generator
--------------------------------

Command line utility to generate config files for the
`EPICS Channel Archiver <https://github.com/EPICSTools/ChannelArchiver>`_.

.. image:: https://travis-ci.org/AustralianSynchrotron/archive-config-generator.svg?branch=master
   :target: https://travis-ci.org/AustralianSynchrotron/archive-config-generator
   :alt: Build Status


Usage
-----

Define a text file where each line contains:

* the PV name
* the monitor type (``scan`` or ``monitor``)
* the scan period / expected monitor update period

For example::

    SR03ID01:FLUX_MONITOR       monitor   1
    SR03ID01:PRESSURE_MONITOR   scan      60
    # comments and blank lines are ignored
    # placeholder labels can be added in parentheses:
    {prefix}:SETPOINT           scan      {slow}


Then run::

    archive-config-generator --group-name MyArchive \
                             --substitutions prefix=MTR01,slow=3600 example.txt

The ouput, which should be stored as `engineconfig.xml` on your archiver host
will look like:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!DOCTYPE engineconfig SYSTEM "engineconfig.dtd">
    <engineconfig>
      <buffer_reserve>3</buffer_reserve>
      <file_size>500</file_size>
      <get_threshold>20</get_threshold>
      <ignored_future>1</ignored_future>
      <max_repeat_count>120</max_repeat_count>
      <write_period>30</write_period>
      <group>
        <name>MyArchive</name>
        <channel>
          <name>SR03ID01:FLUX_MONITOR</name>
          <monitor/>
          <period>1</period>
        </channel>
        <channel>
          <name>SR03ID01:PRESSURE_MONITOR</name>
          <scan/>
          <period>60</period>
        </channel>
        <channel>
          <name>MTR01:SETPOINT</name>
          <scan/>
          <period>3600</period>
        </channel>
      </group>
    </engineconfig>
