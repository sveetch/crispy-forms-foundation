"""
Sandbox URL Configuration
"""
from django.urls import include, re_path
from django.contrib import admin

from django.views.generic.base import TemplateView


urlpatterns = [
    # Dummy homepage just for simple ping view
    re_path(r'^$', TemplateView.as_view(
        template_name="homepage.html"
    ), name='home'),

     re_path(r'^crispy-forms/',
         include('sandbox.demo.urls', namespace='demo')),
]

try:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
except ImportError:
    pass
