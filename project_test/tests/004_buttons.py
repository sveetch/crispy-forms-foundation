import os

import pytest

from crispy_forms_foundation.layout import (Layout, ButtonGroup,
                                            Submit, Button)

from project_test.tests.forms import BasicInputForm
#from project_test.tests.utils import write_output


def test_buttongroup(output_test_path, render_output, rendered_template,
                     helper, client):
    form = BasicInputForm()
    pack = helper.template_pack

    helper.layout = Layout(
        'simple',
        ButtonGroup(
            Submit('Save', 'Save'),
            Button('Cancel', 'Cancel'),
        )
    )

    rendered = rendered_template(form, helper=helper)

    attempted = render_output(os.path.join(output_test_path, pack,
                                           "test_buttongroup.html"))
    #write_output(output_test_path, pack, "test_buttongroup.html", rendered)

    assert attempted == rendered
