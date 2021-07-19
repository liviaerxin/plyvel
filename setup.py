import os
from os.path import join, dirname
from setuptools import setup
from setuptools.extension import Extension
import platform
from Cython.Build import cythonize

CURRENT_DIR = dirname(__file__)
IsDynamic = True

# with open(join(CURRENT_DIR, "plyvel/_version.py")) as fp:
#     exec(fp.read(), globals(), locals())


# def get_file_contents(filename):
#     with open(join(CURRENT_DIR, filename)) as fp:
#         return fp.read()

# Include Dirs
include_dirs = []
libraries = []
library_dirs = []
extra_objects = []
# add "-fno-rtti" fix `Symbol not found: __ZTIN7leveldb10ComparatorE` when using `leveldb 1.23`. Because `leveldb 1.23` compiled without RTTI(run time type info), if we use "-frtti", `U typeinfo for leveldb::Comparator` will not be found in `leveldb.a` or `leveldb.so`
extra_compile_args = ["-Wall", "-g", "-x", "c++", "-std=c++11", "-fno-rtti"]

if platform.system() == "Darwin":
    extra_compile_args += ["-stdlib=libc++"]
    os.environ["CC"] = "clang"
    os.environ["CXX"] = "clang++"

if IsDynamic:
    # Dynamic Libs
    include_dirs = []
    libraries = ["leveldb"]
else:
    # Static Libs
    include_dirs = ["third_party/leveldb/include"]
    static_libraries = ["leveldb"]
    static_lib_dirs = "third_party/leveldb/build/Release"

    # Linking a static library both for `Windows` and `Linux/Unix`, ref at:
    # [How to statically link a library when compiling a python module extension](https://stackoverflow.com/questions/4597228/how-to-statically-link-a-library-when-compiling-a-python-module-extension)
    if platform.system() == "Windows":
        libraries.extend(static_libraries)
        library_dirs.append(static_lib_dirs)
    else:  # POSIX
        extra_objects = [
            "{}/lib{}.a".format(static_lib_dirs, l) for l in static_libraries
        ]

ext_modules = [
    Extension(
        "plyvel._plyvel",
        language="c++",
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        sources=["src/plyvel/_plyvel.pyx", "src/plyvel/comparator.cpp"],
        libraries=libraries,
        extra_objects=extra_objects,
        extra_compile_args=extra_compile_args,
    )
]

setup(
    # name="plyvel",
    # description="Plyvel, a fast and feature-rich Python interface to LevelDB",
    # long_description=get_file_contents("README.rst"),
    # url="https://github.com/wbolster/plyvel",
    # version=__version__,  # noqa: F821
    # author="Wouter Bolsterlee",
    # author_email="wouter@bolsterl.ee",
    ext_modules=cythonize(ext_modules),
    # package_data = {"plyvel":['*.pxd', '*.h']}, # expose to other libraries to cimport from
    # packages=["plyvel"],
    # license="BSD License",
    # classifiers=[
    #     "Development Status :: 5 - Production/Stable",
    #     "Intended Audience :: Developers",
    #     "Intended Audience :: Information Technology",
    #     "Intended Audience :: Science/Research",
    #     "License :: OSI Approved :: BSD License",
    #     "Operating System :: POSIX",
    #     "Operating System :: Windows",
    #     "Programming Language :: C++",
    #     "Programming Language :: Cython",
    #     "Programming Language :: Python",
    #     "Programming Language :: Python :: 2",
    #     "Programming Language :: Python :: 3",
    #     "Topic :: Database",
    #     "Topic :: Database :: Database Engines/Servers",
    #     "Topic :: Software Development :: Libraries :: Python Modules",
    # ],
)
