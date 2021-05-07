import os
from os.path import join, dirname
from setuptools import setup
from setuptools.extension import Extension
import platform

CURRENT_DIR = dirname(__file__)

with open(join(CURRENT_DIR, "plyvel/_version.py")) as fp:
    exec(fp.read(), globals(), locals())


def get_file_contents(filename):
    with open(join(CURRENT_DIR, filename)) as fp:
        return fp.read()


extra_compile_args = ["-Wall", "-g", "-x", "c++", "-std=c++11"]

if platform.system() == "Darwin":
    extra_compile_args += ["-stdlib=libc++"]
    os.environ["CC"] = "clang"
    os.environ["CXX"] = "clang++"

include_dirs = ["leveldb/include"]
static_libraries = ["leveldb"]
static_lib_dirs = "leveldb/build/Release"
libraries = []
library_dirs = []

# Linking a static library both for `Windows` and `Linux/Unix`, ref at:
# [How to statically link a library when compiling a python module extension](https://stackoverflow.com/questions/4597228/how-to-statically-link-a-library-when-compiling-a-python-module-extension)
if platform.system() == "Windows":
    libraries.extend(static_libraries)
    library_dirs.append(static_lib_dirs)
    extra_objects = []
else:  # POSIX
    extra_objects = ["{}/lib{}.a".format(static_lib_dirs, l) for l in static_libraries]
    extra_compile_args += ["-fno-rtti"] # fix `Symbol not found: __ZTIN7leveldb10ComparatorE` using `leveldb 1.23`

ext_modules = [
    Extension(
        "plyvel._plyvel",
        language="c++",
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        sources=["plyvel/_plyvel.pyx", "plyvel/comparator.cpp"],
        libraries=libraries,
        extra_objects=extra_objects,
        extra_compile_args=extra_compile_args,
    )
]

setup(
    name="plyvel",
    description="Plyvel, a fast and feature-rich Python interface to LevelDB",
    long_description=get_file_contents("README.rst"),
    url="https://github.com/wbolster/plyvel",
    version=__version__,  # noqa: F821
    author="Wouter Bolsterlee",
    author_email="wouter@bolsterl.ee",
    ext_modules=ext_modules,
    packages=["plyvel"],
    license="BSD License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: Windows",
        "Programming Language :: C++",
        "Programming Language :: Cython",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
