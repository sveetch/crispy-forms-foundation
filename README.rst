.. _docutils: http://docutils.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation
.. _Foundation Grid: http://foundation.zurb.com/docs/grid.php
.. _crispy-forms-foundation-demo: https://github.com/sveetch/crispy-forms-foundation-demo

Introduction
============

This is a `Django`_ application to add `django-crispy-forms`_ layout objects for `Foundation`_.

This app does not embed a `Foundation`_ release, you will have to install it yourself.

Links
*****

* Download his `PyPi package <http://pypi.python.org/pypi/crispy-forms-foundation>`_;
* Clone it on his `Github repository <https://github.com/sveetch/crispy-forms-foundation>`_;

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

If not defined, the default template pack name used is ``foundation-5``, also you can use ``foundation-3``.

All other `django-crispy-forms`_ settings option apply, see its documentation for more details.

Usage
=====

Import **crispy-forms-foundation** then you can use the layout object in your forms :
    
.. sourcecode:: python

    from crispy_forms_foundation.layout import Layout, Fieldset, Field, SplitDateTimeField, RowFluid, Column, Div, ButtonHolder, Submit, HTML

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
                    Row(
                        Column('template', css_class='large-6'),
                        Column('order', css_class='large-3'),
                        Column('visible', css_class='large-3'),
                    ),
                ),
                Fieldset(
                    ugettext('Publish settings'),
                    'parent',
                    Row(
                        Column(SplitDateTimeField('published'), css_class='large-6'),
                        Column('slug', css_class='large-6'),
                    ),
                ),
                ButtonHolder(
                    Submit('submit_and_continue', ugettext('Save and continue')),
                    Submit('submit', ugettext('Save')),
                ),
            )
            
            super(YourForm, self).__init__(*args, **kwargs)

The embedded templates are in ``crispy_forms_foundation/templates/foundation``.

Layout items
************

There is some layout items dedicated to `Foundation`_, other embedded items are just cloned from the **uni_form** layout items from `django-crispy-forms`_ to use the right template.

Row
---

Act as a div container row, it will embed its items in a div like that :

.. sourcecode:: html

    <div class"row">Your stuff</div>


RowFluid
--------

It has a same behaviour than `Row`_ but add a CSS class "row-fluid" that you can use to have top level row that take all the container width. You have to put the CSS for this class to your CSS stylesheets. It will embed its items in a div like that :

.. sourcecode:: html

    <div class"row row-fluid">Your stuff</div>

The CSS to add should be something like that :

.. sourcecode:: css

    .row-fluid {
        width: 100%;
        max-width: 100%;
        min-width: 100%;
    }

Column
------

This is the column from the `Foundation Grid`_, all columns should be contained in a `Row`_ or a `RowFluid`_ and you will have to define the column type in the ``css_class`` attribute.

Example :

.. sourcecode:: python

    Column('form_field_1', 'form_field_2', css_class='small-12 large-6')

Will render to something like that :

.. sourcecode:: html

    <div class"small-12 large-6 columns">...</div>

``columns`` class is allways appended, so you don't need to specify it.

If not defined, ``css_class`` will default to 'large-12'.

InlineField
-----------

Layout object for rendering an inline field with Foundation form.

Example :

.. sourcecode:: python

    InlineField('field_name')

There is also three optionnal keywords :

label_column='small-3', input_column='small-9', label_class=''

* ``label_column`` css class to add on the label div column, default to ``large-3``;
* ``input_column`` css class to add on the input div column, default to ``large-9``;
* ``label_class`` css class to add on the label element, defaut is empty, you can use it to add alignment like ``right inline``;

Example :

.. sourcecode:: python

    InlineField('field_name', label_column='small-6 large-3', input_column='small-6 large-9', label_class='right inline')

Note that ``label_column`` and ``input_column`` are allways filled with the css class ``columns``.

InlineJustifiedField
--------------------

Same as `InlineField`_ but default is to be right aligned with a vertical padding using the ``label_class`` argument.

Changelog
=========

Version 0.3.1
*************

* Added `InlineField`_ and `InlineJustifiedField`_;

Version 0.3.0
*************

Some backward incompatible change have been done, be sure to check them before upgrading.

* Removed sample view, url and templates. If needed you can find a Django app sample on `crispy-forms-foundation-demo`_;
* Moving ``foundation`` template pack name and its directory to ``foundation-3``. You have to change your ``settings.CRISPY_TEMPLATE_PACK`` if you used the old one;
* Add ``foundation-5`` template pack, it is now the default template pack;
* Removing camelcase on some css classes :

  * ``ctrlHolder`` has changed to ``holder``;
  * ``buttonHolder`` has changed to ``button-holder``;
  * ``asteriskField`` has changed to ``asterisk``;
  * ``errorField`` has changed to ``error``;
  * ``formHint`` has changed to ``hint``;
  * ``inlineLabel`` has changed to ``inline-label``;
  * ``multiField`` has changed to ``multiple-fields``;
