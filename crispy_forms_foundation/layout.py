"""
Inherits from the "uni_form" Layout objects to force templates on TEMPLATE_PACK and 
use of Foundation CSS classes

Also the templates are more clean that the included ones from crispy_forms which produce 
too much spaces and newlines in the final HTML.
"""
from django.conf import settings
from django.template import Context
from django.template.loader import render_to_string

from crispy_forms.utils import render_field
from crispy_forms import layout as crispy_forms_layout

TEMPLATE_PACK = getattr(settings, 'CRISPY_TEMPLATE_PACK', 'foundation-5')

class Layout(crispy_forms_layout.Layout): pass
class UneditableField(crispy_forms_layout.HTML): pass
class HTML(crispy_forms_layout.HTML): pass
class MultiWidgetField(crispy_forms_layout.MultiWidgetField): pass


class Div(crispy_forms_layout.Div):
    """
    Layout object. It wraps fields in a <div>

    You can set `css_id` for a DOM id and `css_class` for a DOM class. Example : ::

        Div('form_field_1', 'form_field_2', css_id='div-example', css_class='divs')
    """
    template = "{0}/layout/div.html".format(TEMPLATE_PACK)


class Row(Div):
    """
    Layout object. It wraps fields in a div whose default class is "row". Example : ::

        Row('form_field_1', 'form_field_2', 'form_field_3')
    """
    css_class = 'row'

class RowFluid(Row):
    """
    Layout object. It wraps fields in a div whose default class is "row row-fluid". Example : ::

        RowFluid('form_field_1', 'form_field_2', 'form_field_3')
    """
    css_class = 'row row-fluid'


class Column(Div):
    """
    Layout object. It wraps fields in a div whose default class is "formColumn". Example : ::

        Column('form_field_1', 'form_field_2')
    
    Or : ::

        Column('form_field_1', 'form_field_2', css_class='small-12 large-6')
    
    If not defined, CSS class will default to 'large-12 columns'. ``columns`` class is 
    always appended, so you don't need to specify it.
    """
    css_class = 'columns'

    def __init__(self, field, *args, **kwargs):
        self.field = field
        if 'css_class' not in kwargs:
            kwargs['css_class'] = 'large-12'

        super(Column, self).__init__(field, *args, **kwargs)


class Fieldset(crispy_forms_layout.Fieldset):
    """
    Layout object. It wraps fields in a <fieldset>

    Example::

        Fieldset("Text for the legend",
            'form_field_1',
            'form_field_2'
        )

    The first parameter is the text for the fieldset legend. This text is context aware,
    so you can do things like : ::

        Fieldset("Data for {{ user.username }}",
            'form_field_1',
            'form_field_2'
        )
    """
    template = "{0}/layout/fieldset.html".format(TEMPLATE_PACK)


class Field(crispy_forms_layout.Field):
    """
    Layout object, It contains one field name, and you can add attributes to it easily.
    For setting class attributes, you need to use `css_class`, as `class` is a Python keyword.

    Example::

        Field('field_name', style="color: #333;", css_class="whatever", id="field_name")
    """
    template = "{0}/field.html".format(TEMPLATE_PACK)


class MultiField(crispy_forms_layout.MultiField):
    """ MultiField container. Renders to a MultiField <d.format(TEMPLATE_PACK)iv> """
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

    Example::

        InlineField('field_name')
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
    
    You should only use this with a checkbox field

    Example::

        SwitchField('field_name', style="color: #333;", css_class="whatever", id="field_name")
    """
    template = "{0}/switch.html".format(TEMPLATE_PACK)
    
    def __init__(self, field, *args, **kwargs):
        self.switch_class = ['switch']+kwargs.pop('switch_class', '').split()

        super(SwitchField, self).__init__(field, *args, **kwargs)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        context['switch_class'] = " ".join(self.switch_class)
        return super(SwitchField, self).render(form, form_style, context, template_pack)


class ButtonHolder(crispy_forms_layout.ButtonHolder):
    """
    Layout object. It wraps fields in a <div class="button-holder">

    This is where you should put Layout objects that render to form buttons like Submit.
    It should only hold `HTML` and `BaseInput` inherited objects.

    Example::

        ButtonHolder(
            HTML(<span style="display: hidden;">Information Saved</span>),
            Submit('Save', 'Save')
        )
    """
    template = "{0}/layout/buttonholder.html".format(TEMPLATE_PACK)


class ButtonHolderPanel(ButtonHolder):
    """
    Act like ``ButtonHolder`` but add a ``panel`` css class on the main div
    """
    def __init__(self, field, *args, **kwargs):
        kwargs['css_class'] = kwargs.get('css_class', '')+' panel'
        super(ButtonHolderPanel, self).__init__(field, *args, **kwargs)


class ButtonGroup(crispy_forms_layout.LayoutObject):
    """
    Layout object. It wraps fields in a <ul class="button-group">

    This is where you should put Layout objects that render to form buttons like Submit.
    It should only hold `HTML` and `BaseInput` inherited objects.

    Example: ::

        ButtonGroup(
            Submit('Save', 'Save'),
            Button('Cancel', 'Cancel'),
        )
    """
    template = "{0}/layout/buttongroup.html".format(TEMPLATE_PACK)

    def __init__(self, *fields, **kwargs):
        self.fields = list(fields)
        self.css_class = kwargs.get('css_class', None)
        self.css_id = kwargs.get('css_id', None)
        self.template = kwargs.get('template', self.template)

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        field_list = []
        for field in self.fields:
            field_list.append(
                render_field(field, form, form_style, context, template_pack=template_pack)
            )

        return render_to_string(self.template, Context({'buttongroup': self, 'field_list': field_list}))


class Panel(crispy_forms_layout.Div):
    """
    Act like ``Div`` but add a ``panel`` css class.
    
    Example: ::

        Panel('form_field_1', 'form_field_2', css_id='div-example', css_class='divs')
    """
    def __init__(self, field, *args, **kwargs):
        kwargs['css_class'] = kwargs.get('css_class', '')+' panel'
        super(Panel, self).__init__(field, *args, **kwargs)


class Button(crispy_forms_layout.Button):
    """
    Used to create a Submit input descriptor for the {% crispy %} template tag : ::

        button = Button('Button 1', 'Press Me!')

    .. note:: The first argument is also slugified and turned into the id for the button.
    """
    input_type = 'button'
    field_classes = 'button'


class Submit(crispy_forms_layout.Submit):
    """
    Used to create a Submit button descriptor for the {% crispy %} template tag : ::

        submit = Submit('Search the Site', 'search this site')

    .. note:: The first argument is also slugified and turned into the id for the submit button.
    """
    input_type = 'submit'
    field_classes = 'submit button'


class Hidden(crispy_forms_layout.Hidden):
    """
    Used to create a Hidden input descriptor for the {% crispy %} template tag.
    """
    input_type = 'hidden'
    field_classes = 'hidden'


class Reset(crispy_forms_layout.Reset):
    """
    Used to create a Reset button input descriptor for the {% crispy %} template tag : ::

        reset = Reset('Reset This Form', 'Revert Me!')

    .. note:: The first argument is also slugified and turned into the id for the reset.
    """
    input_type = 'reset'
    field_classes = 'reset button'
