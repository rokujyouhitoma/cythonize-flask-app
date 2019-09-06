import sys

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

sources = []

include_dirs = []

libraries = []

CFLAGS = ['-Wall', '-std=c99', '-D_GNU_SOURCE', '-D_FILE_OFFSET_BITS=64', '-O3', '-g']

extentions = [
    Extension('hello',
              sources=['hello.py'] + sources,
              include_dirs=include_dirs,
              libraries=libraries,
              language='c',
              extra_compile_args=CFLAGS),
]

compiler_directives = {
    'language_level': sys.version_info[0]
}

setup(
    name = 'cythonize hello.py',
    ext_modules=cythonize(extentions, compiler_directives=compiler_directives),
)
