"""
Form container layout objects

See :

* `Foundation forms <http://foundation.zurb.com/docs/components/forms.html>`_ for fieldset component;
* `Foundation Accordion <http://foundation.zurb.com/docs/components/accordion.html>`_ for accordion components;
* `Foundation Tabs <http://foundation.zurb.com/docs/components/tabs.html>`_ for tabs components;
"""
from django.conf import settings

from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import render_field
from crispy_forms import bootstrap as crispy_forms_bootstrap
from django.template import Context
from django.template.loader import render_to_string

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

    def has_errors(self, form):
        """
        Find tab fields are listed as invalid
        """
        return any([fieldname_error for fieldname_error in form.errors.keys() if fieldname_error in self])

    def render_link(self, form):
        """
        Render the link for the tab-pane. It must be called after render so css_class is updated
        with active if needed.
        """
        return render_to_string(self.link_template, Context({'link': self, 'tab_has_errors': self.has_errors(form)}))

class TabHolder(crispy_forms_bootstrap.TabHolder):
    """
    TabHolder object. It wraps Tab objects in a container::

        TabHolder(
            Tab('form_field_1', 'form_field_2'),
            Tab('form_field_3')
        )
    """
    template = "{0}/layout/tab.html".format(TEMPLATE_PACK)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        links, content = '', ''
        for tab in self.fields:
            tab.active = False

        # The first tab with errors will be active
        self.first_container_with_errors(form.errors.keys()).active = True

        for tab in self.fields:
            content += render_field(
                tab, form, form_style, context, template_pack=template_pack
            )
            links += tab.render_link(form)

        return render_to_string(self.template, Context({
            'tabs': self, 'links': links, 'content': content
        }))


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
            AccordionGroup("another group name", "form_field"),
        )
    """
    template = "{0}/layout/accordion.html".format(TEMPLATE_PACK)
