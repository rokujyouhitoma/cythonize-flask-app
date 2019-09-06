PYTHON=python

compile:
	PYTHON setup.py build_ext --inplace

run:
	env FLASK_APP=app.py flask run

clean:
	rm -rf __pycache__ build/ hello.c hello.cpython-36m-darwin.so
