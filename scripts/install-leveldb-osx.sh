#!/bin/sh
set -eux

cd leveldb

mkdir -p build && cd build

export CC=clang
export CXX=clang++

cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POSITION_INDEPENDENT_CODE=on \
    -DLEVELDB_BUILD_TESTS=off \
    -DLEVELDB_BUILD_BENCHMARKS=off \
    .. && cmake --build .

mkdir -p Release

cp libleveldb.a Release\