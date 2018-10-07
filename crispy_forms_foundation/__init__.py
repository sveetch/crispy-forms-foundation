# -*- coding: utf-8 -*-
"""Django application to add 'django-crispy-forms' layout objects for 'Foundation for sites'"""  # noqa: E501
from __future__ import absolute_import, unicode_literals

import os
from setuptools.config import read_configuration

import pkg_resources

PROJECT_DIR = os.path.join(os.path.dirname(__file__), "..")


def _extract_version(package_name):
    """
    Get package version from installed distribution or configuration file if not
    installed
    """
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        _conf = read_configuration(os.path.join(PROJECT_DIR, "setup.cfg"))
    return _conf["metadata"]["version"]


__version__ = _extract_version("crispy_forms_foundation")
