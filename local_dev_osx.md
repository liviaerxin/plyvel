# 

## Install Dependency

```sh
❯ python3 -m venv venv
❯ source ./venv/bin/activate

# install forefront build package
❯ pip install -U build

# install build requirements from `pyproject.toml` file
❯ python -c 'import toml; c = toml.load("pyproject.toml");
print("\n".join(c["build-system"]["requires"]))' | pip install -r /dev/stdin

❯ python -c 'import toml; c = toml.load("pyproject.toml");
print("\n".join(c["build-system"]["macos"]["requires"]))' | pip install -r /dev/stdin

❯ python -c 'import toml; c = toml.load("pyproject.toml");
print("\n".join(c["dev"]["tools"]["requires"]))' | pip install -r /dev/stdin

# install dependency library
❯ brew install leveldb
```

## Fast Build and Test

```sh
❯ python setup.py build_ext -i -f

❯ otool -L ./src/plyvel/_plyvel.cpython-39-darwin.so
./src/plyvel/_plyvel.cpython-39-darwin.so:
	/opt/homebrew/opt/leveldb/lib/libleveldb.1.dylib (compatibility version 1.0.0, current version 1.23.0)
	/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 905.6.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1292.100.5)

❯ python -c "from src import plyvel; print(plyvel.__leveldb_version__); print(plyvel.__version__)"
1.23
1.3.0
```

## Final Build

Build,

```sh
❯ python setup.py bdist_wheel
❯ pip install dist/*.whl
❯ python -c "import plyvel; print(plyvel.__leveldb_version__); print(plyvel.__version__)"
```

or more generic

```sh
❯ python -m build
```

Delocate,

```sh
# before delocate,
❯ delocate-listdeps --all dist/plyvel-1.3.0-cp39-cp39-macosx_11_0_arm64.whl
/opt/homebrew/Cellar/leveldb/1.23/lib/libleveldb.1.23.0.dylib
/usr/lib/libSystem.B.dylib
/usr/lib/libc++.1.dylib

❯ unzip -l dist/plyvel-1.3.0-cp39-cp39-macosx_11_0_arm64.whl
Archive:  dist/plyvel-1.3.0-cp39-cp39-macosx_11_0_arm64.whl
  Length      Date    Time    Name
---------  ---------- -----   ----
      339  06-17-2021 13:27   plyvel/__init__.py
   268457  06-23-2021 09:41   plyvel/_plyvel.cpython-39-darwin.so
      190  06-17-2021 13:27   plyvel/_version.py
     1567  06-23-2021 09:41   plyvel-1.3.0.dist-info/LICENSE.rst
     3296  06-23-2021 09:41   plyvel-1.3.0.dist-info/METADATA
      108  06-23-2021 09:41   plyvel-1.3.0.dist-info/WHEEL
        7  06-23-2021 09:41   plyvel-1.3.0.dist-info/top_level.txt
      627  06-23-2021 09:41   plyvel-1.3.0.dist-info/RECORD
---------                     -------
   274591                     8 files


# do delocate,
❯ delocate-wheel -w fixed_wheels -v dist/*.whl
Fixing: dist/plyvel-1.3.0-cp39-cp39-macosx_11_0_arm64.whl
Copied to package .dylibs directory:
  /opt/homebrew/Cellar/gperftools/2.9.1/lib/libtcmalloc.4.dylib
  /opt/homebrew/Cellar/leveldb/1.23/lib/libleveldb.1.23.0.dylib
  /opt/homebrew/Cellar/snappy/1.1.9/lib/libsnappy.1.1.9.dylib

# after delocate,
❯ delocate-listdeps --all fixed_wheels/plyvel-1.3.0-cp39-cp39-macosx_11_0_arm64.whl
/usr/lib/libSystem.B.dylib
/usr/lib/libc++.1.dylib
@loader_path/.dylibs/libleveldb.1.23.0.dylib
@loader_path/libsnappy.1.1.9.dylib
@loader_path/libtcmalloc.4.dylib

❯ unzip -l fixed_wheels/plyvel-1.3.0-cp39-cp39-macosx_11_0_arm64.whl
Archive:  fixed_wheels/plyvel-1.3.0-cp39-cp39-macosx_11_0_arm64.whl
  Length      Date    Time    Name
---------  ---------- -----   ----
      922  06-23-2021 17:44   plyvel-1.3.0.dist-info/RECORD
      108  06-23-2021 09:41   plyvel-1.3.0.dist-info/WHEEL
     1567  06-23-2021 09:41   plyvel-1.3.0.dist-info/LICENSE.rst
        7  06-23-2021 09:41   plyvel-1.3.0.dist-info/top_level.txt
     3296  06-23-2021 09:41   plyvel-1.3.0.dist-info/METADATA
      190  06-17-2021 13:27   plyvel/_version.py
      339  06-17-2021 13:27   plyvel/__init__.py
   268464  06-23-2021 17:44   plyvel/_plyvel.cpython-39-darwin.so
   303728  06-23-2021 17:44   plyvel/.dylibs/libleveldb.1.23.0.dylib
    94336  06-23-2021 17:44   plyvel/.dylibs/libsnappy.1.1.9.dylib
   284272  06-23-2021 17:44   plyvel/.dylibs/libtcmalloc.4.dylib
---------                     -------
   957229                     11 files
```

Upload,