.. _crispy-forms-foundation-demo: https://github.com/sveetch/crispy-forms-foundation-demo

=========
Changelog
=========

Version 0.7.0 - 2017/10/08
**************************

**Add support for Django 2.0 and 2.1**

* Rewrite package to use ``setup.cfg``;
* Add support for Django 2.0 and Django 2.1, close #36;
* Django 1.11 support is the last one for Python2;
* Change old demo project to more cleaner sandbox;
* Included fix from django-crispy-forms#836 for
  ``FormHelper.field_template`` usage in uniform, close #39;

Version 0.6.4 - 2017/07/29
**************************

* Fixed ``layout.buttons.ButtonGroup`` for deprecated ``Context()`` usage;
* Fixed tests that performs comparison on html part using ``django.test.html.parse_html``;

Version 0.6.3 - 2017/07/16
**************************

This release adds some bugfixes with Abide, new button objects that will replace the old ones a release and Foundation5 support will be removed for the next (non bugfix) release.

* Removed ``is-visible`` class and added missing ``data-form-error-for`` attribute in Foundation6 field templates, close #33;
* Added new field ``layout.fields.FakeField``;
* Fixed tests to always compare rendered value to attempted value, so the test error output diffs are allways in the same order;
* Updated documentation;
* Adopted new settings structure in ``project/settings/``, removed ``db.sqlite3`` from repository;
* Enabled ``django-debug-toolbar`` in development environment and settings for demo only (not for tests);
* Moved ``layout.buttons.Hidden`` to ``layout.fields.Hidden``;
* Added ``layout.buttons.ButtonElement``, ``layout.buttons.ButtonSubmit`` and ``layout.buttons.ButtonReset`` to button input as real ``<button/>`` element but keeping old input button behavior for now. **This is on the way to replace respectively** ``Button``, ``Submit`` and ``Reset``. Close #28;
* Added ``layout.buttons.InputButton``, ``layout.buttons.InputSubmit`` and ``layout.buttons.InputReset`` to maintain backward compatibility when the button objects will replace the old ones;

Version 0.6.2 - 2017/07/03
**************************

* Validated working with Django 1.11 from unittests;
* Dropped testing for Django >= 1.10 with Python 2.x in tox config;

Version 0.6.1 - 2017/07/03
**************************

* Cleaned tests structure so it runs everywhere;
* Fixed tests to pass with tox on every supported Django versions;
* Better Makefile;
* Upgraded dependancy ``django-crispy-forms`` to ``1.6.1`` since it backward compatible with Django 1.8;
* Updated documentation;

Version 0.6.0 - 2017/02/11
**************************

This release adds **Foundation for site version 6** support, version 5 support is still available for now.

* Added 'foundation-6' templates, copied from @flesser branch ``foundation-6``;
* Added ``layout.base.Callout`` element;
* Added ``crispy_forms_foundation.templatetags.crispy_forms_foundation_field`` to re-implement ``crispy_field`` filter so we can have the right input field error for Foundation-6;
* Added ``layout.buttons.ButtonHolderCallout``;
* Chanded ``.help-text`` that is allways a ``<p>`` in Foundation6 (does not have real meaning in Foundation5);
* Changed ``layout.containers.TabHolder`` so it build a random id for container if ``css_id`` is not given;
* Changed ``layout.containers.Container`` to be able to manage the *active* classname ``active_css_class`` Class attribute or its ``get_active_css_class`` method, and add it a condition to use another class name for Foundation-6 (``is-active`` instead of ``active``);
* Changed layout components to get template pack name from lazy object from ``crispy_forms.utils.TEMPLATE_PACK``;
* Changed documentation for better structure;
* Improved unittests to perform for both foundation-5 and foundation-6 template packs;
* Fixed demo views and forms so they can switch between template packs;
* Fixed layout elements so their template does not include ``TEMPLATE_PACK`` anymore in class defintions;
* Fixed switches for Foundation-6;
* Fixed button group for Foundation-6;
* Fixed ``InlineJustifiedField`` for Foundation-6;
* Fixed error messages for Foundation-6;
* Fixed Accordion for Foundation-6;
* Fixed Tabs for Foundation-6;


