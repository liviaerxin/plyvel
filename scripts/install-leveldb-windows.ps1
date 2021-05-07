cd leveldb

mkdir build -ea 0

cd build

cmake -G "Visual Studio 16 2019" -A x64 -DLEVELDB_BUILD_TESTS=off -DLEVELDB_BUILD_BENCHMARKS=off ..

cmake --build . --config Release

cd..
cd..