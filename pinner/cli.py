#!/usr/bin/env python
"""Checks if python packages in requirements.txt are pinned

Usage:
    pinner [options] [<path>]

Options:
    -h --help         Display this help
    -v --verbose      Print extra info
"""
import logging
from docopt import docopt
import sys
from pinner.api import find_requirements, process_file


logger = logging.getLogger(__name__)


def main(argv=None):
    options = docopt(__doc__, argv=argv)
    setup_logging(options)

    path = options.get('<path>') or '.'
    files = list(find_requirements(path))
    if files:
        logger.debug('Found files: {0}'.format(','.join(files)))
    else:
        logger.error('No requirements files found in path: %s' % path)
        sys.exit(1)

    warnings = []
    for file in files:
        warnings.extend(process_file(file, emit_warning))

    sys.exit(len(warnings))


def setup_logging(options):
    level = logging.DEBUG if options['--verbose'] else logging.INFO
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(level)


def emit_warning(path, lineno, exception):
    msg = '{path}:{lineno}:1: {e.text}'.format(path=path, lineno=lineno, e=exception)
    logger.error(msg)
    return msg
