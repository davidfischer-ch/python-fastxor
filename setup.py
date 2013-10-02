#! /usr/bin/env python
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

from codecs import open
from setuptools import setup, Extension

# https://pypi.python.org/pypi?%3Aaction=list_classifiers

classifiers = """
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)
Natural Language :: English
Operating System :: POSIX :: Linux
Programming Language :: C++
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Python :: Implementation :: CPython
Topic :: Software Development :: Libraries :: Python Modules
"""

not_yet_tested = """
Operating System :: MacOS :: MacOS X
Operating System :: Unix
"""

fastxor = Extension('fastxor',
                    define_macros=[('MAJOR_VERSION', '0'), ('MINOR_VERSION', '1')],
                    include_dirs=['/usr/local/include'],
                    # libraries=[''],
                    library_dirs=['/usr/local/lib'],
                    sources=['fastxor.cpp'])

setup(name='fastxor',
      version='0.1.6',
      ext_modules=[fastxor],
      description="A C++ fast XOR implementation strongly inspired by eryksun's StackOverflow post "
                  "(http://stackoverflow.com/users/205580/eryksun)",
      long_description=open('README.rst', 'r', encoding='utf-8').read(),
      author='David Fischer',
      author_email='david.fischer.ch@gmail.com',
      url='https://github.com/davidfischer-ch/python-fastxor',
      license='EUPL 1.1',
      classifiers=filter(None, classifiers.split('\n')),
      keywords=['xor', 'c++', 'extension'],
      tests_require=['coverage', 'mock', 'nose', 'numpy', 'pytoolbox>=v5.1.7-beta'],
      # Thanks to https://github.com/graingert/django-browserid/commit/46c763f11f76b2f3ba365b164196794a37494f44
      test_suite='tests.fastxor_runtests.main')
