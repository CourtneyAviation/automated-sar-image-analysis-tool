SHELL:= /usr/bin/env bash

PY:= python3.11

venv:= .venv

vb:= $(venv)/bin/

define vrun
	@source $(vb)activate && $(1)
endef

.PHONY: shell install pipenv clean

shell: install
	$(call vrun, pipenv shell)

install: $(vb)pipenv
	$(call vrun, pipenv install --dev)

pipenv: $(vb)pipenv
$(vb)pipenv: $(venv)/lib/$(PY)/site-packages/setuptools
	$(call vrun, pip install pipenv)

$(venv)/lib/$(PY)/site-packages/setuptools: $(vb)activate
	$(call vrun, pip install --upgrade pip setuptools)

$(vb)activate:
	$(PY) -m venv $(venv)

clean:
	-rm Pipfile.lock
	-rm -fr $(venv)
