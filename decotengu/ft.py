#
# DecoTengu - dive decompression library.
#
# Copyright (C) 2013 by Artur Wroblewski <wrobell@pld-linux.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import logging

logger = logging.getLogger(__name__)


def seq(start, stop, step=1):
    """
    Create a sequence [start, stop] with specific step.
    """
    if start > stop and step > 0 or start < stop and step < 0:
        raise ValueError('Wrong sign of step')

    count = int((stop - start) / step) + 1
    return (start + k * step for k in range(count))


def recurse_while(predicate, f, start):
    """
    Execute function `f` while predicate function is true.

    If `f` is never executed then `start` value is returned.

    :Parameters:
     predicate
        Predicate function guarding execution.
     f
        Function to execute. Value returned by the function is passed as
        argument for next invocation.
     start
        Value passed as argument during first execution of `f` function.
    """
    x = None
    while predicate(start):
        x = start
        start = f(x)
    if x is None:
        return start
    return x


def bisect_find(n, f, *args, **kw):
    """
    Find largest k for which f(k) is True.
    
    The k is integer in range 0 <= k <= n - 1.

    There must be at least one k for which f(k) is False. If not, then
    ValueError exception is raised.

    :Parameters:
     n
        Range for k, so 0 <= k <= n - 1.
     f
        Invariant function accepting k.
     *args
        Additional positional parameters of f.
     **kw
        Additional named parameters of f.
    """
    lo = 0
    hi = n
    logger.debug('bisect n: {}'.format(n))

    while lo < hi:
        k = (lo + hi) // 2

        logger.debug('bisect range: {} <= {} <= {}'.format(lo, k, hi))
        assert lo <= k <= hi, 'bisect range: {} <= {} <= {}'.format(lo, k, hi)

        if f(k, *args, **kw):
            lo = k + 1
        else:
            hi = k

    if hi == 0:
        return -1
        # raise ValueError('Possible solution out of 0 <= k <= {} range (k reached {})'.format(n - 1, hi - 1))
    elif lo == n:
        return n
        # raise ValueError('Possible solution out of 0 <= k <= {} range (k reached {})'.format(n - 1, lo))
    assert hi > 0
    if __debug__:
        logger.debug('bisect check a >= b')
        assert f(hi - 1, *args, **kw)

        logger.debug('bisect check a < b')
        assert not f(hi, *args, **kw)

    return hi - 1 # hi is first k for which f(k) is not true, so f(hi - 1) is true


# vim: sw=4:et:ai

