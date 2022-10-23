.. _Abide: https://get.foundation/docs/components/abide.html

===============================
Use Foundation Abide validation
===============================

You can use `Abide`_ validation in your form but note that there is no support within the layout objects. You will have to add the ``required`` attribute (and eventually its validation pattern) on your field widgets in your form like this:

.. code-block:: python

    title = forms.CharField(label=_('Title'), widget=forms.TextInput(attrs={'required':''}), required=True)

To enable `Abide`_ on your form, you'll have to load its Javascript library (if you don't load yet the whole Foundation library) then in your form helper you will have to add its attribute on the form like this :

.. code-block:: python

    class SampleForm(forms.Form):
        title = forms.CharField(label=_('Title'), widget=forms.TextInput(attrs={'required':''}), required=True)
        textarea_input = forms.CharField(label=_('Textarea'), widget=forms.Textarea(attrs={'required':''}), required=True)

        def __init__(self, *args, **kwargs):
            self.helper = FormHelper()

            # Enable Abide validation on the form
            self.helper.attrs = {'data_abide': '', 'novalidate': ''}

            self.helper.form_action = '.'
            self.helper.layout = Layout(
                ...
            )

            super(SampleForm, self).__init__(*args, **kwargs)

If needed, you can define an `Abide`_ error message directly on the field like this :

.. code-block:: python

    class SampleForm(forms.Form):
        def __init__(self, *args, **kwargs):
            super(SampleForm, self).__init__(*args, **kwargs)
            self.fields['textarea_input'].abide_msg = "This field is required !"


Support within tabs
*******************

Default `Abide`_ behavior is not aware of Tabs and so input errors can be hided when they are not in the active tab.

**crispy-forms-foundation** ships a jQuery plugin that add support for this usage, you will need to load it in your pages then initialize it on your form:

.. code-block:: html

    <script src="{{ STATIC_URL }}js/crispy_forms_foundation/plugins.js"></script>
    <script>
    $(document).ready(function() {
        $('form').abide_support_for_tabs();
    });
    </script>

This way, all input errors will be raised to their tab name that will display an error mark.


Support within accordions
*************************

Like with tabs, there is a jQuery plugin to add `Abide`_ support within accordions.

You will need to load it in your pages then initialize it on your form:

.. code-block:: html

    <script src="{{ STATIC_URL }}js/crispy_forms_foundation/plugins.js"></script>
    <script>
    $(document).ready(function() {
        $('form').abide_support_for_accordions();
    });
    </script>
