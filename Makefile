CC := gcc
PYTHON := python

CYTHONIZE := cythonize

SITE_PACKAGES := $(shell $(PYTHON) -c "import site; print(site.getsitepackages()[0])")

compile: compile-libraries compile-app

compile-libraries:
	CYTHONIZE $(SITE_PACKAGES)/flask/ -3 -b

compile-app:
	PYTHON setup.py build_ext --force --inplace

run:
	#env FLASK_APP=app.py flask run
	gunicorn --workers=2 --worker-class="egg:meinheld#gunicorn_worker" app:app

.PHONY: clean
clean:
	@rm -rf *.c *.so build __pycache__ flask
