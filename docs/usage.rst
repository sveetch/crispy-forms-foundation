.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation
.. _Foundation Grid: http://foundation.zurb.com/docs/components/grid.html
.. _crispy-forms-foundation-demo: https://github.com/sveetch/crispy-forms-foundation-demo
.. _Abide: http://foundation.zurb.com/docs/components/abide.html

=====
Usage
=====

Import **crispy-forms-foundation** then you can use the layout objects in your form :
    
.. sourcecode:: python

    from crispy_forms_foundation.layout import Layout, Fieldset, SplitDateTimeField, Row, Column, ButtonHolder, Submit

    class YourForm(forms.ModelForm):
        """
        *Page* form
        """
        def __init__(self, *args, **kwargs):
            # Init layout form with crispy
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

The embedded templates are in ``crispy_forms_foundation/templates/foundation-5``.

Use Foundation Abide validation
*******************************

You can use `Abide`_ validation in your form but note that there is no support within the layout objects. You will have to add the ``required`` attribute (and eventually its validation pattern) on your field widgets in your form like this:

.. sourcecode:: python

    title = forms.CharField(label=_('Title'), widget=forms.TextInput(attrs={'required':''}), required=True)

To enable `Abide`_ on your form, you'll have to load its Javascript library (if you don't load yet the whole Foundation library) then in your form helper you will have to add its attribute on the form like this :

.. sourcecode:: python

    class SampleForm(forms.Form):
        title = forms.CharField(label=_('Title'), widget=forms.TextInput(attrs={'required':''}), required=True)
        textarea_input = forms.CharField(label=_('Textarea'), widget=forms.Textarea(attrs={'required':''}), required=True)
        
        def __init__(self, *args, **kwargs):
            self.helper = FormHelper()
            
            # Enable Abide validation on the form
            self.helper.attrs = {'data_abide': ''}
            
            self.helper.form_action = '.'
            self.helper.layout = Layout(
                ...
            )
            
            super(SampleForm, self).__init__(*args, **kwargs)

You can also set an `Abide`_ error message directly on the field like this :

.. sourcecode:: python

    class SampleForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(SampleForm, self).__init__(*args, **kwargs)
            self.fields['textarea_input'].abide_msg = "This field is required !"

Support within tabs
-------------------

Default `Abide`_ behavior is not aware of Tabs and so input errors can be hided when they are not in the active tab.

**crispy-forms-foundation** ships a jQuery plugin that add support for this usage, you will need to load it in your pages then initialize it on your form:

.. sourcecode:: html

    <script type="text/javascript" src="{{ STATIC_URL }}js/crispy_forms_foundation/plugins.js"></script>
    <script type="text/javascript">
    //<![CDATA[
    $(document).ready(function() {
        $('form').abide_support_for_tabs();
    });
    //]]>
    </script>

This way, all input errors will be raised to their tab name that will display an error mark.

Support within accordions
-------------------------

Like with tabs, there is a jQuery plugin to add `Abide`_ support within accordions.

You will need to load it in your pages then initialize it on your form:

.. sourcecode:: html

    <script type="text/javascript" src="{{ STATIC_URL }}js/crispy_forms_foundation/plugins.js"></script>
    <script type="text/javascript">
    //<![CDATA[
    $(document).ready(function() {
        $('form').abide_support_for_accordions();
    });
    //]]>
    </script>

Automatic form layout
*********************

There is some forms you can use to quickly and automatically create a Foundation layout for your forms. This is mostly for fast integration or prototyping because it will probably never totally fit to your design.

.. automodule:: crispy_forms_foundation.forms
    :members:
