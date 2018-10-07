"""
Urls for "crispy form foundation" demo
"""
from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import FormByFieldsetView, FormByTabView, FormByAccordionView, StaticPage

urlpatterns = [
    url(r'^foundation-(?P<foundation_version>\d+)/$',
        FormByFieldsetView.as_view(),
        name='crispy-demo-form-fieldsets'),
    url(r'^foundation-(?P<foundation_version>\d+)/fieldsets/$',
        FormByFieldsetView.as_view(),
        name='crispy-demo-form-fieldsets'),
    url(r'^foundation-(?P<foundation_version>\d+)/tabs/$',
        FormByTabView.as_view(),
        name='crispy-demo-form-tabs'),
    url(r'^foundation-(?P<foundation_version>\d+)/accordions/$',
        FormByAccordionView.as_view(),
        name='crispy-demo-form-accordions'),
    url(r'^foundation-(?P<foundation_version>\d+)/success/$',
        StaticPage.as_view(),
        name='crispy-demo-success'),
]
