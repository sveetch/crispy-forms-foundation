#!/usr/bin/env python
"""
Sandbox management script
"""
import os

from django.core import management

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.demo")

    management.execute_from_command_line()
