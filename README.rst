.. _docutils: http://docutils.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation
.. _Foundation Grid: http://foundation.zurb.com/docs/grid.php
.. _crispy-forms-foundation-demo: https://github.com/sveetch/crispy-forms-foundation-demo
.. _Abide: http://foundation.zurb.com/docs/components/abide.html

Introduction
============

This is a `Django`_ application to add `django-crispy-forms`_ layout objects for `Foundation`_.

This app does not embed a `Foundation`_ release, you will have to install it yourself.

Links
*****

* Read the documentation on `Read the docs <http://crispy-forms-foundation.readthedocs.org/>`_;
* Download his `PyPi package <http://pypi.python.org/pypi/crispy-forms-foundation>`_;
* Clone it on his `Github repository <https://github.com/sveetch/crispy-forms-foundation>`_;
* Demo app : `crispy-forms-foundation-demo`_;

Requires
========

* `django-crispy-forms`_ = 1.4.x;

Installation
============

Just register the app in your project settings like that :

.. sourcecode:: python

    INSTALLED_APPS = (
        ...
        'crispy_forms',
        'crispy_forms_foundation',
        ...
    )

Then append this part to specify usage of the Foundation set :

.. sourcecode:: python

    # Default layout to use with "crispy_forms"
    CRISPY_TEMPLATE_PACK = 'foundation-5'

If not defined, the default template pack name used is ``foundation-5``, also there is a basic ``foundation-3`` support but it's not be maintained anymore.

All other `django-crispy-forms`_ settings option apply, see its documentation for more details.
