Add support to `Binary Distributions` for building a Platform Wheel (macOS and Windows, tested)

## Getting the Source

```sh
git clone --recurse-submodules https://github.com/liviaerxin/plyvel
```

## Build leveldb

1. On `macOS`

```sh
./scripts/install-leveldb-osx.sh
```

2. On `Windows`


## Build plyvel

Build in Local,
```sh
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements-dev.txt
python3 setup.py build_ext --inplace
```

Test,
```sh
python3 -c "import plyvel; print(plyvel.__leveldb_version__); print(plyvel.__version__)"
```

Build Wheel,
```
python3 setup.py bdist_wheel
```

Install to System,
```sh
pip3 install dist/plyvel-*.whl
```

======
Plyvel
======

.. image:: https://travis-ci.org/wbolster/plyvel.svg?branch=master
    :target: https://travis-ci.org/wbolster/plyvel

**Plyvel** is a fast and feature-rich Python interface to LevelDB_.

Plyvel has a rich feature set, high performance, and a friendly Pythonic API.
See the documentation and project page for more information:

* Documentation_
* `Project page`_
* `PyPI page`_

.. _Project page: https://github.com/wbolster/plyvel
.. _Documentation: https://plyvel.readthedocs.io/
.. _PyPI page: http://pypi.python.org/pypi/plyvel/
.. _LevelDB: http://code.google.com/p/leveldb/

Note that using a released version is recommended over a checkout from version
control. See the installation docs for more information.