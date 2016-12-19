"""foo18 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Dummy homepage just for simple ping view
    url(r'^$', TemplateView.as_view(
        template_name="homepage.html"
    ), name='home'),

     url(r'^crispy-forms/', include('project.demo.urls', namespace='crispy-foundation')),
]
