#!/bin/sh
set -eux

cd third_party/leveldb

mkdir -p build && cd build

export CC=clang
export CXX=clang++
export C_INCLUDE_PATH=/usr/local/include # where find snappy header files
export CPLUS_INCLUDE_PATH=/usr/local/include # where find snappy header files
export LIBRARY_PATH=/usr/local/lib # where find snappy library

cmake \
    -DCMAKE_BUILD_TYPE=release \
    -DBUILD_SHARED_LIBS=off \
    -DCMAKE_POSITION_INDEPENDENT_CODE=on \
    -DLEVELDB_BUILD_TESTS=off \
    -DLEVELDB_BUILD_BENCHMARKS=off \
    -DHAVE_SNAPPY=on \
    .. && cmake --build .

mkdir -p Release

libtool -static -o Release/libleveldb.a libleveldb.a /usr/local/lib/libsnappy.a

# cp libleveldb.a Release\

# cd..
# cd..