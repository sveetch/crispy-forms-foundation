"""
Used forms in tests
"""
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import Layout


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
