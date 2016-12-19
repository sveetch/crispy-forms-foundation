# -*- coding: utf-8 -*-
"""
Views
"""
from django import template
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView

from crispy_forms_foundation import __version__ as crispy_forms_foundation_version
from crispy_forms import __version__ as crispy_forms_version
from .forms import FormByFieldsetsForm, FormByTabsForm, FormByAccordionsForm

class FormContainersMixin(object):
    def get_versions(self):
        return {
            "django_crispy_forms": crispy_forms_version,
            "crispy_forms_foundation": crispy_forms_foundation_version,
        }
    
    def get_success_url(self):
        return reverse('crispy-demo-success', args=[])


class FormF5ByFieldsetView(FormContainersMixin, FormView):
    template_name = 'crispy_demo/fieldsets.html'
    form_class = FormByFieldsetsForm


class FormF5ByTabView(FormContainersMixin, FormView):
    template_name = 'crispy_demo/tabs.html'
    form_class = FormByTabsForm


class FormF5ByAccordionView(FormContainersMixin, FormView):
    template_name = 'crispy_demo/accordions.html'
    form_class = FormByAccordionsForm
