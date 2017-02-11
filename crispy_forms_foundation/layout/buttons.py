"""
Buttons
=======

.. _Foundation: http://github.com/zurb/foundation

References
    * `Foundation 5 Button <http://foundation.zurb.com/sites/docs/v/5.5.3/components/buttons.html>`_;
    * `Foundation 5 Button Group <http://foundation.zurb.com/sites/docs/v/5.5.3/components/button_groups.html>`_;
    * `Foundation 6 Button <http://foundation.zurb.com/sites/docs/button.html>`_;
    * `Foundation 6 Button Group <http://foundation.zurb.com/sites/docs/button-group.html>`_;

"""  # noqa: E501
from django.template import Context
from django.template.loader import render_to_string

from crispy_forms.utils import render_field, TEMPLATE_PACK
from crispy_forms import layout as crispy_forms_layout


__all__ = [
    'ButtonHolder', 'ButtonHolderPanel', 'ButtonHolderCallout', 'ButtonGroup',
    'Button', 'Submit', 'Hidden', 'Reset',
]


class ButtonHolder(crispy_forms_layout.ButtonHolder):
    """
    It wraps fields in an element ``<div class="button-holder">``.

    This is where you should put Layout objects that render to form buttons
    like Submit. It should only hold ``HTML`` and ``BaseInput`` inherited
    objects.

    Example:

    .. sourcecode:: python

        ButtonHolder(
            HTML(<span style="display: hidden;">Information Saved</span>),
            Submit('Save', 'Save')
        )
    """
    template = "%s/layout/buttonholder.html"


class ButtonHolderPanel(ButtonHolder):
    """
    Act like ``ButtonHolder`` but add a ``panel`` class name on the main
    ``div``.
    """
    def __init__(self, field, *args, **kwargs):
        kwargs['css_class'] = kwargs.get('css_class', '')+' panel'
        super(ButtonHolderPanel, self).__init__(field, *args, **kwargs)


class ButtonHolderCallout(ButtonHolder):
    """
    Act like ``ButtonHolder`` but add a ``callout`` class name on the main
    ``div``.
    """
    def __init__(self, field, *args, **kwargs):
        kwargs['css_class'] = kwargs.get('css_class', '')+' callout'
        super(ButtonHolderPanel, self).__init__(field, *args, **kwargs)


class ButtonGroup(crispy_forms_layout.LayoutObject):
    """
    It wraps fields in an element ``<div class="button-group">``.

    This is where you should put Layout objects that render to form buttons
    like Submit. It should only hold `HTML` and `BaseInput` inherited objects.

    Example:

    .. sourcecode:: python

        ButtonGroup(
            Submit('Save', 'Save'),
            Button('Cancel', 'Cancel'),
        )
    """
    template = "%s/layout/buttongroup.html"

    def __init__(self, *fields, **kwargs):
        self.fields = list(fields)
        self.css_class = kwargs.get('css_class', None)
        self.css_id = kwargs.get('css_id', None)
        self.template = kwargs.get('template', self.template)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        field_list = []
        template = self.get_template_name(template_pack)

        for field in self.fields:
            field_list.append(
                render_field(field, form, form_style, context,
                             template_pack=template_pack)
            )

        return render_to_string(template, Context({
            'buttongroup': self,
            'field_list': field_list,
        }))


class Button(crispy_forms_layout.BaseInput):
    """
    Used to create a Submit input descriptor for the {% crispy %} template tag:

    .. sourcecode:: python

        button = Button('Button 1', 'Press Me!')

    .. note:: The first argument is also slugified and turned into the id for
              the button.
    """
    input_type = 'button'
    field_classes = 'button'


class Submit(crispy_forms_layout.BaseInput):
    """
    Used to create a Submit button descriptor for the {% crispy %} template
    tag:

    .. sourcecode:: python

        submit = Submit('Search the Site', 'search this site')

    .. note:: The first argument is also slugified and turned into the id for
              the submit button.
    """
    input_type = 'submit'
    field_classes = 'submit button'


class Hidden(crispy_forms_layout.Hidden):
    """
    Used to create a Hidden input descriptor for the {% crispy %} template tag.
    """
    input_type = 'hidden'
    field_classes = 'hidden'


class Reset(crispy_forms_layout.BaseInput):
    """
    Used to create a Reset button input descriptor for the ``{% crispy %}``
    template tag:

    .. sourcecode:: python

        reset = Reset('Reset This Form', 'Revert Me!')

    .. note:: The first argument is also slugified and turned into the id for
              the reset.
    """
    input_type = 'reset'
    field_classes = 'reset button'
