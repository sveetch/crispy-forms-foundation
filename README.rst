.. _docutils: http://docutils.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation

Introduction
============

This is a `Django`_ application to add `django-crispy-forms`_ layout objects for `Foundation`_.

Actually this is only to use specific templates and changing some CSS class names.

This app does not embed a `Foundation`_ release, you will have to install it yourself.

Links
*****

* Download his `PyPi package <http://pypi.python.org/pypi/crispy-forms-foundation>`_;
* Clone it on his `Github repository <https://github.com/sveetch/crispy-forms-foundation>`_;

Requires
========

* `django-crispy-forms`_ >= 1.1.2;

Installation
============

Just register the app in your project settings like this :

.. sourcecode:: python

    INSTALLED_APPS = (
        ...
        'crispy_forms',
        'crispy_forms_foundation',
        ...
    )

Usage
=====

Import `crispy-forms-foundation`_ then you can use the layout object in your forms :
    
.. sourcecode:: python

    from crispy_forms_foundation import Layout, Fieldset, Field, SplitDateTimeField, RowFluid, Column, Div, ButtonHolder, Submit, HTML

    class YourForm(forms.ModelForm):
        """
        *Page* form
        """
        def __init__(self, *args, **kwargs):
            self.helper = FormHelper()
            self.helper.form_action = '.'
            self.helper.layout = Layout(
                Fieldset(
                    ugettext('Content'),
                    'title',
                    'content',
                ),
                Fieldset(
                    ugettext('Display settings'),
                    RowFluid(
                        Column('template', css_class='six'),
                        Column('order', css_class='three'),
                        Column('visible', css_class='three'),
                    ),
                ),
                Fieldset(
                    ugettext('Publish settings'),
                    'parent',
                    RowFluid(
                        Column(SplitDateTimeField('published'), css_class='six'),
                        Column('slug', css_class='six'),
                    ),
                ),
                ButtonHolder(
                    Submit('submit_and_continue', ugettext('Save and continue')),
                    Submit('submit', ugettext('Save')),
                ),
            )
            
            super(YourForm, self).__init__(*args, **kwargs)

The embedded templates are in ``crispy_forms_foundation/templates/foundation``.
