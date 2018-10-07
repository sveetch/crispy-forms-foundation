"""
Sandbox URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic.base import TemplateView

urlpatterns = [
    # Dummy homepage just for simple ping view
    url(r'^$', TemplateView.as_view(
        template_name="homepage.html"
    ), name='home'),

     url(r'^crispy-forms/',
         include('sandbox.demo.urls')),
]

try:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
except ImportError:
    pass
