"""Common code for scripts distributed with the `igor` package."""
from __future__ import absolute_import

import argparse as _argparse
import logging
import sys as _sys

try:
    import matplotlib as _matplotlib
    import matplotlib.pyplot as _matplotlib_pyplot
except ImportError as _matplotlib_import_error:
    _matplotlib = None

from ._version import __version__


logger = logging.getLogger(__name__)


class Script (object):
    log_levels = [logging.ERROR, logging.WARNING,
                  logging.INFO, logging.DEBUG]

    def __init__(self, description=None,
                 filetype='IGOR Binary Wave (.ibw) file'):
        self.parser = _argparse.ArgumentParser(description=description)
        self.parser.add_argument(
            '--version', action='version',
            version='%(prog)s {}'.format(__version__))
        self.parser.add_argument(
            '-f', '--infile', metavar='FILE', default='-',
            help='input {}'.format(filetype))
        self.parser.add_argument(
            '-o', '--outfile', metavar='FILE', default='-',
            help='file for ASCII output')
        self.parser.add_argument(
            '-p', '--plot', action='store_const', const=True,
            help='use Matplotlib to plot any IGOR waves')
        self.parser.add_argument(
            '-V', '--verbose', action='count', default=0,
            help='increment verbosity')
        self._num_plots = 0

    def run(self, *args, **kwargs):
        args = self.parser.parse_args(*args, **kwargs)
        if args.infile == '-':
            args.infile = _sys.stdin
        if args.outfile == '-':
            args.outfile = _sys.stdout
        if args.verbose > 1:
            log_level = self.log_levels[min(
                args.verbose - 1, len(self.log_levels) - 1)]
            logger.setLevel(log_level)
        self._run(args)
        self.display_plots()

    def _run(self, args):
        raise NotImplementedError()

    def plot_wave(self, args, wave, title=None):
        if not args.plot:
            return  # no-op
        if not _matplotlib:
            raise _matplotlib_import_error
        if title is None:
            title = wave['wave']['wave_header']['bname']
        figure = _matplotlib_pyplot.figure()
        axes = figure.add_subplot(1, 1, 1)
        axes.set_title(title)
        try:
            axes.plot(wave['wave']['wData'], 'r.')
        except ValueError as error:
            logger.error('error plotting {}: {}'.format(title, error))
            pass
        self._num_plots += 1

    def display_plots(self):
        if self._num_plots:
            _matplotlib_pyplot.show()
