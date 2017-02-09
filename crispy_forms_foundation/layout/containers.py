"""
Form container layout objects

See :

* `Foundation forms <http://foundation.zurb.com/sites/docs/v/5.5.3/components/forms.html>`_ for fieldset component;
* `Foundation Accordion <http://foundation.zurb.com/sites/docs/v/5.5.3/components/accordion.html>`_ for accordion components;
* `Foundation Tabs <http://foundation.zurb.com/sites/docs/v/5.5.3/components/tabs.html>`_ for tabs components;
"""  # noqa: E501
from random import randint

from django.conf import settings
from django.template.loader import render_to_string

from crispy_forms import layout as crispy_forms_layout
from crispy_forms.utils import render_field
from crispy_forms import bootstrap as crispy_forms_bootstrap
from crispy_forms.compatibility import text_type


TEMPLATE_PACK = getattr(settings, 'CRISPY_TEMPLATE_PACK', 'foundation-5')


class Container(crispy_forms_bootstrap.Container):
    pass


class ContainerHolder(crispy_forms_bootstrap.ContainerHolder):
    pass


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
    template = "%s/layout/fieldset.html"


class TabHolder(crispy_forms_bootstrap.TabHolder):
    """
    Tabs holder object to wrap Tab item objects in a container:

    .. sourcecode:: python

        TabHolder(
            TabItem('My tab 1', 'form_field_1', 'form_field_2'),
            TabItem('My tab 2', 'form_field_3')
        )

    ``TabHolder`` direct children should allways be a ``TabItem`` layout item.

    The first ``TabItem`` containing a field error will be marked as
    *active* if any, else this will be just the first ``TabItem``.
    """
    template = "%s/layout/tab-holder.html"
    default_active_tab = None

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        """
        Re-implement almost the same code from crispy_forms but passing
        ``form`` instance to item ``render_link`` method.
        """
        links, content = '', ''
        for tab in self.fields:
            tab.active = False

        # Activate item
        self.open_target_group_for_form(form)

        for tab in self.fields:
            content += render_field(
                tab, form, form_style, context, template_pack=template_pack
            )
            links += tab.render_link(form, template_pack)

        context.update({
            'tabs': self,
            'links': links,
            'content': content
        })

        template = self.get_template_name(template_pack)
        return render_to_string(template, context.flatten())


class VerticalTabHolder(TabHolder):
    """
    VerticalTabHolder appends vertical class to TabHolder container
    """
    css_class = 'vertical'


class TabItem(crispy_forms_bootstrap.Tab):
    """
    Tab item object. It wraps fields in a div whose default class is "tabs" and
    takes a name as first argument.

    The item name is also slugified to build an id for the tab if you don't
    define it using ``css_id`` argument.

    Example:

    .. sourcecode:: python

        TabItem('My tab', 'form_field_1', 'form_field_2', 'form_field_3')

    ``TabItem`` layout item has no real utility out of a ``TabHolder``.
    """
    css_class = 'content'
    link_template = "%s/layout/tab-item.html"

    def has_errors(self, form):
        """
        Find tab fields are listed as invalid
        """
        return any([fieldname_error for fieldname_error in form.errors.keys()
                    if fieldname_error in self])

    def render_link(self, form, template_pack=TEMPLATE_PACK, **kwargs):
        """
        Render the link for the tab-pane. It must be called after render so
        ``css_class`` is updated with ``active`` class name if needed.
        """
        link_template = self.link_template % template_pack
        return render_to_string(link_template,
                                {
                                    'link': self,
                                    'item_has_errors': self.has_errors(form)
                                })


class AccordionHolder(crispy_forms_bootstrap.Accordion):
    """
    Accordion items holder object to wrap Accordion item objects in a
    container:

    .. sourcecode:: python

        AccordionHolder(
            AccordionItem("group name", "form_field_1", "form_field_2"),
            AccordionItem("another group name", "form_field"),
        )

    ``AccordionHolder`` direct children should allways be a ``AccordionItem``
    layout item.

    The first ``AccordionItem`` containing a field error will be marked as
    *active* if any, else this will be just the first ``AccordionItem``.
    """
    template = "%s/layout/accordion-holder.html"

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK,
               **kwargs):
        """
        Re-implement almost the same code from crispy_forms but using
        ``form`` instance to catch field errors.
        """
        content = ''

        # accordion group needs the parent div id to set `data-parent` (I don't
        # know why). This needs to be a unique id
        if not self.css_id:
            self.css_id = "-".join(["accordion",
                                    text_type(randint(1000, 9999))])

        # Active first 'AccordionItem' containing a field error if any, else
        # active first holder item
        self.open_target_group_for_form(form)

        for group in self.fields:
            group.data_parent = self.css_id
            group.item_has_errors = any([fieldname_error for fieldname_error in
                                         form.errors.keys()
                                         if fieldname_error in group])
            content += render_field(
                group, form, form_style, context, template_pack=template_pack,
                **kwargs
            )

        template = self.get_template_name(template_pack)
        context.update({'accordion': self, 'content': content})

        return render_to_string(template, context.flatten())


class AccordionItem(crispy_forms_bootstrap.AccordionGroup):
    """
    Accordion item object. It wraps given fields inside an accordion
    tab. It takes accordion tab name as first argument.

    The item name is also slugified to build an id for the tab if you don't
    define it using ``css_id`` argument.

    Example:

    .. sourcecode:: python

        AccordionItem("group name", "form_field_1", "form_field_2")
    """
    template = "%s/layout/accordion-item.html"
