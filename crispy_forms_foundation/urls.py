# -*- coding: utf-8 -*-
"""
Url map for sample views
"""
from django.conf.urls.defaults import *

from crispy_forms_foundation.views import SampleView

urlpatterns = patterns('',
    url(r'^$', SampleView.as_view(), name='crispy-foundation-sample-view'),
)
