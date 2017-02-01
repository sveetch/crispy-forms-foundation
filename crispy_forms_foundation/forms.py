# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from copy import deepcopy

from django import forms
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper

from .layout import Submit, HTML, InlineSwitchField


class FoundationFormMixin(object):
    """
    Mixin to implement the layout helper that will automatically build a form
    layout

    Generally, you will prefer to use ``FoundationForm`` or
    ``FoundationModelForm`` instead.

    If you still want to directly use this mixin you'll just have to execute
    ``FoundationFormMixin.init_helper()`` in your form init.

    **Attributes**

    title
        If set, defines the form's title
    layout
        If set, override the default layout for the form
    error_title
        Defines the error title for non field errors
    form_id
        Defines the id of the form
    classes
        Defines the classes used on the form
    action
        Defines the action of the form. ``reverse`` will be called on the
        value. On failure the value will be assigned as is
    method
        Defines the method used for the action
    attrs
        Defines the attributes of the form
    switches
        If True, will replace all fields checkboxes with switches
    submit
        Adds a submit button on the form. Can be set to a Submit object or
        a string which will be used as the value of the submit button
    title_templatestring
        Template string used to display form title (if any)
    """
    title = None
    layout = None
    error_title = _("Errors :")
    form_id = None
    classes = "foundation-form"
    action = ""
    method = "post"
    attrs = {}
    switches = True
    submit = True
    title_templatestring = u"<h3 class=\"subheader\">{0}</h3>"

    def init_helper(self):
        # Put required HTML attribute on required fields so they are managed by
        # Abide (if enabled)
        if "data_abide" in self.attrs:
            for field in self.fields.values():
                if field.required:
                    field.widget.attrs["required"] = ""
                    field.abide_msg = _("This field is required.")

        if not self.layout:
            # Start with an empty layout
            self.helper = FormHelper(self)
        else:
            # Start from the given layout
            self.helper = FormHelper()
            self.helper.layout = deepcopy(self.layout)

        # Try to reverse form_action url, else fallback to use it as a simple
        # string
        try:
            self.helper.form_action = reverse(self.action)
        except NoReverseMatch:
            self.helper.form_action = self.action

        if self.title:
            html = HTML(self.title_templatestring.format(self.title))
            self.helper.layout.insert(0, html)

        if self.form_id is not None:
            self.helper.form_id = self.form_id

        self.helper.form_class = self.classes
        self.helper.form_method = self.method
        self.helper.form_error_title = self.error_title
        self.helper.attrs = self.attrs

        if self.switches:
            # Get a list of all fields with their location within the layout
            layout_field_names = self.helper.layout.get_field_names()
            # Transform checkbox fields to switches element
            for pointer in layout_field_names:
                if isinstance(self.fields[pointer[1]].widget,
                              forms.CheckboxInput):
                    field = InlineSwitchField(pointer[1],
                                              switch_class="inline")
                    self.replace_layout_object(pointer[0], field)

        if self.submit:
            if isinstance(self.submit, Submit):
                self.helper.add_input(self.submit)
            elif isinstance(self.submit, str):
                self.helper.add_input(Submit('submit', self.submit))
            else:
                self.helper.add_input(Submit('submit', _("Submit")))

    def replace_layout_object(self, position, instead):
        previous_layout_object = None
        layout_object = self.helper.layout.fields[position[0]]

        for i in position[1:]:
            previous_layout_object = layout_object
            layout_object = layout_object.fields[i]

        if previous_layout_object:
            previous_layout_object[-1] = instead
        else:
            self.helper.layout.fields[position[0]] = instead


class FoundationForm(FoundationFormMixin, forms.Form):
    """
    A **Django form** that inherit from ``FoundationFormMixin`` to
    automatically build a form layout

    Example:

    .. sourcecode:: python

        from django import forms
        from crispy_forms_foundation.forms import FoundationForm

        class YourForm(FoundationForm):
            title = "Testing"
            action = 'test'
            layout = Layout(Fieldset("Section", "my_field", "my_field_2"))
            switches = False
            attrs = {'data_abide': ""}

            title = forms.CharField(label='Title', required=True)
            slug = forms.CharField(label='Slug', required=False)

    """
    def __init__(self, *args, **kwargs):
        super(FoundationForm, self).__init__(*args, **kwargs)
        self.init_helper()


class FoundationModelForm(FoundationFormMixin, forms.ModelForm):
    """
    A **Django Model form** that inherit from ``FoundationFormMixin`` to
    automatically build a form layout

    Example:

    .. sourcecode:: python

        from crispy_forms_foundation.forms import FoundationModelForm

        class YourForm(FoundationModelForm):
            title = "Testing"
            action = 'test'
            layout = Layout(Fieldset("Section", "my_field", "my_field_2"))
            switches = False
            attrs = {'data_abide': ""}

            class Meta:
                model = MyModel
                fields = ['my_field', 'my_field_2', 'my_field_3']

    """
    def __init__(self, *args, **kwargs):
        super(FoundationModelForm, self).__init__(*args, **kwargs)
        self.init_helper()
