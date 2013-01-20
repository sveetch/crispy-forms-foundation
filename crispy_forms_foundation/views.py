# -*- coding: utf-8 -*-
"""
Sample views
"""
from django.views.generic.edit import FormView
from django import forms
from django.utils.translation import ugettext

from crispy_forms.helper import FormHelper
import crispy_forms_foundation.layout as foundation_layout

class FoundationSampleForm(forms.Form):
    """
    Sample form
    """
    title = forms.CharField(label=ugettext("title"), max_length=255, required=True)
    content = forms.CharField(label=ugettext("content"), max_length=255, required=True, widget=forms.Textarea)
    first_name = forms.CharField(label=ugettext("first_name"), max_length=255, required=True)
    last_name = forms.CharField(label=ugettext("last_name"), max_length=255, required=True)
    template = forms.CharField(label=ugettext("template"), max_length=255, required=True)
    order = forms.CharField(label=ugettext("order"), max_length=255, required=True)
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = '.'
        self.helper.layout = foundation_layout.Layout(
            foundation_layout.Fieldset(
                ugettext('Simple fieldset'),
                'title',
                'content',
            ),
            foundation_layout.Fieldset(
                ugettext('Columned in a row'),
                foundation_layout.Row(
                    foundation_layout.Column('first_name', css_class='six'),
                    foundation_layout.Column('last_name', css_class='six'),
                ),
            ),
            foundation_layout.Fieldset(
                ugettext('Columned in fluid row'),
                foundation_layout.RowFluid(
                    foundation_layout.Column('template', css_class='six'),
                    foundation_layout.Column('order', css_class='six'),
                ),
            ),
            foundation_layout.ButtonHolder(
                foundation_layout.Submit('submit_and_continue', ugettext('Save and continue')),
                foundation_layout.Submit('submit', ugettext('Save')),
            ),
        )
        
        super(FoundationSampleForm, self).__init__(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        return

class SampleView(FormView):
    """
    Sample form view
    """
    form_class = FoundationSampleForm
    template_name = "crispy_forms_foundation/sample.html"
