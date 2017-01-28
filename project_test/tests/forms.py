"""
Used forms in tests
"""
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import (Layout, Row, Column, ButtonHolder,
                                            Submit)


class BasicForm(forms.Form):
    """
    Basic form without defined layout for a single input
    """
    simple = forms.CharField(label='Simple text',
                             widget=forms.TextInput(attrs={'required':''}),
                             required=True)

    def save(self, commit=True):
        return


class LayoutForm(forms.Form):
    """
    Form with a layout for a single input
    """
    simple = forms.CharField(label='Simple text',
                             widget=forms.TextInput(attrs={'required':''}),
                             required=True)

    def __init__(self, *args, **kwargs):
        foundation_version = kwargs.pop('foundation_version', None)

        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.template_pack = "foundation-{}".format(foundation_version)

        self.helper.layout = Layout(
            'simple',
        )

        super(LayoutForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        return


class AdvancedForm(forms.Form):
    """
    Form with an advanced layout with some inputs
    """
    simple = forms.CharField(label='Simple text',
                             widget=forms.TextInput(attrs={'required':''}),
                             required=True)
    opt_in = forms.BooleanField(
            label="Opt in",
            widget=forms.CheckboxInput(attrs={'required': ''}), required=True)
    longtext = forms.CharField(label='Address', required=False,
                              widget=forms.Textarea(attrs={'rows': 3}))

    def __init__(self, *args, **kwargs):
        foundation_version = kwargs.pop('foundation_version', None)

        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.template_pack = "foundation-{}".format(foundation_version)

        self.helper.layout = Layout(
            Row(
                Column(
                    'simple',
                    css_class='six'
                ),
                Column(
                    'opt_in',
                    css_class='six'
                ),
            ),
            Row(
                Column(
                    'longtext'
                ),
            ),
            Row(
                Column(
                    ButtonHolder(Submit('submit', 'Submit')),
                ),
                css_class="large"
            ),
        )

        super(AdvancedForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        return
