.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms

.. _install-intro:

=======
Install
=======

Get it from PyPi: ::

    pip install crispy-forms-foundation


Register required applications in your project settings:

    .. code-block:: python

        INSTALLED_APPS = (
            ...
            "crispy_forms",
            "crispy_forms_foundation",
            ...
        )

Import default settings at the end of the settings file:

    .. code-block:: python

        from crispy_forms_foundation.settings import *

Default template pack name used will be ``foundation-6``.

All other `django-crispy-forms`_ settings option apply, see its documentation for
more details.

Finally you will need to install Foundation assets in your project. For novices, a
quick way to start is to use last
`Foundation compiled version from CDN links <https://get.foundation/sites/docs/installation.html#cdn-links>`_.
