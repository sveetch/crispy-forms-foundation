"""
Urls for "crispy form foundation" demo
"""
from django.conf.urls import url, patterns
from django.views.generic.base import TemplateView

from .views import FormF5ByFieldsetView, FormF5ByTabView, FormF5ByAccordionView

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name="crispy_demo/index.html"), name='crispy-demo-index'),
    url(r'^$', FormF5ByFieldsetView.as_view(), name='crispy-demo-form-fieldsets'),
    url(r'^fieldsets/$', FormF5ByFieldsetView.as_view(), name='crispy-demo-form-fieldsets'),
    url(r'^tabs/$', FormF5ByTabView.as_view(), name='crispy-demo-form-tabs'),
    url(r'^accordions/$', FormF5ByAccordionView.as_view(), name='crispy-demo-form-accordions'),
    url(r'^success/$', TemplateView.as_view(template_name="crispy_demo/success.html"), name='crispy-demo-success'),
)
