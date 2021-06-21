$GLOBAL:oldDir = (Get-Location).Path

cd .\third_party\snappy

mkdir build -ea 0

cd build

cmake -G "Visual Studio 16 2019" -A x64 -DSNAPPY_BUILD_BENCHMARKS=off -DSNAPPY_BUILD_TESTS=off ..

cmake --build . --config Release

cd $GLOBAL:oldDir