Version 0.5.5 - 2017/02/01
**************************

* Dropped support for Python 2.6 and Django<1.8;
* Added default app settings file;
* Added project test structure;
* Added pretty simple tests to cover layout elements which include some code;
* Added demo app taken from crispy-form-foundation-demo;
* Added dev and test requirements files;
* Updated setup.py;
* Added and enabled minified basic assets for Foundation 5 and 6 for test and demo;
* Finished demo urls/templates to work on every Foundation versions;
* Fixed Flake issues;
* Validated test with Tox for Python 2.7, Python 3.5 and Django>=1.8,<=1.10;

Backward compatibility change for foundation-5 template pack:

* Moved Tab link template ``tab-item.html`` to ``tab-link.html``;
* Added ``tab-item.html`` to build the Tab item instead of using the Div default template;

Everything should still work as with previous version.


Version 0.5.4 - 2016/02/26
**************************

* Fixed ``TabHolder`` and ``AccordionHolder`` to have the right *active* behavior on their items: activate the first item with a field error if any, else just activate the first item;


Version 0.5.3 - 2015/09/25
**************************

* Fixed bugs with button layout elements since django-crispy-forms==1.5.x, this is backward compatible with previous django-crispy-forms<1.5.x (with pull request #26 to close #25);
* Fixed package infos and README to be more explicit on Django compatibility (1.4 to 1.8 actually tested);


Version 0.5.2 - 2015/07/12
**************************

* Use relative imports and enforce absolute imports;
* Add german and french translation with i18n;


Version 0.5.1 - 2015/05/02
**************************

* Fix 'disable_csrf' option that was not honored in template forms;


Version 0.5.0 - 2015/04/02
**************************

* Better layout elements organization;
* Merged pull request #20 for *Added Foundation tabs and accordion components based on crispy-forms bootstrap3 implementation*;
* Removed all stuff for Foundation 3 that is not supported anymore;
* Fix TabItem and TabHolder so tab inputs errors are raised to the Tab item;
* Fix AccordionItem and AccordionHolder so accordion inputs errors are raised to the accordion item name;
* Add jquery plugin to add Abide support within tabs and accordions so the input errors are raised to their title name and not hided into contents;
* Update documentation;


Version 0.4.1 - 2015/02/22
**************************

* Added docs for submit button;
* Fixed bug where the class layout property was being used and modified by instances;
* Added Contributors to the doc;


Version 0.4 - 2014/11/29
************************

* Allow unicode characters in the form title in ``forms.FoundationFormMixin``;
* Extended ``forms.FoundationFormMixin.init_helper()`` to allow more customization:

  * Renamed attribute input to submit as this is more descriptive
  * Allow to give a string which is used as display text for the Submit button
  * Allow to give a Submit instance wich is directly used

* Added ``forms.FoundationFormMixin.title_templatestring`` attribute to store template string used to display form title;
* Moved ``forms.FoundationFormMixin.id`` attribute name to ``forms.FoundationFormMixin.form_id``;


Version 0.3.9 - 2014/11/21
**************************

* Added ``FoundationFormMixin``, ``FoundationForm`` and ``FoundationModelForm`` in ``forms.py`` to quickly and automatically create a Foundation layout;
* Added ``InlineSwitchField`` layout element for better switches usage;


Version 0.3.8 - 2014/11/16
**************************

* Redesigned *non field errors*;
* Added abide error message on field;
* Added missing error message and help text on inline field;


Version 0.3.7 - 2014/11/15
**************************

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


Version 0.3.0 - 2014/03/28
**************************

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


Version 0.1.0 - 2012/12/23
**************************

First commit.
