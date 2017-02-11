#: -*- coding: utf-8 -*-
"""
Settings
========

Default required settings. You can override them in your project settings
file.

"""

# Allowed layout pack
CRISPY_ALLOWED_TEMPLATE_PACKS = (
    'bootstrap',
    'uni_form',
    'bootstrap3',
    'bootstrap4',
    'foundation-5',
    'foundation-6'
)


# Default layout pack
CRISPY_TEMPLATE_PACK = 'foundation-6'

# Default class names on input
CRISPY_CLASS_CONVERTERS = {
    'inputelement': None,
    'errorcondition': 'is-invalid-input',
}
