import pytest

from crispy_forms_foundation.layout import (Layout, Row, Column, ButtonHolder,
                                            Submit)

from forms import BasicInputForm, BasicInputFormLayoutIncluded, AdvancedForm
from utils import read_output, write_output


def test_basic(output_test_path, rendered_template, helper, client):
    form = BasicInputForm()
    pack = helper.template_pack

    rendered = rendered_template(form, helper=helper)

    attempted = read_output(output_test_path, pack, "test_basic.html")
    #write_output(output_test_path, pack, "test_basic.html", rendered)

    assert rendered == attempted


def test_layout(output_test_path, rendered_template, helper, client):
    form = BasicInputFormLayoutIncluded(helper=helper)
    pack = helper.template_pack

    rendered = rendered_template(form)

    attempted = read_output(output_test_path, pack, "test_layout.html")
    #write_output(output_test_path, pack, "test_layout.html", rendered)

    assert rendered == attempted


def test_advanced(output_test_path, rendered_template, helper, client):
    form = AdvancedForm()
    pack = helper.template_pack

    helper.layout = Layout(
        Row(
            Column(
                'simple',
                css_class='six'
            ),
            Column(
                'opt_in',
                css_class='six'
            ),
        ),
        Row(
            Column(
                'longtext'
            ),
        ),
        Row(
            Column(
                ButtonHolder(Submit('submit', 'Submit')),
            ),
            css_class="large"
        ),
    )

    rendered = rendered_template(form, helper=helper)

    attempted = read_output(output_test_path, pack, "test_advanced.html")
    #write_output(output_test_path, pack, "test_advanced.html", rendered)

    assert rendered == attempted
