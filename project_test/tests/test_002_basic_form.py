import pytest

from django import forms
from django.template import Context, Template

from crispy_forms.helper import FormHelper

from forms import BasicForm, LayoutForm


@pytest.mark.parametrize("foundation_version", [5])
def test_basic_form(client, foundation_version):
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

    attempted = ("""<form  method="post"><fieldset class="">"""
           """<legend></legend>"""
           """<div id="div_id_simple" class="holder">"""
           """<label for="id_simple" class="required">\n"""
           """                Simple text<span class="asterisk">*</span></label>"""
           """<input class="textinput textInput" id="id_simple" name="simple" """
           """required="" type="text" /></div></fieldset></form>""")

    assert template.render(context) == attempted


@pytest.mark.parametrize("foundation_version", [5])
def test_layout_form(client, foundation_version):
    basic_form = LayoutForm(foundation_version=foundation_version)

    # Use crispy templatetag to return string of generated form
    context = Context({
        "form": basic_form,
        #"form_helper": helper,
    })
    template = Template(("""{% spaceless %}{% load crispy_forms_tags %}"""
                         """{% crispy form %}{% endspaceless %}"""))

    attempted = ("""<form  action="." method="post">"""
                 """<div id="div_id_simple" class="holder">"""
                 """<label for="id_simple" class="required">\n"""
                 """                Simple text<span class="asterisk">*"""
                 """</span></label><input class="textinput textInput" """
                 """id="id_simple" name="simple" required="" type="text" />"""
                 """</div></form>""")

    assert template.render(context) == attempted
