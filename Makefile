PYTHON := python

compile:
	PYTHON setup.py build_ext --force --inplace

run:
	env FLASK_APP=app.py flask run

.PHONY: clean
clean:
	@rm -rf *.c *.so build __pycache__
