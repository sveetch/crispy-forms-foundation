"""
Layout items for Foundation components

Inherits from the default **crispy_forms** layout objects to force templates on the 
right ``TEMPLATE_PACK`` (defined from ``settings.CRISPY_TEMPLATE_PACK``) and implements 
Foundation components.
"""
from django.conf import settings

from crispy_forms_foundation.layout.base import Div, Panel, Layout, UneditableField, HTML
from crispy_forms_foundation.layout.grid import Row, RowFluid, Column
from crispy_forms_foundation.layout.fields import (MultiWidgetField, Field, MultiField, 
                                                   SplitDateTimeField, InlineField, 
                                                   InlineJustifiedField, SwitchField, 
                                                   InlineSwitchField)
from crispy_forms_foundation.layout.buttons import (ButtonHolder, ButtonHolderPanel, 
                                                    ButtonGroup, Button, Submit, 
                                                    Hidden, Reset)
from crispy_forms_foundation.layout.containers import (Container, ContainerHolder,
                                                  Fieldset, TabItem, TabHolder, 
                                                  VerticalTabHolder, AccordionItem, 
                                                  AccordionHolder)

TEMPLATE_PACK = getattr(settings, 'CRISPY_TEMPLATE_PACK', 'foundation-5')
