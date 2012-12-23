"""
Inherits from the "uni_form" Layout objects to force templates on "foundation/..." and 
use of Foundation CSS classes

Also the templates are more clean that the included ones from crispy_forms which produce 
too much spaces and newlines in the final HTML.

TODO: * Add some more element like prefixed/suffixed inputs, like the bootstrap layouts;
"""
from django.conf import settings

from crispy_forms.utils import render_field
from crispy_forms import layout as crispy_forms_layout

TEMPLATE_PACK = getattr(settings, 'CRISPY_TEMPLATE_PACK', 'foundation')

class Layout(crispy_forms_layout.Layout): pass
class UneditableField(crispy_forms_layout.HTML): pass
class HTML(crispy_forms_layout.HTML): pass
class MultiWidgetField(crispy_forms_layout.MultiWidgetField): pass

class ButtonHolder(crispy_forms_layout.ButtonHolder):
    """
    Layout object. It wraps fields in a <div class="buttonHolder">

    This is where you should put Layout objects that render to form buttons like Submit.
    It should only hold `HTML` and `BaseInput` inherited objects.

    Example::

        ButtonHolder(
            HTML(<span style="display: hidden;">Information Saved</span>),
            Submit('Save', 'Save')
        )
    """
    template = "foundation/layout/buttonholder.html"


class Submit(crispy_forms_layout.Submit):
    """
    Used to create a Submit button descriptor for the {% crispy %} template tag::

        submit = Submit('Search the Site', 'search this site')

    .. note:: The first argument is also slugified and turned into the id for the submit button.
    """
    input_type = 'submit'
    field_classes = 'submit button'


class Button(crispy_forms_layout.Button):
    """
    Used to create a Submit input descriptor for the {% crispy %} template tag::

        button = Button('Button 1', 'Press Me!')

    .. note:: The first argument is also slugified and turned into the id for the button.
    """
    input_type = 'button'
    field_classes = 'button'


class Hidden(crispy_forms_layout.Hidden):
    """
    Used to create a Hidden input descriptor for the {% crispy %} template tag.
    """
    input_type = 'hidden'
    field_classes = 'hidden'


class Reset(crispy_forms_layout.Reset):
    """
    Used to create a Reset button input descriptor for the {% crispy %} template tag::

        reset = Reset('Reset This Form', 'Revert Me!')

    .. note:: The first argument is also slugified and turned into the id for the reset.
    """
    input_type = 'reset'
    field_classes = 'reset secondary button'


class Fieldset(crispy_forms_layout.Fieldset):
    """
    Layout object. It wraps fields in a <fieldset>

    Example::

        Fieldset("Text for the legend",
            'form_field_1',
            'form_field_2'
        )

    The first parameter is the text for the fieldset legend. This text is context aware,
    so you can do things like::

        Fieldset("Data for {{ user.username }}",
            'form_field_1',
            'form_field_2'
        )
    """
    template = "foundation/layout/fieldset.html"


class MultiField(crispy_forms_layout.MultiField):
    """ MultiField container. Renders to a MultiField <div> """
    template = "foundation/layout/multifield.html"
    field_template = "foundation/multifield.html"


class Div(crispy_forms_layout.Div):
    """
    Layout object. It wraps fields in a <div>

    You can set `css_id` for a DOM id and `css_class` for a DOM class. Example::

        Div('form_field_1', 'form_field_2', css_id='div-example', css_class='divs')
    """
    template = "foundation/layout/div.html"


class Row(Div):
    """
    Layout object. It wraps fields in a div whose default class is "row". Example::

        Row('form_field_1', 'form_field_2', 'form_field_3')
    """
    css_class = 'row'

class RowFluid(Row):
    """
    Layout object. It wraps fields in a div whose default class is "row row-fluid". Example::

        RowFluid('form_field_1', 'form_field_2', 'form_field_3')
    """
    css_class = 'row row-fluid'


class Column(Div):
    """
    Layout object. It wraps fields in a div whose default class is "formColumn". Example::

        Column('form_field_1', 'form_field_2')
    """
    css_class = 'columns'


class Field(crispy_forms_layout.Field):
    """
    Layout object, It contains one field name, and you can add attributes to it easily.
    For setting class attributes, you need to use `css_class`, as `class` is a Python keyword.

    Example::

        Field('field_name', style="color: #333;", css_class="whatever", id="field_name")
    """
    template = "%s/field.html" % TEMPLATE_PACK


class SplitDateTimeField(Field):
    """
    Just an inherit from ``crispy_forms.layout.Field`` to have a common Field for 
    displaying field with the ``django.forms.extra.SplitDateTimeWidget`` widget.
    
    Simply use a specific template
    """
    template="foundation/layout/splitdatetime_field.html"

    #def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        #html = ''
        #for field in self.fields:
            #html += render_field(field, form, form_style, context, template=self.template, attrs=self.attrs, template_pack=template_pack)
        #return html
