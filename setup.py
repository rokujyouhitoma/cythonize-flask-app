from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    name = "cythonize hello.py",
    ext_modules=[
    Extension("hello",
              sources=["hello.py"],
              extra_compile_args=["-O3"],
              language="c")
    ],
    cmdclass = {"build_ext": build_ext}
)
