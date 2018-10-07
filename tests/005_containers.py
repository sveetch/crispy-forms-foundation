import os

import pytest
from django.test.html import parse_html

from crispy_forms_foundation.layout import (Layout, TabHolder, TabItem,
                                            AccordionHolder, AccordionItem)

from tests.forms import AdvancedForm
#from tests.utils import write_output


def test_tab(output_test_path, render_output, rendered_template, helper,
             client):
    form = AdvancedForm()
    pack = helper.template_pack

    helper.layout = Layout(
        TabHolder(
            TabItem('My tab 1', 'simple'),
            TabItem('My tab 2', 'opt_in'),
            TabItem('My tab 3', 'longtext'),
            css_id="meep-meep"
        )
    )

    rendered = rendered_template(form, helper=helper)

    attempted = render_output(os.path.join(output_test_path, pack,
                                           "test_tab.html"))
    #write_output(output_test_path, pack, "test_tab.html", rendered)

    assert parse_html(attempted) == parse_html(rendered)


def test_accordion(output_test_path, render_output, rendered_template, helper,
                   client):
    form = AdvancedForm()
    pack = helper.template_pack

    # Define 'css_id' to avoid test fails with automatic generated random ID
    helper.layout = Layout(
        AccordionHolder(
            AccordionItem('Group 1', 'simple'),
            AccordionItem('Group 2', 'opt_in'),
            AccordionItem('Group 3', 'longtext'),
            css_id="meep-meep"
        )
    )

    rendered = rendered_template(form, helper=helper)

    attempted = render_output(os.path.join(output_test_path, pack,
                                           "test_accordion.html"))
    #write_output(output_test_path, pack, "test_accordion.html", rendered)

    assert parse_html(attempted) == parse_html(rendered)
