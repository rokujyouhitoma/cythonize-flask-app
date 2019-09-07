CC := gcc
PYTHON := python

CYTHONIZE := cythonize

SITE_PACKAGES := $(shell $(PYTHON) -c "import site; print(site.getsitepackages()[0])")

compile: compile-app

compile-app:
	PYTHON setup.py build_ext --force --inplace

run:
	PYTHON app.py

.PHONY: clean
clean:
	@rm -rf __pycache__
