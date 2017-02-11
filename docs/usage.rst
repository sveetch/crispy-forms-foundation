============
Basic sample
============

Import **crispy-forms-foundation** then you can use the layout objects in your form :

.. sourcecode:: python

    from crispy_forms_foundation.layout import Layout, Fieldset, SplitDateTimeField, Row, Column, ButtonHolder, Submit

    class YourForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            self.helper = FormHelper()
            self.helper.form_action = '.'
            self.helper.layout = Layout(
                Fieldset(
                    'Content',
                    'title',
                    'content',
                ),
                Fieldset(
                    'Display settings',
                    Row(
                        Column('template', css_class='large-6'),
                        Column('order', css_class='large-3'),
                        Column('visible', css_class='large-3'),
                    ),
                ),
                Fieldset(
                    'Publish settings',
                    'parent',
                    Row(
                        Column(SplitDateTimeField('published'), css_class='large-6'),
                        Column('slug', css_class='large-6'),
                    ),
                ),
                ButtonHolder(
                    Submit('submit_and_continue', 'Save and continue'),
                    Submit('submit', 'Save'),
                ),
            )

            super(YourForm, self).__init__(*args, **kwargs)

Embedded templates are in ``crispy_forms_foundation/templates/foundation-5`` or ``crispy_forms_foundation/templates/foundation-6`` depending of your template pack.
