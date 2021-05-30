#!/bin/sh
set -eux

cd leveldb

mkdir -p build && cd build

export CC=clang
export CXX=clang++
export C_INCLUDE_PATH=/usr/local/include
export CPLUS_INCLUDE_PATH=/usr/local/include
export LIBRARY_PATH=/usr/local/lib

cmake \
    -DCMAKE_BUILD_TYPE=release \
    -DBUILD_SHARED_LIBS=off \
    -DCMAKE_POSITION_INDEPENDENT_CODE=on \
    -DLEVELDB_BUILD_TESTS=off \
    -DLEVELDB_BUILD_BENCHMARKS=off \
    -DHAVE_SNAPPY=on \
    # -DSNAPPY_BUILD_BENCHMARKS=off \
    # -DSNAPPY_BUILD_TESTS=off \
    .. && cmake --build .

mkdir -p Release

cp libleveldb.a Release\

cd..
cd..