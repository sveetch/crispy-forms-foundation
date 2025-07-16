# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys


# Settings file required by Django
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sandbox.settings.documentation")


# Setup Django
import django

django.setup()


# Get the module version
from crispy_forms_foundation import __version__ as crispy_forms_foundation_version

# -- Project information -----------------------------------------------------

now = datetime.date.today()
project = "crispy-form-foundation"
copyright = "2014-{}, David THENON".format(now.year)
author = "David THENON"

# The short X.Y version
version = crispy_forms_foundation_version
# The full version, including alpha/beta/rc tags
release = crispy_forms_foundation_version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.todo",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Use index.rst as root content doc file
master_doc = "index"


# -- Options for HTML output -------------------------------------------------

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = "_static/logo.png"

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# For Furo theme
html_theme = "furo"
html_title = "{name}<br><small>v{version}</small>".format(
    name=project,
    version=version,
)

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/sveetch/crispy-forms-foundation",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
    "source_repository": "https://github.com/sveetch/crispy-forms-foundation/",
    "source_branch": "master",
    "source_directory": "docs/",
}

# Apply some CSS patch to Furo
html_css_files = [
    "css/furo-adjustments.css",
]

# -- Autodoc config---------- -------------------------------------------------

# Do not order autodoc contents by alphabetical, keep to the source order
autodoc_member_order = "bysource"
