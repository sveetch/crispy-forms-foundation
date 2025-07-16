#!/usr/bin/env python
"""
A script to launch a livereload server to watch and rebuild documentation on sources
changes.

You need to have project with documentation requirements to use it.

Once launched, server will be available on port 8002, like: ::

    http://localhost:8002/

Borrowed from: ::

    https://livereload.readthedocs.io/en/latest/#script-example-sphinx

"""
from pathlib import Path

from livereload import Server, shell

server = Server()

# Watch document sources
server.watch("docs/*.rst", shell("make html", cwd="docs"))
server.watch("docs/*/**.rst", shell("make html", cwd="docs"))
server.watch("*.rst", shell("make html", cwd="docs"))


# Watch Python modules for autodoc review
server.watch("crispy_forms_foundation/*.py", shell("make html", cwd="docs"))
server.watch("crispy_forms_foundation/*/**.py", shell("make html", cwd="docs"))

# Serve the builded documentation
server.serve(root="docs/_build/html", port=8002, host="0.0.0.0")
