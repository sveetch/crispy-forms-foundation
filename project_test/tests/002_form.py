import pytest

from django import forms
from django.template import Context, Template

from crispy_forms.helper import FormHelper

from forms import BasicForm, LayoutForm, AdvancedForm
from utils import read_output, write_output


@pytest.mark.parametrize("foundation_version", [5])
def test_basic(output_test_path, client, foundation_version):
    basic_form = BasicForm()

    helper = FormHelper()
    helper.template_pack = "foundation-{}".format(foundation_version)

    # Use crispy templatetag to return string of generated form
    context = Context({
        "form": basic_form,
        "form_helper": helper,
    })
    template = Template(("""{% spaceless %}{% load crispy_forms_tags %}"""
                         """{% crispy form form_helper %}{% endspaceless %}"""))

    attempted = read_output(output_test_path, "test_basic.html")
    #attempted = ""

    rendered = template.render(context)

    #write_output(output_test_path, "test_basic.html", rendered)

    assert rendered == attempted


@pytest.mark.parametrize("foundation_version", [5])
def test_layout(output_test_path, client, foundation_version):
    layout_form = LayoutForm(foundation_version=foundation_version)

    # Use crispy templatetag to return string of generated form
    context = Context({"form": layout_form})
    template = Template(("""{% spaceless %}{% load crispy_forms_tags %}"""
                         """{% crispy form %}{% endspaceless %}"""))

    attempted = read_output(output_test_path, "test_layout.html")
    #attempted = ""

    rendered = template.render(context)

    #write_output(output_test_path, "test_layout.html", rendered)

    assert rendered == attempted


@pytest.mark.parametrize("foundation_version", [5])
def test_advanced(output_test_path, client, foundation_version):
    advanced_form = AdvancedForm(foundation_version=foundation_version)

    context = Context({"form": advanced_form})
    template = Template(("""{% spaceless %}{% load crispy_forms_tags %}"""
                         """{% crispy form %}{% endspaceless %}"""))

    attempted = read_output(output_test_path, "test_advanced.html")
    #attempted = ""

    rendered = template.render(context)

    #write_output(output_test_path, "test_advanced.html", rendered)

    assert rendered == attempted
