.. _virtualenv: http://www.virtualenv.org
.. _pip: https://pip.pypa.io
.. _Pytest: http://pytest.org
.. _Napoleon: https://sphinxcontrib-napoleon.readthedocs.io
.. _Flake8: http://flake8.readthedocs.io
.. _Sphinx: http://www.sphinx-doc.org
.. _tox: http://tox.readthedocs.io
.. _sphinx-autobuild: https://github.com/GaretJax/sphinx-autobuild

===========
Development
===========

Development requirement
***********************

crispy-form-foundation is developed with:

* *Test Development Driven* (TDD) using `Pytest`_;
* Respecting flake and pip8 rules using `Flake8`_;
* `Sphinx`_ for documentation with enabled `Napoleon`_ extension (using
  *Google style*);
* `tox`_ to run tests on various environments;

Install for development
***********************

First ensure you have `pip`_ and `virtualenv`_ packages installed then type: ::

    git clone https://github.com/sveetch/crispy-forms-foundation.git
    cd crispy-forms-foundation
    make install

This will install the whole project in development mode.

To reach the administration you may need a super user: ::

    make superuser


Unittests
---------

Unittests are made to works on `Pytest`_, a shortcut in Makefile is available
to start them on your current development install: ::

    make tests


Tox
---

To ease development against multiple Python versions a tox configuration has
been added. You are encouraged to use it to test your pull requests to ensure about
compatibility support.

Just go in the ``crispy-forms-foundation`` directory and execute Tox: ::

    make tox


Documentation
-------------

You can easily build the documentation from one Makefile action: ::

    make docs

There is a Makefile action ``livedocs`` to serve documentation and automatically
rebuild it when you change documentation files: ::

    make livedocs

And go on ``http://localhost:8002/`` or your server machine IP with port 8002.

Note that you need to build the documentation at least once before using
``livedocs``.
