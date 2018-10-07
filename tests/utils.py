import os
import io

from django.template import Context, Template

import django
from distutils.version import LooseVersion


# Getting Django versions compatibilities
DJANGO110_COMPAT = LooseVersion(django.get_version()) >= LooseVersion('1.10')


def write_output(filepath, pack, filename, content):
    """
    Write content to filepath+pack+filename, create filepath if it does not
    allready exists.

    This an helper to automatically rewrite HTML outputs when needed during
    development.

    Beware, using this will lose every templating instructions previously
    written in output attempts.
    """
    if (filepath and filepath != '.'
       and not os.path.exists(os.path.join(filepath, pack))):
        os.makedirs(os.path.join(filepath, pack))

    destination = os.path.join(filepath, pack, filename)

    with io.open(destination, 'w', encoding='utf-8') as f:
        f.write(content)

    return destination


def render_attempted_output(path, **kwargs):
    """
    Return compiled template from given path with given context

    It's a little hack to be able to use Django template stuff to conditionnate
    some HTML differences on Django versions.

    Template is readed as a simple file without using Django template engine
    loader select.

    Template context will contains some variables about Django versions
    compatibilities. Actually this is only about the 'required' input attribute
    behavior that is different from 1.9 (``required=""``) to
    1.10 (``required``).
    """
    context_kwargs = {
        'DJANGO110_COMPAT': DJANGO110_COMPAT,
    }
    context_kwargs.update(**kwargs)
    context = Context(context_kwargs)

    with io.open(path, 'r', encoding='utf-8') as f:
        template = Template(f.read())

    return template.render(context)


def get_rendered_template(form, **kwargs):
    """
    Return compiled template with given context where only 'form' is required.
    If crispy helper is given, it must be given as 'helper' named argument.

    Template is different depending helper is given or not in kwargs.
    """
    context_kwargs = {
        "form": form,
    }
    context_kwargs.update(**kwargs)
    context = Context(context_kwargs)

    # Use spaceless to avoid too much unuseful white spaces
    tpl = """{% spaceless %}{% load crispy_forms_tags %}"""

    if 'helper' in kwargs:
        tpl += """{% crispy form helper %}"""
    else:
        tpl += """{% crispy form %}"""

    tpl += """{% endspaceless %}"""

    template = Template(tpl)

    return template.render(context)
