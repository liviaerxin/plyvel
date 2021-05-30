#!/bin/sh
set -ux

# check whether `snappy` exist
not_match=0
echo bbb
cmd_output=$(clang -lsnappy 2>&1)
echo aaa
[[ $cmd_output =~ "library not found for -lsnappy" ]] && not_match=1

if [ $not_match -eq 1 ]
then
    echo Not find snappy.
    cd snappy
    mkdir -p build && cd build
    cmake \
        -DBUILD_SHARED_LIBS=off \
        -DCMAKE_POSITION_INDEPENDENT_CODE=on \
        -DSNAPPY_BUILD_BENCHMARKS=off \
        -DSNAPPY_BUILD_TESTS=off \
        .. && cmake --build . --target install

    cd..
    cd..
fi