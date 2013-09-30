Python fastxor extension module
===============================

.. image:: https://secure.travis-ci.org/davidfischer-ch/fastxor.png
    :target: http://travis-ci.org/davidfischer-ch/fastxor

Afraid of red status ? Please click on the link, sometimes this is not my fault ;-)

A C++ fast XOR implementation strongly inspired by `eryksun's stackoverflow post <http://stackoverflow.com/users/205580/eryksun>`_

Here are the results on my workplace desktop computer (Intel(R) Core(TM) i7-3770 CPU @ 3.40GHz):

======================== ======= ========
Method Name              Time    Speep-up
======================== ======= ========
xor_inplace_loop           0.444    1.000
xor_list_comprehension     0.237    1.877
numpy.bitwise_xor        0.00175  252.986
fastxor.fast_xor_inplace 0.00125  356.339
======================== ======= ========

What the release number stands for ?
------------------------------------

I do my best to follow this interesting recommendation : `Semantic Versioning 2.0.0 <http://semver.org/>`_

How to install it (Python 2.7) ?
--------------------------------

Install some packages that are not handled by pip::

    sudo apt-get install python-dev python-pip

Make sure that pip is up-to-date (PIPception)::

    sudo pip-2.7 install --upgrade pip

Then, you only need to run ``setup.py``::

    python2 setup.py test
    sudo python2 setup.py install

How to install it (Python 3.3) ?
--------------------------------

Install some packages that are not handled by pip::

    sudo apt-get install python3-dev python3-pip

Make sure that pip is up-to-date (PIPception)::

    sudo pip-3.3 install --upgrade pip

Then, you only need to run ``setup.py``::

    python3 setup.py test
    sudo python3 setup.py install

Sometimes numpy setup fails, just run ``sudo pip-3.3 install numpy`` to solve this.

How to check coverage ?
-----------------------

::

    python setup.py test
    xdg-open tests/cover/index.html

How to use it ?
---------------

This extension module gives you access to fast_xor_inplace and fast_xor (... TODO).

2013 - David Fischer
