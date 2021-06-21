$GLOBAL:oldDir = (Get-Location).Path
$GLOBAL:incDir = Join-Path $GLOBAL:oldDir '\third_party\snappy'
$GLOBAL:libDir = Join-Path $GLOBAL:oldDir '\third_party\snappy\build\Release'

SET ILink_LibraryPath=$GLOBAL:incDir

cd third_party\leveldb

mkdir build -ea 0

cd build

cmake -G "Visual Studio 16 2019" -A x64 -DLEVELDB_BUILD_TESTS=off -DLEVELDB_BUILD_BENCHMARKS=off -DHAVE_SNAPPY=on ..

cmake --build . --config Release

$GLOBAL:levellib = Join-Path $GLOBAL:oldDir '\third_party\leveldb\build\Release\leveldb.lib'
$GLOBAL:snappylib = Join-Path $GLOBAL:oldDir '\third_party\snappy\build\Release\snappy.lib'

LIB.EXE /OUT:$GLOBAL:levellib $GLOBAL:levellib $GLOBAL:snappylib

cd $GLOBAL:oldDir