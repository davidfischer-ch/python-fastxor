# -*- coding: utf-8 -*-

#**********************************************************************************************************************#
#              PYTHON-FASTXOR - A C++ fast XOR implementation strongly inspired by eryksun's StackOverflow post
#
#  Main Developer : David Fischer (david.fischer.ch@gmail.com)
#  Copyright      : Copyright (c) 2012-2013 David Fischer. All rights reserved.
#
#**********************************************************************************************************************#
#
# This file is part of python-fastxor Project.
#
# This project is free software: you can redistribute it and/or modify it under the terms of the EUPL v. 1.1 as provided
# by the European Commission. This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the European Union Public License for more details.
#
# You should have received a copy of the EUPL General Public License along with this project.
# If not, see he EUPL licence v1.1 is available in 22 languages:
#     22-07-2013, <https://joinup.ec.europa.eu/software/page/eupl/licence-eupl>
#
# Retrieved from https://github.com/davidfischer-ch/python-fastxor.git

from __future__ import division

import numpy, os, sys
from time import time
from fastxor import fast_xor_inplace
#from xorcpp import xorcpp_inplace

range_method = range if sys.version_info[0] >= 3 else xrange


def xor_inplace_loop(a, b):
    for i in range_method(len(b)):
        a[i] ^= b[i]


def xor_list_comprehension(a, b):
    return [a[i] ^ b[i] for i in range_method(len(b))]
    #c = [x ^ y for x, y in zip(a, b)]


def numpy_xor(a, b):
    u"""https://gist.github.com/zed/353005"""
    return numpy.bitwise_xor(a, b)


class Test_fastxor(object):

    def test_benchmark(self):
        print(u'\n\nBenchmark and test fast_xor_inplace ...\n')
        a1 = bytearray(os.urandom(1024 * 1024 * 2))
        a2, a3, a4 = a1[:], a1[:], a1[:]
        b = bytearray(os.urandom(len(a1)))

        t0 = time()
        xor_inplace_loop(a1, b)
        t1 = time()
        xor_inplace_loop_time = t1 - t0

        a2 = xor_list_comprehension(a2, b)
        t2 = time()
        xor_list_comprehension_time = t2 - t1

        a3 = numpy_xor(a3, b)
        t3 = time()
        numpy_xor_time = t3 - t2

        fast_xor_inplace(a4, b)
        t4 = time()
        fast_xor_inplace_time = t4 - t3

        for i in range_method(len(a1)):
            if a1[i] != a2[i] or a1[i] != a3[i] or a1[i] != a4[i]:
                raise ValueError(u'Arrays at index {0} does not match ({1}, {2}, {3}, {4})'.format(
                                 i, a1[i], a2[i], a3[i], a4[i]))

        print(u"""
======================== ======= ========
Method Name              Time    Speep-up
======================== ======= ========
xor_inplace_loop         {0:7.3} {1:8.3f}
xor_list_comprehension   {2:7.3} {3:8.3f}
numpy.bitwise_xor        {4:7.3} {5:8.3f}
fastxor.fast_xor_inplace {6:7.3} {7:8.3f}
======================== ======= ========
""".format(xor_inplace_loop_time, 1.0, xor_list_comprehension_time, xor_inplace_loop_time / xor_list_comprehension_time,
           numpy_xor_time, xor_inplace_loop_time / numpy_xor_time, fast_xor_inplace_time,
           xor_inplace_loop_time / fast_xor_inplace_time))
