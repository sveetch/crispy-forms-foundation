"""
Layout items for Foundation components.

Inherits from the default **crispy_forms** layout objects to force templates on
the right ``TEMPLATE_PACK`` (defined from ``settings.CRISPY_TEMPLATE_PACK``)
and implements Foundation components.
"""
from __future__ import absolute_import

from .base import Div, Panel, Callout, Layout, UneditableField, HTML
from .grid import Row, RowFluid, Column, GridX, GridY, Cell
from .fields import (MultiWidgetField, Field, MultiField,
                     SplitDateTimeField, InlineField,
                     InlineJustifiedField, SwitchField,
                     InlineSwitchField, FakeField, Hidden)
from .buttons import (ButtonHolder, ButtonHolderPanel, ButtonGroup,
                      Button, Submit, Reset,
                      InputButton, InputSubmit, InputReset,
                      ButtonElement, ButtonSubmit, ButtonReset)
from .containers import (Container, ContainerHolder,
                         Fieldset, TabItem, TabHolder,
                         VerticalTabHolder, AccordionItem,
                         AccordionHolder)


__all__ = [
    'Div', 'Panel', 'Callout', 'Layout', 'UneditableField', 'HTML',
    'Row', 'RowFluid', 'Column',
    'GridX', 'GridY', 'Cell',

    'Field', 'FakeField', 'Hidden',
    'MultiWidgetField', 'MultiField',
    'SplitDateTimeField',
    'InlineField', 'InlineJustifiedField', 'SwitchField', 'InlineSwitchField',

    'ButtonHolder', 'ButtonHolderPanel', 'ButtonGroup',
    'Button', 'Submit', 'Reset',
    'InputButton', 'InputSubmit', 'InputReset',
    'ButtonElement', 'ButtonSubmit', 'ButtonReset',

    'Container', 'ContainerHolder', 'Fieldset',
    'TabItem', 'TabHolder', 'VerticalTabHolder',
    'AccordionItem', 'AccordionHolder',
]
