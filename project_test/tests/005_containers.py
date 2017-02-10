import pytest

from crispy_forms_foundation.layout import (Layout, TabHolder, TabItem,
                                            AccordionHolder, AccordionItem)

from forms import AdvancedForm
from utils import read_output, write_output


def test_tab(output_test_path, rendered_template, helper, client):
    form = AdvancedForm()

    helper.layout = Layout(
        TabHolder(
            TabItem('My tab 1', 'simple'),
            TabItem('My tab 2', 'opt_in'),
            TabItem('My tab 3', 'longtext'),
            css_id="meep-meep"
        )
    )

    rendered = rendered_template(form, helper=helper)

    attempted = read_output(output_test_path, "test_tab.html")
    #attempted = ""
    #write_output(output_test_path, "test_tab.html", rendered)

    assert attempted == rendered


def test_accordion(output_test_path, rendered_template, helper, client):
    form = AdvancedForm()

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

    attempted = read_output(output_test_path, "test_accordion.html")
    #attempted = ""
    #write_output(output_test_path, "test_accordion.html", rendered)

    assert attempted == rendered
