"""
Used forms in tests
"""
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import (Layout, Row, Column, ButtonHolder,
                                            Submit)


class BasicInputForm(forms.Form):
    """
    Basic form with a single CharField field
    """
    simple = forms.CharField(label='Simple text',
                             widget=forms.TextInput(attrs={'required':''}),
                             required=True)

    def save(self, commit=True):
        return


class BoolInputForm(forms.Form):
    """
    Basic form with a single BooleanField field
    """
    opt_in = forms.BooleanField(
            label="Opt in",
            widget=forms.CheckboxInput(attrs={'required': ''}),
            required=True)

    def save(self, commit=True):
        return


class BasicInputFormLayoutIncluded(BasicInputForm):
    """
    Basic form with included layout
    """
    def __init__(self, *args, **kwargs):
        self.helper = kwargs.pop('helper', FormHelper())

        self.helper.form_action = '.'

        self.helper.layout = Layout(
            'simple',
        )

        super(BasicInputFormLayoutIncluded, self).__init__(*args, **kwargs)


class AdvancedForm(forms.Form):
    """
    Form with an advanced layout with some inputs
    """
    simple = forms.CharField(label='Simple text',
                             widget=forms.TextInput(attrs={'required':''}),
                             required=True)
    opt_in = forms.BooleanField(
            label="Opt in",
            widget=forms.CheckboxInput(attrs={'required': ''}),
            required=True)
    longtext = forms.CharField(label='Address', required=False,
                              widget=forms.Textarea(attrs={'rows': 3}))

    def save(self, commit=True):
        return
