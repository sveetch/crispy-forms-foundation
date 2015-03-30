"""
Form container layout objects

See :

* `Foundation forms <http://foundation.zurb.com/docs/components/forms.html>`_ for fieldset component;
* `Foundation Accordion <http://foundation.zurb.com/docs/components/accordion.html>`_ for accordion components;
* `Foundation Tabs <http://foundation.zurb.com/docs/components/tabs.html>`_ for tabs components;
"""
from random import randint

from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string

from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import render_field
from crispy_forms import bootstrap as crispy_forms_bootstrap
from crispy_forms.compatibility import text_type

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


class TabHolder(crispy_forms_bootstrap.TabHolder):
    """
    Tabs holder object to wrap Tab item objects in a container:

    .. sourcecode:: python

        TabHolder(
            TabItem('My tab 1', 'form_field_1', 'form_field_2'),
            TabItem('My tab 2', 'form_field_3')
        )
    
    ``TabHolder`` directl children should allways be a ``TabItem`` layout item.
    """
    template = "{0}/layout/tab-holder.html".format(TEMPLATE_PACK)

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

class TabItem(crispy_forms_bootstrap.Tab):
    """
    Tab item object. It wraps fields in a div whose default class is "tabs" and
    takes a name as first argument. 
    
    The item name is also slugified to build an id for the tab if you don't define 
    it using ``css_id`` argument.
    
    Example:

    .. sourcecode:: python

        TabItem('My tab', 'form_field_1', 'form_field_2', 'form_field_3')
    
    ``TabItem`` layout item has no real utility out of a ``TabHolder``.
    """
    css_class = 'content'
    link_template = "{0}/layout/tab-item.html".format(TEMPLATE_PACK)

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
        return render_to_string(self.link_template, Context({'link': self, 'item_has_errors': self.has_errors(form)}))


class AccordionHolder(crispy_forms_bootstrap.Accordion):
    """
    Accordion items holder object to wrap Accordion item objects in a container:

    .. sourcecode:: python

        AccordionHolder(
            AccordionItem("group name", "form_field_1", "form_field_2"),
            AccordionItem("another group name", "form_field"),
        )
    """
    template = "{0}/layout/accordion-holder.html".format(TEMPLATE_PACK)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        content = ''

        # accordion group needs the parent div id to set `data-parent` (I don't
        # know why). This needs to be a unique id
        if not self.css_id:
            self.css_id = "-".join(["accordion", text_type(randint(1000, 9999))])

        # first group with errors or first groupt will be visible, others will be collapsed
        self.first_container_with_errors(form.errors.keys()).active = True

        for group in self.fields:
            group.data_parent = self.css_id
            group.item_has_errors = any([fieldname_error for fieldname_error in form.errors.keys() if fieldname_error in group])
            content += render_field(
                group, form, form_style, context, template_pack=template_pack
            )

        return render_to_string(
            self.template,
            Context({'accordion': self, 'content': content})
        )

class AccordionItem(crispy_forms_bootstrap.AccordionGroup):
    """
    Accordion item object. It wraps given fields inside an accordion
    tab. It takes accordion tab name as first argument.
    
    The item name is also slugified to build an id for the tab if you don't define 
    it using ``css_id`` argument.

    Example:

    .. sourcecode:: python

        AccordionItem("group name", "form_field_1", "form_field_2")
    """
    template = "{0}/layout/accordion-item.html".format(TEMPLATE_PACK)
