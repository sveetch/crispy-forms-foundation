"""
Forms crispies items
"""
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import (
    Layout, Fieldset, HTML, Row, Column, Panel, 
    ButtonHolder, ButtonHolderPanel, ButtonGroup, Button, Submit, 
    InlineField, InlineJustifiedField, 
    SwitchField, InlineSwitchField
)

def part_1_crispies():
    return [
        Row(
            Column('full_input'),
        ),
        Row(
            Column(
                Row(
                    Column(
                        'column_input_1',
                        css_class='large-4'
                    ),
                    Column(
                        'column_input_2',
                        css_class='large-4'
                    ),
                    Column(
                        'column_input_3',
                        css_class='large-4'
                    ),
                )
            ),
        ),
    ]


def part_2_crispies():
    return [
        Row(
            Column(
                'select_input',
                css_class='large-12'
            ),
        ),
        Row(
            Column(
                'radio_input',
                css_class='large-4'
            ),
            Column(
                'checkbox_input',
                css_class='large-4'
            ),
            Column(
                Row(
                    Column(
                        SwitchField('checkbox_switch_input_1', switch_class="round tiny"),
                        css_class='small-3'
                    ),
                    Column(
                        HTML('<label>Checkbox with a switch field</label>'),
                        css_class='small-9'
                    ),
                ),
                Row(
                    Column(
                        InlineSwitchField('checkbox_switch_input_2'),
                    ),
                ),
                css_class='large-4'
            ),
        ),
    ]


def part_3_crispies():
    return [
        Row(
            Column('textarea_input'),
        ),
    ]


def part_4_crispies():
    return [
        InlineField('inlinefield_input'),
        InlineJustifiedField('inlinejustifiedfield_input'),
    ]


def buttons_crispies():
    return [
        Row(
            Column(
                ButtonGroup(
                    Submit('submit', _('Submit'), css_class='success'),
                    Button('cancel', _('Cancel')),
                    Button('dummy', _('Delete'), css_class='alert'),
                    css_class='radius right'
                ),
                css_class='clearfix'
            ),
        ),
        Row(
            Column(
                Panel(
                    ButtonGroup(
                        Submit('submit', _('Submit'), css_class='success'),
                        Button('cancel', _('Cancel')),
                        Button('dummy', _('Delete'), css_class='alert'),
                        css_class='radius right'
                    ),
                    css_class='clearfix'
                )
            ),
        ),
    ]
