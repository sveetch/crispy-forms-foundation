"""
Form container layout objects
"""
from django.conf import settings

from crispy_forms import layout as crispy_forms_layout
from crispy_forms import bootstrap as crispy_forms_bootstrap

TEMPLATE_PACK = getattr(settings, 'CRISPY_TEMPLATE_PACK', 'foundation-5')


class Container(crispy_forms_bootstrap.Container): pass
class ContainerHolder(crispy_forms_bootstrap.ContainerHolder): pass


class Fieldset(crispy_forms_layout.Fieldset):
    """
    It wraps fields in a ``<fieldset>``:

    .. sourcecode:: python

        Fieldset("Text for the legend",
            'form_field_1',
            'form_field_2'
        )

    The first parameter is the text for the fieldset legend. This text is
    context aware, so you can do things like :

    .. sourcecode:: python

        Fieldset("Data for {{ user.username }}",
            'form_field_1',
            'form_field_2'
        )
    """
    template = "{0}/layout/fieldset.html".format(TEMPLATE_PACK)


class Tab(crispy_forms_bootstrap.Tab):
    """
    Tab object. It wraps fields in a div whose default class is "tabs" and
    takes a name as first argument. Example::

        Tab('tab_name', 'form_field_1', 'form_field_2', 'form_field_3')
    """
    css_class = 'content'
    link_template = "{0}/layout/tab-link.html".format(TEMPLATE_PACK)


class TabHolder(crispy_forms_bootstrap.TabHolder):
    """
    TabHolder object. It wraps Tab objects in a container::

        TabHolder(
            Tab('form_field_1', 'form_field_2'),
            Tab('form_field_3')
        )
    """
    template = "{0}/layout/tab.html".format(TEMPLATE_PACK)


class VerticalTabHolder(TabHolder):
    """
    VerticalTabHolder appends vertical class to TabHolder container
    """
    css_class = 'vertical'


class AccordionGroup(crispy_forms_bootstrap.AccordionGroup):
    """
    Accordion Group object. It wraps given fields inside an accordion
    tab. It takes accordion tab name as first argument::

        AccordionGroup("group name", "form_field_1", "form_field_2")
    """
    template = "{0}/layout/accordion-group.html".format(TEMPLATE_PACK)

class Accordion(crispy_forms_bootstrap.Accordion):
    """
    Accordion menu object. It wraps `AccordionGroup` objects in a container::

        Accordion(
            AccordionGroup("group name", "form_field_1", "form_field_2"),
            AccordionGroup("another group name", "form_field")
    """
    template = "{0}/layout/accordion.html".format(TEMPLATE_PACK)
