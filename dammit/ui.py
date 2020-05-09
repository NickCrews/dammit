# Copyright (C) 2015-2018 Camille Scott
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.

import sys
import textwrap


def header(msg, level=1):
    '''Standardize output headers for submodules.

    This doesn't need to be logged, but it's nice for
    the user.
    '''
    if level < 1:
        level = 1
    return ' '.join([level * '#', msg])


def checkbox(msg, checked=False):
    '''Generate a Github markdown checkbox for the message.'''

    if checked:
        return '- [x] ' + msg
    else:
        return '- [ ] ' + msg


def paragraph(msg, wrap=80):
    '''Generate a wrapped paragraph.'''

    return '\n' + '\n'.join(textwrap.wrap(msg, wrap)) + '\n'

 
def listing(d):
    '''Generate a markdown list.
    '''
    if type(d) is str or type(d) is bytes:
        return d
    elif type(d) is dict:
        keys = sorted(d.keys())
        return '\n'.join(['* {k}: {v}'.format(k=key,v=d[key]) for key in keys]) + '\n'
    elif hasattr(d, '__iter__'):
        return '\n'.join(['* {0}'.format(e) for e in sorted(d)]) + '\n'
    else:
        return str(d)
