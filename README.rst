Add support to `Binary Distributions` for building a Platform Wheel (macOS and Windows, tested) with bundling static `leveldb` library for distribution

******************
Getting the Source
******************

.. code-block:: sh

    git clone --recurse-submodules https://github.com/liviaerxin/plyvel

*************
Build leveldb
*************

1. On `macOS`

.. code-block:: sh

    ./scripts/install-leveldb-osx.sh


2. On `Windows`(Visual Studio 16 2019, x64)

.. code-block:: sh

    ./scripts/install-leveldb-windows.sh

************
Build plyvel
************

Prepare virtual enviroment and dependencies,

On `macOS`,

.. code-block:: sh

    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r requirements-dev.txt

On `Windows`,

.. code-block:: sh

    python -m venv venv
    powershell.exe .\venv\Scripts\Activate.ps1
    pip install -r requirements-dev.txt

Build `plyvel` in Local for test,

.. code-block:: sh

    python setup.py build_ext --inplace


Test,

.. code-block:: sh
    
    python -c "import plyvel; print(plyvel.__leveldb_version__); print(plyvel.__version__)"


Build `plyvel` wheel for distribution,

.. code-block:: sh
    
    python setup.py bdist_wheel


Install to System,

.. code-block:: sh
    
    pip3 install dist/plyvel-*.whl


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