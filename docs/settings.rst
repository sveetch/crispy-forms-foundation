.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms

========
Settings
========

**crispy-forms-foundation** itself does not have its own settings but overrides some of `django-crispy-forms`_ settings:

CRISPY_ALLOWED_TEMPLATE_PACKS
    To add ``foundation-5`` and ``foundation-6`` template pack names to allowed template packs.
CRISPY_TEMPLATE_PACK
    To set default template pack to ``foundation-6``.
CRISPY_CLASS_CONVERTERS
    To define some input class name converters required for ``foundation-6``.

These settings are defined in ``crispy_forms_foundation.settings`` you should have imported (as seen in :ref:`install-intro` document).

All other settings from `django-crispy-forms`_ still apply to change crispies behaviors.
