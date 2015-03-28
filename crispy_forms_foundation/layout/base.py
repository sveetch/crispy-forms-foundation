"""
Basic layout items
"""
from django.conf import settings

from crispy_forms import layout as crispy_forms_layout

TEMPLATE_PACK = getattr(settings, 'CRISPY_TEMPLATE_PACK', 'foundation-5')


class Layout(crispy_forms_layout.Layout): pass
class UneditableField(crispy_forms_layout.HTML): pass
class HTML(crispy_forms_layout.HTML): pass


class Div(crispy_forms_layout.Div):
    """
    It wraps fields in a <div>

    You can set ``css_id`` for a DOM id and ``css_class`` for a DOM class. Example:

    .. sourcecode:: python

        Div('form_field_1', 'form_field_2', css_id='div-example', css_class='divs')
    """
    template = "{0}/layout/div.html".format(TEMPLATE_PACK)


class Panel(crispy_forms_layout.Div):
    """
    Act like ``Div`` but add a ``panel`` css class.

    Example:

    .. sourcecode:: python

        Panel('form_field_1', 'form_field_2', css_id='div-example', css_class='divs')
    """
    def __init__(self, field, *args, **kwargs):
        kwargs['css_class'] = kwargs.get('css_class', '')+' panel'
        super(Panel, self).__init__(field, *args, **kwargs)
