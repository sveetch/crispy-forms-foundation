.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation
.. _crispy-forms-foundation-demo: https://github.com/sveetch/crispy-forms-foundation-demo

=======
Install
=======

Register the app in your project settings like that :

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

If not defined, the default template pack name used is ``foundation-5``, also you can use ``foundation-3`` but pay attention that is not really maintained.

All other `django-crispy-forms`_ settings option apply, see its documentation for more details.
