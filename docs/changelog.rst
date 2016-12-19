.. _crispy-forms-foundation-demo: https://github.com/sveetch/crispy-forms-foundation-demo

=========
Changelog
=========

Devel - Unreleased
******************

* Added default app settings file;
* Added project test structure;
* Added demo app taken from crispy-form-foundation-demo;
* Added dev and test requirements files;
* Updated setup.py;
* Added and enabled minified basic assets for Foundation 5 and 6;
* Finished urls/templates dynamic structure to work on every versions;

Version 0.5.4
*************

* Fixed ``TabHolder`` and ``AccordionHolder`` to have the right *active* behavior on their items: activate the first item with a field error if any, else just activate the first item;

Version 0.5.3
*************

* Fixed bugs with button layout elements since django-crispy-forms==1.5.x, this is backward compatible with previous django-crispy-forms<1.5.x (with pull request #26 to close #25);
* Fixed package infos and README to be more explicit on Django compatibility (1.4 to 1.8 actually tested);

Version 0.5.2
*************

* Use relative imports and enforce absolute imports;
* Add german and french translation with i18n;

Version 0.5.1
*************

* Fix 'disable_csrf' option that was not honored in template forms;

Version 0.5.0
*************

* Better layout elements organization;
* Merged pull request #20 for *Added Foundation tabs and accordion components based on crispy-forms bootstrap3 implementation*;
* Removed all stuff for Foundation 3 that is not supported anymore;
* Fix TabItem and TabHolder so tab inputs errors are raised to the Tab item;
* Fix AccordionItem and AccordionHolder so accordion inputs errors are raised to the accordion item name;
* Add jquery plugin to add Abide support within tabs and accordions so the input errors are raised to their title name and not hided into contents;
* Update documentation;

Version 0.4.1
*************

* Added docs for submit button;
* Fixed bug where the class layout property was being used and modified by instances;
* Added Contributors to the doc;

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

* Added ``FoundationFormMixin``, ``FoundationForm`` and ``FoundationModelForm`` in ``forms.py`` to quickly and automatically create a Foundation layout;
* Added ``InlineSwitchField`` layout element for better switches usage;

Version 0.3.8
*************

* Redesigned *non field errors*;
* Added abide error message on field;
* Added missing error message and help text on inline field;

Version 0.3.7
*************

* Added better documentation with Sphinx in 'docs/';

Version 0.3.6
*************

* Added ``ButtonGroup`` to use Foundation's Button groups instead of Button holder;
* Added ``Panel`` layout element that act like a ``Div`` but add a ``panel`` css class name;

Version 0.3.5
*************

* Added ``SwitchField`` field;

Version 0.3.3
*************

* Fix bad template includes in some templates;

Version 0.3.2
*************

* Fixed some css class in templates;
* Added documentation for ``Abide`` usage;
* Added ``ButtonHolderPanel`` layout object;

Version 0.3.1
*************

* Added ``InlineField`` and ``InlineJustifiedField``;

Version 0.3.0
*************

Some backward incompatible change have been done, be sure to check them before upgrading.

* Removed sample view, url and templates. If needed you can find a Django app sample on `crispy-forms-foundation-demo`_;
* Moved ``foundation`` template pack name and its directory to ``foundation-3``. You have to change your ``settings.CRISPY_TEMPLATE_PACK`` if you used the old one;
* Added ``foundation-5`` template pack, it is now the default template pack;
* Removed camelcase on some css classes :

  * ``ctrlHolder`` has changed to ``holder``;
  * ``buttonHolder`` has changed to ``button-holder``;
  * ``asteriskField`` has changed to ``asterisk``;
  * ``errorField`` has changed to ``error``;
  * ``formHint`` has changed to ``hint``;
  * ``inlineLabel`` has changed to ``inline-label``;
  * ``multiField`` has changed to ``multiple-fields``;
