"""
Django settings for project demonstration
"""
#from __future__ import absolute_import, unicode_literals

from sandbox.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Enabled django-debug-toolbar, you may need to fill your IP in FOO within your
# 'local' settings file
INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (  # noqa
    'debug_toolbar',
)

MIDDLEWARE[0:0] = [  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


#
# Default crispy_forms_foundation settings
#
from crispy_forms_foundation.settings import *


#
# django-debug-toolbar settings
#
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
]

try:
    from sandbox.settings.local import *  # noqa
except ImportError:
    pass
