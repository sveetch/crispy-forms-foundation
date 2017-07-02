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

* Unittests using `Pytest`_;
* Respecting flake and pip8 rules using `Flake8`_;
* `Sphinx`_ for documentation with enabled `Napoleon`_ extension (using only the *Google style*);
* `tox`_ to test again different Python and Django versions;


Every requirement is available in file ``requirements/dev.txt`` (except for tox).

Install for development
***********************

First ensure you have `pip`_ and ``python-venv`` package installed, clone crispy-form-foundation repository, enter its directory and just type: ::

    make install-dev

Unittests
---------

Unittests are made to works on `Pytest`_, a shortcut in Makefile is available to start them on your current development install: ::

    make tests

Tox
---

To ease development again multiple Python and Django versions, a tox configuration has been added. You are strongly encouraged to use it to test your pull requests.

Before using it you will need to install tox, it is recommended to install it at your system level so dependancy is not in tests requirements file: ::

    sudo pip install tox

Then go in the crispy-form-foundation repository directory where live the ``setup.py`` and ``tox.ini`` files and execute tox: ::

    tox

Documentation
-------------

You should see about `sphinx-autobuild`_ for a watcher which automatically rebuild HTML documentation when you change sources.

When installed you can use following command from ``docs/`` directory: ::

    make livehtml
