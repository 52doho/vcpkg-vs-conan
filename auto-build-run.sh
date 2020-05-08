#/usr/bin/bash

[ -d build ] || mkdir build
cd build
# NOTE: replace path
cmake .. -DCMAKE_TOOLCHAIN_FILE=/home/jd/Downloads/SourceCode/vcpkg/scripts/buildsystems/vcpkg.cmake
make -j 6

echo ""
echo "------> build success and running:"
./vcpkg-vs-conan
