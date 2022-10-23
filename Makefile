PYTHON_INTERPRETER=python3
VENV_PATH=.venv
PIP=$(VENV_PATH)/bin/pip
DJANGO_MANAGE=$(VENV_PATH)/bin/python sandbox/manage.py
FLAKE=$(VENV_PATH)/bin/flake8
SPHINX_RELOAD=$(VENV_PATH)/bin/python sphinx_reload.py
PYTEST=$(VENV_PATH)/bin/pytest
TOX=$(VENV_PATH)/bin/tox
TWINE=$(VENV_PATH)/bin/twine

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install             -- to install this project with virtualenv and Pip"
	@echo ""
	@echo "  clean               -- to clean EVERYTHING"
	@echo "  clean-data          -- to clean data (uploaded medias, database, etc..)"
	@echo "  clean-doc           -- to remove documentation builds"
	@echo "  clean-install       -- to clean installation"
	@echo "  clean-pycache       -- to remove all __pycache__, this is recursive from current directory"
	@echo ""
	@echo "  migrate             -- to apply demo database migrations"
	@echo "  run                 -- to run Django development server for demo"
	@echo "  shell               -- to run Django shell"
	@echo "  superuser           -- to create a superuser for Django admin"
	@echo
	@echo "  docs                -- to build documentation"
	@echo
	@echo "  flake               -- to launch Flake8 checking"
	@echo "  test               -- to launch tests using Pytest"
	@echo "  tox                 -- to launch tests for every Tox environments"
	@echo "  quality             -- to launch Flake8 checking and Pytest"
	@echo
	@echo "  check-release       -- to check package release before uploading it to PyPi"
	@echo "  release             -- to release package for latest version on PyPi (once release has been pushed to repository)"
	@echo

clean-pycache:
	@echo ""
	@echo "==== Clear Python cache ===="
	@echo ""
	rm -Rf .pytest_cache
	find . -type d -name "__pycache__"|xargs rm -Rf
	find . -name "*\.pyc"|xargs rm -f
.PHONY: clean-pycache

clean-install:
	@echo ""
	@echo "==== Clear installation ===="
	@echo ""
	rm -Rf $(VENV_PATH)
	rm -Rf .tox
	rm -Rf crispy_forms_foundation.egg-info
.PHONY: clean-install

clean-doc:
	@echo ""
	@echo "==== Clear documentation ===="
	@echo ""
	rm -Rf docs/_build
.PHONY: clean-doc

clean-data:
	@echo ""
	@echo "==== Clear sandbox data ===="
	@echo ""
	rm -Rf data
.PHONY: clean-data

clean: clean-doc clean-install clean-pycache clean-data
.PHONY: clean

venv:
	@echo ""
	@echo "==== Install virtual environment ===="
	@echo ""
	virtualenv -p $(PYTHON_INTERPRETER) $(VENV_PATH)
	# This is required for those ones using ubuntu<16.04
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade setuptools
.PHONY: venv

migrate:
	@echo ""
	@echo "==== Apply pending migrations ===="
	@echo ""
	mkdir -p data/db
	$(DJANGO_MANAGE) migrate
.PHONY: migrate

shell:
	@echo ""
	@echo "==== Running Django shell ===="
	@echo ""
	$(DJANGO_MANAGE) shell
.PHONY: shell

superuser:
	@echo ""
	@echo "==== Create new superuser ===="
	@echo ""
	$(DJANGO_MANAGE) createsuperuser
.PHONY: superuser

install: venv
	@echo ""
	@echo "==== Install everything for development ===="
	@echo ""
	mkdir -p data
	$(PIP) install -e .[dev,test,quality,doc]
	${MAKE} migrate
.PHONY: install

docs:
	@echo ""
	@echo "==== Build documentation ===="
	@echo ""
	cd docs && make html
.PHONY: docs

livedocs:
	@echo ""
	@echo "==== Watching documentation sources ===="
	@echo ""
	$(SPHINX_RELOAD)
.PHONY: livedocs

run:
	@echo ""
	@echo "==== Running development server ===="
	@echo ""
	$(DJANGO_MANAGE) runserver 0.0.0.0:8001
.PHONY: run

flake:
	@echo ""
	@echo "==== Flake ===="
	@echo ""
	$(FLAKE) --show-source crispy_forms_foundation tests
.PHONY: flake

test:
	@echo ""
	@echo "==== Tests ===="
	@echo ""
	$(PYTEST) -vv tests/
.PHONY: test

build-package:
	@echo ""
	@echo "==== Build package ===="
	@echo ""
	rm -Rf dist
	$(VENV_PATH)/bin/python setup.py sdist
.PHONY: build-package

release: build-package
	@echo ""
	@echo "==== Release ===="
	@echo ""
	$(TWINE) upload dist/*
.PHONY: release

check-release: build-package
	@echo ""
	@echo "==== Check package ===="
	@echo ""
	$(TWINE) check dist/*
.PHONY: check-release

tox:
	@echo ""
	@echo "==== Launch all Tox environments ===="
	@echo ""
	$(TOX)
.PHONY: tox

quality: test flake docs check-release
	@echo ""
	@echo "♥ ♥ Everything should be fine ♥ ♥"
	@echo ""
.PHONY: quality
