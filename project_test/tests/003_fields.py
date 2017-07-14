import os

import pytest

from crispy_forms_foundation.layout import (Layout, InlineField,
                                            InlineSwitchField)

from project_test.tests.forms import BasicInputForm, BoolInputForm
#from project_test.tests.utils import write_output


def test_inlinefield(output_test_path, render_output, rendered_template,
                     helper, client):
    form = BasicInputForm()
    pack = helper.template_pack

    helper.layout = Layout(
        InlineField('simple', label_column='large-7', input_column='large-5',
                    label_class='foobar')
    )

    rendered = rendered_template(form, helper=helper)

    attempted = render_output(os.path.join(output_test_path, pack,
                                           "test_inlinefield.html"))
    #write_output(output_test_path, pack, "test_inlinefield.html", rendered)

    assert attempted == rendered


def test_inlineswitchfield(output_test_path, render_output, rendered_template,
                           helper, client):
    form = BoolInputForm()
    pack = helper.template_pack

    helper.layout = Layout(
        InlineSwitchField('opt_in', label_column='large-8',
                          input_column='large-4', label_class='foobar',
                          switch_class="inline")
    )

    rendered = rendered_template(form, helper=helper)

    attempted = render_output(os.path.join(output_test_path, pack,
                                           "test_inlineswitchfield.html"))
    #write_output(output_test_path, pack, "test_inlineswitchfield.html", rendered)

    assert attempted == rendered
