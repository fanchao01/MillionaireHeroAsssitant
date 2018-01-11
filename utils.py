# coding:utf-8

import time
import functools


DEBUG = False


def timeit(func):
    if DEBUG is True:
        @functools.wraps(func)
        def inner(*args, **kwargs):
            s = time.time()
            r = func(*args, **kwargs)
            e = time.time()
            print '%s: %0.2f seconds' % (func.__name__, (e-s))
            return r
    else:
        return func

    return inner
