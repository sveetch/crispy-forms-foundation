"""
Field layout items

See :

* `Foundation forms <http://foundation.zurb.com/docs/components/forms.html>`_ for input field components;
* `Foundation Switches <http://foundation.zurb.com/docs/components/switch.html>`_ for switches components;
"""
from django.conf import settings

from crispy_forms.utils import render_field
from crispy_forms import layout as crispy_forms_layout

TEMPLATE_PACK = getattr(settings, 'CRISPY_TEMPLATE_PACK', 'foundation-5')


class MultiWidgetField(crispy_forms_layout.MultiWidgetField): pass


class Field(crispy_forms_layout.Field):
    """
    Layout object, It contains one field name, and you can add attributes to it easily.
    For setting class attributes, you need to use `css_class`, as `class` is a Python keyword.

    Example:

    .. sourcecode:: python

        Field('field_name', style="color: #333;", css_class="whatever", id="field_name")
    """
    template = "{0}/field.html".format(TEMPLATE_PACK)


class MultiField(crispy_forms_layout.MultiField):
    """
    MultiField container. Renders to a MultiField
    """
    template = "{0}/layout/multifield.html".format(TEMPLATE_PACK)
    field_template = "{0}/multifield.html".format(TEMPLATE_PACK)


class SplitDateTimeField(Field):
    """
    Just an inherit from ``crispy_forms.layout.Field`` to have a common Field for
    displaying field with the ``django.forms.extra.SplitDateTimeWidget`` widget.

    Simply use a specific template
    """
    template="{0}/layout/splitdatetime_field.html".format(TEMPLATE_PACK)


class InlineField(Field):
    """
    Layout object for rendering an inline field with Foundation

    Example:

    .. sourcecode:: python

        InlineField('field_name')

    Or:

    .. sourcecode:: python

        InlineField('field_name', label_column='large-8', input_column='large-4', label_class='')

    ``label_column``, ``input_column``, ``label_class``, are optional argument.
    """
    template = "{0}/layout/inline_field.html".format(TEMPLATE_PACK)

    def __init__(self, field, label_column='large-3', input_column='large-9', label_class='', *args, **kwargs):
        self.field = field
        self.label_column = label_column+' columns'
        self.input_column = input_column+' columns'
        self.label_class = label_class

        super(InlineField, self).__init__(field, *args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['label_column'] = self.label_column
        context['input_column'] = self.input_column
        context['label_class'] = self.label_class

        html = ''
        for field in self.fields:
            html += render_field(field, form, form_style, context, template=self.template, attrs=self.attrs, template_pack=template_pack)
        return html


class InlineJustifiedField(InlineField):
    """
    Same as InlineField but default is to be right aligned with a vertical padding
    """
    def __init__(self, field, *args, **kwargs):
        kwargs['label_class'] = kwargs.get('label_class', None) or 'right inline'
        super(InlineJustifiedField, self).__init__(field, *args, **kwargs)


class SwitchField(crispy_forms_layout.Field):
    """
    A specific field to use Foundation form switches

    You should only use this with a checkbox field and this is a *raw* usage of this
    Foundation element, you should see ``InlineSwitchField`` instead.

    Example:

    .. sourcecode:: python

        SwitchField('field_name', style="color: #333;", css_class="whatever", id="field_name")
    """
    template = "{0}/switch.html".format(TEMPLATE_PACK)

    def __init__(self, field, *args, **kwargs):
        self.switch_class = ['switch'] + kwargs.pop('switch_class', '').split()
        super(SwitchField, self).__init__(field, *args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['switch_class'] = " ".join(self.switch_class)
        return super(SwitchField, self).render(form, form_style, context, template_pack)


class InlineSwitchField(InlineField):
    """
    Like ``SwitchField`` it use Foundation form switches with checkbox field but within an ``InlineField``

    Contrary to ``SwitchField`` this play nice with the label to be able to display it (as Foundation form switches default behavior is to hide the label text)

    Example:

    .. sourcecode:: python

        InlineSwitchField('field_name')

    Or:

    .. sourcecode:: python

        InlineSwitchField('field_name', label_column='large-8', input_column='large-4', label_class='', switch_class="inline")

    ``label_column``, ``input_column``, ``label_class``, ``switch_class`` are optional argument.
    """
    template = "{0}/inline_switch.html".format(TEMPLATE_PACK)

    def __init__(self, field, *args, **kwargs):
        self.switch_class = ['switch']+kwargs.pop('switch_class', '').split()
        kwargs['label_column'] = kwargs.pop('label_column', 'large-8')
        kwargs['input_column'] = kwargs.pop('input_column', 'large-4')

        super(InlineSwitchField, self).__init__(field, *args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['switch_class'] = " ".join(self.switch_class)
        return super(InlineSwitchField, self).render(form, form_style, context, template_pack)
