"""
catchpycli.utils
----------------
all the useful things
"""

import sys
import platform

from . import __version__


def default_useragent():
    """Return a string representing the default user agent."""
    _implementation = platform.python_implementation()

    if _implementation == 'CPython':
        _implementation_version = platform.python_version()
    elif _implementation == 'PyPy':
        _implementation_version = '%s.%s.%s' % (
                sys.pypy_version_info.major,
                sys.pypy_version_info.minor,
                sys.pypy_version_info.micro)

        if sys.pypy_version_info.releaselevel != 'final':
            _implementation_version = ''.join([
                _implementation_version,
                sys.pypy_version_info.releaselevel])

    elif _implementation == 'Jython':
        _implementation_version = platform.python_version()  # Complete Guess

    elif _implementation == 'IronPython':
        _implementation_version = platform.python_version()  # Complete Guess

    else:
        _implementation_version = 'Unknown'

    try:
        p_system = platform.system()
        p_release = platform.release()
    except IOError:
        p_system = 'Unknown'
        p_release = 'Unknown'

    return " ".join([
        '%s/%s' % (__name__, __version__),
        '%s/%s' % (_implementation, _implementation_version),
        '%s/%s' % (p_system, p_release)])

