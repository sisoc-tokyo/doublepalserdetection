from distutils.core import setup
from Cython.Build import cythonize

setup(
    #ext_modules = cythonize("parse_csv.pyx")
    #ext_modules = cythonize("signature_detection.pyx")
    ext_modules = cythonize("*.pyx")
)
