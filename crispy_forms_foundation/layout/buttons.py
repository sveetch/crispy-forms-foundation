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
from django.template.loader import render_to_string

from crispy_forms.utils import render_field, TEMPLATE_PACK
from crispy_forms import layout as crispy_forms_layout


__all__ = [
    'ButtonHolder', 'ButtonHolderPanel', 'ButtonHolderCallout', 'ButtonGroup',
    'Button', 'Submit', 'Reset',
    'InputButton', 'InputSubmit', 'InputReset',
    'ButtonElement', 'ButtonSubmit', 'ButtonReset',
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

        buttons = render_to_string(template, {
            'buttongroup': self,
            'field_list': field_list,
        })

        return buttons


class InputButton(crispy_forms_layout.BaseInput):
    """
    Used to create a Submit input descriptor for the {% crispy %} template tag:

    .. sourcecode:: python

        button = InputButton('Button 1', 'Press Me!')

    .. note:: The first argument is also slugified and turned into the id for
              the button.
    """
    input_type = 'button'
    field_classes = 'button'


class Button(InputButton):
    """
    This is the old Button object that inherit from ``InputButton`` for
    backward compatibility.

    If you want to stand for an input button, you are invited to use
    ``InputButton`` instead to avoid problem when ``ButtonElement`` will
    become the new ``Button`` object.
    """
    pass


class InputSubmit(crispy_forms_layout.BaseInput):
    """
    Used to create a Submit button descriptor for the {% crispy %} template
    tag:

    .. sourcecode:: python

        submit = Submit('Search the Site', 'search this site')
    """
    input_type = 'submit'
    field_classes = 'submit button'


class Submit(InputSubmit):
    """
    This is the old Button object that inherit from ``InputSubmit`` for
    backward compatibility.

    If you want to stand for an input button, you are invited to use
    ``InputSubmit`` instead to avoid problem when ``ButtonSubmit`` will
    become the new ``Submit`` object.
    """
    pass


class InputReset(crispy_forms_layout.BaseInput):
    """
    Used to create a Reset button input descriptor for the ``{% crispy %}``
    template tag:

    .. sourcecode:: python

        reset = Reset('Reset This Form', 'Revert Me!')
    """
    input_type = 'reset'
    field_classes = 'reset button'


class Reset(InputReset):
    """
    This is the old Button object that inherit from ``InputReset`` for
    backward compatibility.

    If you want to stand for an input button, you are invited to use
    ``InputReset`` instead to avoid problem when ``ButtonReset`` will
    become the new ``Reset`` object.
    """
    pass


class ButtonElement(crispy_forms_layout.BaseInput):
    """
    Contrary to ``Button``, ButtonElement purpose use a ``<button>`` element
    to create a clickable form button and accept an argument to add free
    content inside element.

    Advantage of ``<button>`` is to accept almost any HTML content inside
    element.

    .. sourcecode:: python

        button = ButtonElement('name', 'value',
                               content="<span>Press Me!</span>")

    .. note::
            * First argument is for ``name`` attribute and also turned into
              the id for the button;
            * Second argument is for ``value`` attribute and also for element
              content if not given;
            * Third argument is an optional named argument ``content``, if
              given it will be appended inside element instead of ``value``.
              Content string is marked as safe so you can put anything you
              want;
    """
    template = "%s/layout/basebutton.html"
    input_type = 'button'
    field_classes = 'button'

    def __init__(self, field, *args, **kwargs):
        self.content = kwargs.pop('content', None)
        super(ButtonElement, self).__init__(field, *args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['button_content'] = self.content
        return super(ButtonElement, self).render(form, form_style, context,
                                                 template_pack)


class ButtonSubmit(ButtonElement):
    """
    Create a submit button following the ``ButtonElement`` behaviors:

    .. sourcecode:: python

        button = ButtonSubmit('search', 'go-search',
                              content="<span>Search this site!</span>")

    """
    input_type = 'submit'
    field_classes = 'submit button'


class ButtonReset(ButtonElement):
    """
    Create a reset button following the ``ButtonElement`` behaviors:

    .. sourcecode:: python

        button = ButtonReset('reset', 'revert'
                             content="<span>Revert Me!</span>")

    """
    input_type = 'reset'
    field_classes = 'reset button'
