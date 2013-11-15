===============================
rcfile
===============================

.. image:: https://badge.fury.io/py/rcfile.png
    :target: http://badge.fury.io/py/rcfile

.. image:: https://travis-ci.org/aequitas/rcfile.png?branch=master
        :target: https://travis-ci.org/aequitas/rcfile

.. image:: https://pypip.in/d/rcfile/badge.png
        :target: https://crate.io/packages/rcfile?version=latest

.. image:: https://coveralls.io/repos/aequitas/rcfile/badge.png?branch=master 
        :target: https://coveralls.io/r/aequitas/rcfile?branch=master

Configuration file loader for Python projects

Based on: https://github.com/dominictarr/rc

Features
--------

Read environment variables and config files and return them merged with predefined list of arguments.

Arguments:
    appname - application name, used for config files and environemnt variable names.
    args - arguments from command line (optparse, docopt, etc).
    strip_dashes - strip dashes prefixing key names from args dict.

Returns:
    dict containing the merged variables of environment variables, config files and args.

Environment variables are read if they start with appname in uppercase with underscore, for example:

    TEST_VAR=1

Config files compatible with ConfigParser are read and the section name appname is read, example:

    [appname]
    var=1

Files are read from: /etc/appname/config, /etc/appfilerc, ~/.config/appname/config, ~/.config/appname,
    ~/.appname/config, ~/.appnamerc, .appnamerc, file provided by config variable in args.

Example usage with docopt:

    args = rcfile(__name__, docopt(__doc__, version=__version__))

* TODO

Requirements
------------

- Python >= 2.6 or >= 3.3

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/aequitas/rcfile/blob/master/LICENSE>`_ file for more details.
