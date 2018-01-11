# -*- coding: utf-8 -*-
import os
import utils
import ImageGrab
import time

BBOX = [60, 220, 230, 315]
CWD = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')


@utils.timeit
def grab(filename=None, filetype='JPEG', bbox=None):
    if not os.path.exists(CWD):
        os.makedirs(CWD)

    filename = filename or os.path.join(CWD, ('%s.jpg' % time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())))
    bbox = bbox or BBOX
    im = ImageGrab.grab(bbox)
    im.save(filename, filetype)
    s2 = open(filename, 'rb').read()
    return s2


if __name__ == '__main__':
    grab()
