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
        )
    )

    rendered = rendered_template(form, helper=helper)

    attempted = read_output(output_test_path, "test_tab.html")
    #attempted = ""
    #write_output(output_test_path, "test_tab.html", rendered)

    assert rendered == attempted


def test_accordion(output_test_path, rendered_template, helper, client):
    """
    NOTE: Fail because accordion generated id can be the same between two test.
          Need to give an id and maybe another test to check id is correctly
          generated ?
    """
    form = AdvancedForm()

    helper.layout = Layout(
        AccordionHolder(
            AccordionItem('Group 1', 'simple'),
            AccordionItem('Group 2', 'opt_in'),
            AccordionItem('Group 3', 'longtext'),
        )
    )

    rendered = rendered_template(form, helper=helper)

    attempted = read_output(output_test_path, "test_accordion.html")
    #attempted = ""
    #write_output(output_test_path, "test_accordion.html", rendered)

    assert rendered == attempted
