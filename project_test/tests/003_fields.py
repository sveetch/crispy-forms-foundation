import pytest

from django import forms
from django.template import Context, Template

from crispy_forms.helper import FormHelper
from crispy_forms_foundation.layout import (Layout, InlineField,
                                            InlineSwitchField)

from forms import BasicInputForm, BoolInputForm
from utils import read_output, write_output


@pytest.mark.parametrize("foundation_version", [5])
def test_inlinefield(output_test_path, client, foundation_version):
    form = BasicInputForm()

    helper = FormHelper()
    helper.template_pack = "foundation-{}".format(foundation_version)
    helper.layout = Layout(
        InlineField('simple', label_column='large-7', input_column='large-5', label_class='foobar')
    )

    context = Context({
        "form": form,
        "form_helper": helper,
    })
    template = Template(("""{% spaceless %}{% load crispy_forms_tags %}"""
                         """{% crispy form form_helper %}{% endspaceless %}"""))

    attempted = read_output(output_test_path, "test_inlinefield.html")
    #attempted = ""

    rendered = template.render(context)

    #write_output(output_test_path, "test_inlinefield.html", rendered)

    assert rendered == attempted


@pytest.mark.parametrize("foundation_version", [5])
def test_inlineswitchfield(output_test_path, client, foundation_version):
    form = BoolInputForm()

    helper = FormHelper()
    helper.template_pack = "foundation-{}".format(foundation_version)
    helper.layout = Layout(
        InlineSwitchField('opt_in', label_column='large-8', input_column='large-4', label_class='foobar', switch_class="inline")
    )

    context = Context({
        "form": form,
        "form_helper": helper,
    })
    template = Template(("""{% spaceless %}{% load crispy_forms_tags %}"""
                         """{% crispy form form_helper %}{% endspaceless %}"""))

    attempted = read_output(output_test_path, "test_inlineswitchfield.html")
    #attempted = ""

    rendered = template.render(context)

    #write_output(output_test_path, "test_inlineswitchfield.html", rendered)

    assert rendered == attempted
