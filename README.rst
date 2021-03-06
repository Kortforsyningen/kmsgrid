###############################################################################
                                  kmsgrid
###############################################################################

``kmsgrid`` is a small utility that makes it easy to work with the various
datum 
`grid files <ftp://ftp.sdfe.dk/download/transformationsprogram/Geoids2013.zip>`_
made by KMS/DTU for the transformation library TrLib (KMSTrans).


Using kmsgrid
===============================================================================

``kmsgrid`` is both a Python module and a command line utility.


Command line
-------------------------------------------------------------------------------

The ``kmsgrid`` command line utility comprises two sub-utilities: "info"
and "translate".

::

    $ kmsgrid --help
    usage: kmsgrid [-h] {translate,info,help} ...

    Read binary grid files from trlib.

    optional arguments:
      -h, --help            show this help message and exit

    Subcommands:
      Valid subcommands

      {translate,info,help}
                            additional help

Info
...............................................................................

The ``info`` sub-command is used for getting information about a grid.
Information can be queried about a single point, or about the entire file.
::

    $ kmsgrid info --help
    usage: kmsgrid info [-h] [--datum] [--mode] [--point I J] grid

    positional arguments:
      grid         Binary grid file.

    optional arguments:
      -h, --help   show this help message and exit
      --point I J  Value(s) at a grid index (I,J). Prints values from all
                   dimensions of the grid.


Get information about a 3D grid::

  $ kmsgrid info nkgrf03vel.01
        filename:  nkgrf03vel.01
      dimensions:  3
          latmin:  53.0
          latmax:  73.0
          lonmin:  3.0
          lonmax:  40.0
     data[0].min:  -0.96
     data[0].max:  1.75
    data[0].mean:  0.204704
     data[1].min:  -1.65
     data[1].max:  0.86
    data[1].mean:  -0.194318
     data[2].min:  -0.72
     data[2].max:  9.97
    data[2].mean:  2.34521
            dlat:  0.0833333333333
            dlon:  0.166666666667
            nlat:  241
            nlon:  223
           datum:  ITRF19yy/20yy
            mode:  KMSGrid
       tabletype:  3D

Values in a single grid cell at index 55,12::

    $ kmsgrid info Geoids2013\nkgrf03vel.01 --point 55 12
    0.649999976158 -0.200000002980 -0.720000028610


Translate
...............................................................................

The ``translate`` sub-command work similar to ``gdal_translate`` in that it
translates from one format to another. In fact, behind the scenes, it uses GDAL
to convert KMS grids to more common formats. Only a small subset of the
GDAL formats available can be used with ``kmsgrid``.

::

    $ kmsgrid translate --help
    usage: kmsgrid translate [-h] [--driver DRIVER]
                             [--creation_options CREATION_OPTIONS]
                             grid out dimensions [dimensions ...]

    positional arguments:
      grid                  Binary grid file.
      out                   Name of output grid file
      dimensions            List of dimensions in output grid, e.g. "1 2"

    optional arguments:
      -h, --help            show this help message and exit
      --driver DRIVER, -d DRIVER
                            Output format. Currently supports: GTiff, GTX, NTv2
      --creation_options CREATION_OPTIONS, -co CREATION_OPTIONS
                            Additional GDAL creation options. Must be formatted
                            as "PARAM1=foo PARAM2=bar".

Translate the DVR90 geoid grid to GTX format::

    $ kmsgrid translate --driver=GTX dvr90g2013.01 dvr90.gtx 1

Translate the NKG velocity model to two grids, one for the horizontal part in
NTv2 format and one for the vertical part in GTX format:

    $ kmsgrid translate --driver=NTv2 nkgrf03vel.01 nkgrf03vel_xy.gsb 1 2
    $ kmsgrid translate --driver=GTX nkgrf03vel.01 nkgrf03vel_z.gtx 3


API
-------------------------------------------------------------------------------

This is just a simple example of how the API can be used::

    from kmsgrid import KMSGrid

    # print some useful info
    grid = KMSGrid('dvr90g.2013.01')
    print('Dimensions of grid: {0}'.format(grid.dims))
    print('Datum of grid: {0}'.format(grid.datum))
    print('Bounding boix of grid: [{0}, {1}, {2}, {3}'.format(
        grid.lonmix, grid.latmin, grid.lonmax, grid.latmax))

    # convert grid to a TIFF file
    grid.export(filename='dvr90.tif', dimensions=1)


Installing
===============================================================================

Clone the repository from GitHub and run the following command in the local
repository folder:

::

  $ python setup.py install

Alternatively ``kmsgrid`` can be installed from the Python Package Index with
``pip``::

  pip install kmsgrid
  