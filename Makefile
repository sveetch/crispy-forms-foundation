PYTHON_INTERPRETER=python3
VENV_PATH=.venv
PIP=$(VENV_PATH)/bin/pip
DJANGO_MANAGE=$(VENV_PATH)/bin/python sandbox/manage.py
FLAKE=$(VENV_PATH)/bin/flake8
PYTEST=$(VENV_PATH)/bin/pytest

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install             -- to install this project with virtualenv and Pip"
	@echo ""
	@echo "  clean               -- to clean EVERYTHING"
	@echo "  clean-data          -- to clean data (uploaded medias, database, etc..)"
	@echo "  clean-install       -- to clean installation"
	@echo "  clean-pycache       -- to remove all __pycache__, this is recursive from current directory"
	@echo ""
	@echo "  migrate             -- to apply demo database migrations"
	@echo "  run                 -- to run Django development server"
	@echo "  shell               -- to run Django shell"
	@echo "  superuser           -- to create a superuser for Django admin"
	@echo ""
	@echo "  flake               -- to launch Flake8 checking"
	@echo "  tests               -- to launch tests using Pytest"
	@echo "  quality             -- to launch Flake8 checking and Pytest"
	@echo

clean-pycache:
	find . -type d -name "__pycache__"|xargs rm -Rf
.PHONY: clean-pycache

clean-install:
	rm -Rf $(VENV_PATH)
	rm -Rf .tox
	rm -Rf crispy_forms_foundation.egg-info
.PHONY: clean-install

clean-data:
	rm -Rf data
.PHONY: clean-data

clean: clean-install clean-pycache clean-data
.PHONY: clean

venv:
	virtualenv -p $(PYTHON_INTERPRETER) $(VENV_PATH)
	# This is required for those ones using ubuntu<16.04
	$(PIP) install --upgrade pip
	$(PIP) install --upgrade setuptools
.PHONY: venv

migrate:
	mkdir -p data/db
	$(DJANGO_MANAGE) migrate
.PHONY: migrate

shell:
	$(DJANGO_MANAGE) shell
.PHONY: shell

superuser:
	$(DJANGO_MANAGE) createsuperuser
.PHONY: superuser

install: venv
	mkdir -p data
	$(PIP) install -e .[dev]
	${MAKE} migrate
.PHONY: install

run:
	$(DJANGO_MANAGE) runserver 0.0.0.0:8001
.PHONY: run

flake:
	$(FLAKE) --show-source crispy_forms_foundation
.PHONY: flake

tests:
	$(PYTEST) -vv --exitfirst tests/
.PHONY: tests

quality: tests flake
.PHONY: quality
