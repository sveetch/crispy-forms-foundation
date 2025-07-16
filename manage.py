#!/usr/bin/env python
"""
Django management script for sandbox
"""
import os

from django.core import management

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sandbox.settings.demo")

    management.execute_from_command_line()
