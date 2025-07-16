"""
Django settings for documentation

This is required since documentation use Sphinx extension 'autodoc' which loads some
application code that import Django and so require a settings file just to setup.

If you don't plan to documentate code which involves Django, you should not need of
this settings files and should remove its occurence and Django occurences from
``docs/conf.py``.
"""
from sandbox.settings.base import *  # noqa: F403
