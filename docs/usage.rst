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

    from crispy_forms_foundation.layout import Layout, Fieldset, Field, SplitDateTimeField, Row, RowFluid, Column, Div, ButtonHolder, Submit, HTML

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

.. automodule:: crispy_forms_foundation.layout
    :members:

Use Foundation 5 Abide
**********************

You can use `Abide`_ validation in your form but note that there is no support within the layout objects. You will have to add the ``required`` attribute (and eventually its pattern) on your field widgets in your form.

So to enable `Abide`_ you'll have to load its Javascript library if you don't load yet the whole Foundation library, then in your form helper you will have to its attribute on the form like this :

.. sourcecode:: python

    class SampleForm(forms.Form):
        def __init__(self, *args, **kwargs):
            self.helper = FormHelper()
            self.helper.attrs = {'data_abide': ''}
            self.helper.form_action = '.'
            self.helper.layout = Layout(
                ...
            )
            
            super(SampleForm, self).__init__(*args, **kwargs)

Then add the required attribute on a field widget like this :

.. sourcecode:: python

    textarea_input = forms.CharField(label=_('Textarea'), widget=forms.Textarea(attrs={'required':''}), required=True)

You can also set an abide error message directly on the field like this :

.. sourcecode:: python

    class SampleForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(SampleForm, self).__init__(*args, **kwargs)
            self.fields['textarea_input'].abide_msg = "This field is required !"

Automatic form layout
*********************

There is some forms you can use to quickly and automatically create a Foundation layout for your forms. This is mostly for fast integration or prototyping because it will probably never fit to your design.

.. automodule:: crispy_forms_foundation.forms
    :members:
