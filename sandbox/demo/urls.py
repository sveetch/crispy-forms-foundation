"""
Urls for "crispy form foundation" demo
"""
from django.urls import re_path
from django.views.generic.base import TemplateView

from .views import (
    FormByFieldsetView, FormByTabView, FormByAccordionView, StaticPage
)


app_name = 'demo'

urlpatterns = [
    re_path(r'^foundation-(?P<foundation_version>\d+)/$',
        FormByFieldsetView.as_view(),
        name='crispy-demo-form-fieldsets'),
    re_path(r'^foundation-(?P<foundation_version>\d+)/fieldsets/$',
        FormByFieldsetView.as_view(),
        name='crispy-demo-form-fieldsets'),
    re_path(r'^foundation-(?P<foundation_version>\d+)/tabs/$',
        FormByTabView.as_view(),
        name='crispy-demo-form-tabs'),
    re_path(r'^foundation-(?P<foundation_version>\d+)/accordions/$',
        FormByAccordionView.as_view(),
        name='crispy-demo-form-accordions'),
    re_path(r'^foundation-(?P<foundation_version>\d+)/success/$',
        StaticPage.as_view(),
        name='crispy-demo-success'),
]
