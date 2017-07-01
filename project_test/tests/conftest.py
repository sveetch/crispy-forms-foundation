"""
Some fixture methods
"""
import os
import pytest

from django.template import Context, Template

from crispy_forms.helper import FormHelper


def get_rendered_template(form, **kwargs):
    """
    Return compiled template with given context where only 'form' is required.
    If crispy helper is given, it must be given as 'helper' named argument.

    Template is different depending helper is given or not.
    """
    context_kwargs = {
        "form": form,
    }
    context_kwargs.update(**kwargs)
    context = Context(context_kwargs)

    tpl = """{% spaceless %}{% load crispy_forms_tags %}"""
    if 'helper' in kwargs:
        tpl += """{% crispy form helper %}"""
    else:
        tpl += """{% crispy form %}"""
    tpl += """{% endspaceless %}"""
    template = Template(tpl)

    return template.render(context)


@pytest.fixture(scope='session')
def output_test_path(pytestconfig):
    """Return absolute path to test outputs directory"""
    #return os.path.join(pytestconfig.rootdir.strpath, 'project_test', 'tests', 'output')
    return os.path.join(pytestconfig.rootdir.strpath, 'tests', 'output')


@pytest.fixture(scope='session')
def rendered_template():
    """
    Return callable function to render template
    """
    return get_rendered_template


@pytest.fixture(scope='function', params=[
    "foundation-5",
    "foundation-6"
])
def helper(request):
    """
    Parametrized fixture to return helper configured for a template pack
    """
    helper = FormHelper()
    helper.template_pack = request.param

    return helper
