.. _crispy-forms-foundation-demo: https://github.com/sveetch/crispy-forms-foundation-demo

=========
Changelog
=========

Version 0.4
***********

* Allow unicode characters in the form title in ``forms.FoundationFormMixin``;
* Extended ``forms.FoundationFormMixin.init_helper()`` to allow more customization:

  * Renamed attribute input to submit as this is more descriptive
  * Allow to give a string which is used as display text for the Submit button
  * Allow to give a Submit instance wich is directly used

* Added ``forms.FoundationFormMixin.title_templatestring`` attribute to store template string used to display form title;
* Moved ``forms.FoundationFormMixin.id`` attribute name to ``forms.FoundationFormMixin.form_id``;

Version 0.3.9
*************

* Add ``FoundationFormMixin``, ``FoundationForm`` and ``FoundationModelForm`` in ``forms.py`` to quickly and automatically create a Foundation layout;
* Add ``InlineSwitchField`` layout element for better switches usage;

Version 0.3.8
*************

* Redesign *non field errors*;
* Add abide error message on field;
* Add missing error message and help text on inline field;

Version 0.3.7
*************

* Add better documentation with Sphinx in 'docs/';

Version 0.3.6
*************

* Add ``ButtonGroup`` to use Foundation's Button groups instead of Button holder;
* Add ``Panel`` layout element that act like a ``Div`` but add a ``panel`` css class name;

Version 0.3.5
*************

* Add ``SwitchField`` field;

Version 0.3.3
*************

* Fix bad template includes in some templates;

Version 0.3.2
*************

* Fix some css class in templates;
* Add documentation for ``Abide`` usage;
* Add ``ButtonHolderPanel`` layout object;

Version 0.3.1
*************

* Added ``InlineField`` and ``InlineJustifiedField``;

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
