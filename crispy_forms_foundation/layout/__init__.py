"""
Layout items for Foundation components.

Inherits from the default **crispy_forms** layout objects to force templates on
the right ``TEMPLATE_PACK`` (defined from ``settings.CRISPY_TEMPLATE_PACK``)
and implements Foundation components.
"""
from __future__ import absolute_import

from .base import Div, Panel, Callout, Layout, UneditableField, HTML
from .grid import Row, RowFluid, Column

from .fields import (  # noqa: F401
    MultiWidgetField, Field, MultiField,
    SplitDateTimeField, InlineField,
    InlineJustifiedField, SwitchField,
    InlineSwitchField, FakeField, Hidden
)
from .buttons import (  # noqa: F401
    ButtonHolder, ButtonHolderPanel, ButtonGroup,
    Button, Submit, Reset,
    InputButton, InputSubmit, InputReset,
    ButtonElement, ButtonSubmit, ButtonReset
)
from .containers import (  # noqa: F401
    Container, ContainerHolder,
    Fieldset, TabItem, TabHolder,
    VerticalTabHolder, AccordionItem,
    AccordionHolder
)


__all__ = [
    'Div', 'Panel', 'Callout', 'Layout', 'UneditableField', 'HTML',
    'Row', 'RowFluid', 'Column',

    'Field', 'FakeField', 'Hidden',
    'MultiWidgetField', 'MultiField',
    'SplitDateTimeField',
    'InlineField', 'InlineJustifiedField', 'SwitchField', 'InlineSwitchField'

    'ButtonHolder', 'ButtonHolderPanel', 'ButtonGroup',
    'Button', 'Submit', 'Reset',
    'InputButton', 'InputSubmit', 'InputReset',
    'ButtonElement', 'ButtonSubmit', 'ButtonReset',

    'Container', 'ContainerHolder', 'Fieldset',
    'TabItem', 'TabHolder', 'VerticalTabHolder',
    'AccordionItem', 'AccordionHolder',
]
