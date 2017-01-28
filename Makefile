PYTHON2_PATH=`which python2.7`

.PHONY: help clean delpyc tests flake quality

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  delpyc              -- to remove all *.pyc files, this is recursive from the current directory"
	@echo "  clean               -- to clean local repository from all stuff created during development"
	@echo
	@echo "  flake               -- to launch Flake8 checking on boussole code (not the tests)"
	@echo "  tests               -- to launch tests using py.test"
	@echo "  quality             -- to launch Flake8 checking and tests with py.test"
	@echo
	@echo "  server              -- to launch a Django instance on 0.0.0.0:8001"
	@echo

delpyc:
	find . -name "*\.pyc"|xargs rm -f

clean: delpyc
	rm -Rf dist .tox crispy_forms_foundation.egg-info .cache project_test/.cache/ project_test/tests/__pycache__/ docs/_build

flake:
	flake8 --show-source crispy_forms_foundation

tests:
	py.test -vv project_test/

quality: tests flake

server:
	cd project_test && ./manage.py runserver 0.0.0.0:8001

docserver:
	sphinx-autobuild --host 0.0.0.0 --port 9000 docs docs/_build/html
