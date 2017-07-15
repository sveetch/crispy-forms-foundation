"""
Fields
======

.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Foundation: http://github.com/zurb/foundation
.. _crispy-forms-foundation-demo: https://github.com/sveetch/crispy-forms-foundation-demo
.. _Abide: http://foundation.zurb.com/docs/components/abide.html

References
    * `Foundation 5 Forms <http://foundation.zurb.com/sites/docs/v/5.5.3/components/forms.html>`_;
    * `Foundation 5 Switches <http://foundation.zurb.com/sites/docs/v/5.5.3/components/switch.html>`_;
    * `Foundation 6 Forms <http://foundation.zurb.com/sites/docs/forms.html>`_;
    * `Foundation 6 Switches <http://foundation.zurb.com/sites/docs/switch.html>`_;

"""  # noqa: E501
from crispy_forms.utils import render_field, TEMPLATE_PACK
from crispy_forms import layout as crispy_forms_layout


__all__ = [
    'Field', 'FakeField', 'Hidden', 'MultiWidgetField', 'MultiField',
    'SplitDateTimeField', 'InlineField', 'InlineJustifiedField', 'SwitchField',
    'InlineSwitchField',
]


class Field(crispy_forms_layout.Field):
    """
    Layout object, contain one field name and you can add attributes to it
    easily. For setting class attributes, you need to use ``css_class``,
    because ``class`` is a reserved Python keyword.

    Example:

    .. sourcecode:: python

        Field('field_name', style="color: #333;", css_class="whatever",
              id="field_name")
    """
    template = "%s/field.html"


class FakeField(Field):
    """
    Fake field is intended to be used with some app that does not honor field
    ID on the input element alike ``django-recaptcha`` that build a textarea
    with a dummy ID attribute. This leads to HTML validation error.

    Fake field works as basic Field object except a ``fake_field`` variable is
    passed to the template context.

    Actually the only difference with a ``Field`` is label element drops
    ``for`` attribute.

    You should use this field in last resort.
    """
    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['fake_field'] = True
        return super(FakeField, self).render(form, form_style, context,
                                             template_pack)


class Hidden(crispy_forms_layout.Hidden):
    """
    Hidden field. Work as basic Field except the ``hidden`` value for ``type``
    attribute.
    """
    input_type = 'hidden'
    field_classes = 'hidden'


class MultiWidgetField(crispy_forms_layout.MultiWidgetField):
    pass


class MultiField(crispy_forms_layout.MultiField):
    """
    MultiField container. Render to a MultiField
    """
    template = "%s/layout/multifield.html"
    field_template = "%s/multifield.html"


class SplitDateTimeField(Field):
    """
    Just an inherit from ``crispy_forms.layout.Field`` to have a common Field
    for displaying field with the ``django.forms.extra.SplitDateTimeWidget``
    widget.

    Simply use a specific template
    """
    template = "%s/layout/splitdatetime_field.html"


class InlineField(Field):
    """
    Layout object for rendering an inline field with Foundation

    Example:

    .. sourcecode:: python

        InlineField('field_name')

    Or:

    .. sourcecode:: python

        InlineField('field_name', label_column='large-8',
                    input_column='large-4', label_class='')

    ``label_column``, ``input_column``, ``label_class``, are optional argument.
    """
    template = "%s/layout/inline_field.html"

    def __init__(self, field, label_column='large-3', input_column='large-9',
                 label_class='', *args, **kwargs):
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
        template = self.get_template_name(template_pack)
        for field in self.fields:
            html += render_field(field, form, form_style, context,
                                 template=template, attrs=self.attrs,
                                 template_pack=template_pack)
        return html


class InlineJustifiedField(InlineField):
    """
    Same as InlineField but default is to be right aligned with a vertical
    padding
    """
    def __init__(self, field, *args, **kwargs):
        default = 'middle text-right inline'
        kwargs['label_class'] = kwargs.get('label_class', None) or default
        super(InlineJustifiedField, self).__init__(field, *args, **kwargs)


class SwitchField(Field):
    """
    A specific field to use Foundation form switches

    You must only use this with a checkbox field and this is a *raw* usage of
    this Foundation element, you should see ``InlineSwitchField`` instead.

    Example:

    .. sourcecode:: python

        SwitchField('field_name', style="color: #333;", css_class="whatever",
                    id="field_name")
    """
    template = "%s/switch.html"

    def __init__(self, field, *args, **kwargs):
        self.switch_class = ['switch'] + kwargs.pop('switch_class', '').split()
        kwargs['class'] = (kwargs.pop('class', '') + ' switch-input').strip()

        super(SwitchField, self).__init__(field, *args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['switch_class'] = " ".join(self.switch_class)
        return super(SwitchField, self).render(form, form_style, context,
                                               template_pack)


class InlineSwitchField(InlineField):
    """
    Like ``SwitchField`` it use Foundation form switches with checkbox field
    but within an ``InlineField``

    Contrary to ``SwitchField`` this play nice with the label to be able to
    display it (as Foundation form switches default behavior is to hide the
    label text)

    Example:

    .. sourcecode:: python

        InlineSwitchField('field_name')

    Or:

    .. sourcecode:: python

        InlineSwitchField('field_name', label_column='large-8',
                          input_column='large-4', label_class='',
                          switch_class="inline")

    ``label_column``, ``input_column``, ``label_class``, ``switch_class`` are
    optional argument.
    """
    template = "%s/inline_switch.html"

    def __init__(self, field, *args, **kwargs):
        self.switch_class = ['switch']+kwargs.pop('switch_class', '').split()
        kwargs['label_column'] = kwargs.pop('label_column', 'large-8')
        kwargs['input_column'] = kwargs.pop('input_column', 'large-4')
        kwargs['class'] = (kwargs.pop('class', '') + ' switch-input').strip()

        super(InlineSwitchField, self).__init__(field, *args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['switch_class'] = " ".join(self.switch_class)
        return super(InlineSwitchField, self).render(form, form_style, context,
                                                     template_pack)
