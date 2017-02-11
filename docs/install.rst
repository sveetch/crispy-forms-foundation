.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation

.. _install-intro:

=======
Install
=======

#. Get it from PyPi: ::

    pip install crispy-forms-foundation


#. Register app in your project settings:

    .. sourcecode:: python

        INSTALLED_APPS = (
            ...
            'crispy_forms',
            'crispy_forms_foundation',
            ...
        )

#. Import default settings at the end of the settings file:

    .. sourcecode:: python

        from crispy_forms_foundation.settings import *

    Default template pack name used will be ``foundation-6``.

    All other `django-crispy-forms`_ settings option apply, see its documentation for more details.

#. Finally you will need to install Foundation assets in your project. For novices, a quick way is to use last `Foundation compiled version from CDN links <http://foundation.zurb.com/sites/docs/installation.html#cdn-links>`_.