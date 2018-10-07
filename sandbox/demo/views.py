# -*- coding: utf-8 -*-
"""
Views
"""
from django import template
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
try:
    # Default 'reverse' path since Django1.10
    from django.urls import reverse
except ImportError:
    # 'reverse' path for Django<1.10
    from django.core.urlresolvers import reverse

from crispy_forms_foundation import __version__ as crispy_foundation_version
from crispy_forms import __version__ as crispy_version
from .forms import FormByFieldsetsForm, FormByTabsForm, FormByAccordionsForm


class CrispyFoundationMixin(object):
    def get_versions(self):
        return {
            "foundation_version": self.kwargs.get('foundation_version'),
            "django_crispy_forms": crispy_version,
            "crispy_forms_foundation": crispy_foundation_version,
        }

    def get_context_data(self, **kwargs):
        context = super(CrispyFoundationMixin, self).get_context_data(**kwargs)
        context.update(self.get_versions())
        return context


class FormContainersMixin(object):
    def get_success_url(self):
        return reverse('crispy-foundation:crispy-demo-success', kwargs={
            'foundation_version': int(self.kwargs.get('foundation_version'))
        })

    def get_form_kwargs(self):
        """
        Pass template pack argument
        """
        kwargs = super(FormContainersMixin, self).get_form_kwargs()
        kwargs.update({
            'pack': "foundation-{}".format(self.kwargs.get('foundation_version'))
        })
        return kwargs


class FormByFieldsetView(FormContainersMixin, CrispyFoundationMixin, FormView):
    template_name = 'crispy_demo/fieldsets.html'
    form_class = FormByFieldsetsForm


class FormByTabView(FormContainersMixin, CrispyFoundationMixin, FormView):
    template_name = 'crispy_demo/tabs.html'
    form_class = FormByTabsForm


class FormByAccordionView(FormContainersMixin, CrispyFoundationMixin, FormView):
    template_name = 'crispy_demo/accordions.html'
    form_class = FormByAccordionsForm


class StaticPage(FormContainersMixin, CrispyFoundationMixin, TemplateView):
    template_name = 'crispy_demo/success.html'
