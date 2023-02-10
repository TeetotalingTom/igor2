Igor2
=====

Python parser for Igor Binary Waves (.ibw) and Packed Experiment
(.pxp) files written by WaveMetrics' IGOR Pro software.

Igor2 is the continuation of the inactive igor project, forked
from W. Trevor King and originally written by Paul Kienzle (see
git history).

:License: GNU General Public License, version 3+

Installation
------------
You can install igor2 via pip::

    pip install igor2


Usage
-----
This package is a direct replacement of `igor`. Your scripts should work
without any issues if you replace::

    import igor

with::

    import igor2 as igor


Usage
-----

See the docstrings and unit tests for examples using the Python API.
The package also installs to scripts, ``igorbinarywave.py`` and
``igorpackedexperiment.py`` which can be used to dump files to stdout.
For details on their usage, use the ``--help`` option.  For example::

  $ igorbinarywave.py --help

For users transitioning from igor.py_, there's a compatibility module
exposing the old interface.  Just change::

  import igor

to::

  import igor.igorpy as igor

in your calling code.

Testing
-------

Run internal unit tests with::

    $ nosetests --with-doctest --doctest-tests igor test

The data in the ``test/data`` directory is in the Git repository, but
it is not bundled with the source code.  If you want the test data,
you'll have to clone the Git repository or download a snapshot.

Licence
-------

This project is distributed under the `GNU Lesser General Public
License Version 3`_ or greater, see the ``COPYING`` file distributed
with the project for details.

Links
-----

.. _layman: http://layman.sourceforge.net/
.. _wtk overlay: http://blog.tremily.us/posts/Gentoo_overlay/
.. _Debian: http://www.debian.org/
.. _Gentoo: http://www.gentoo.org/
.. _NumPy: http://numpy.scipy.org/
.. _Matplotlib: http://matplotlib.sourceforge.net/
.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
.. _Git: http://git-scm.com/
.. _homepage: http://blog.tremily.us/posts/igor/
.. _pip: http://pypi.python.org/pypi/pip
.. _igor.py: http://pypi.python.org/pypi/igor.py
.. _GNU Lesser General Public License Version 3:
    http://www.gnu.org/licenses/lgpl.txt
.. _update-copyright: http://blog.tremily.us/posts/update-copyright/